from dataclasses import dataclass
from queue import Queue
from time import time
from typing import List

import cv2
import numpy as np
from pynput import mouse
from PySide6.QtGui import QPainter, QPixmap, QImage

from modes import get_mode

id = 0
parent_id = 0

t = time()
drawing = False
middle_point = []
last_point = []
MOUSE_QUEUE = Queue()
MOUSE_DELAY = 0.2

def on_click(x, y, button, pressed):
    global temp_layer, drawing, last_point, middle_point
    drawing = pressed

    # if pressed:
    #     temp_layer = np.zeros((800, 800, 3), np.uint8)
    #     middle_point = []
    #     last_point = []
    # else:
    #     img = cv2.addWeighted(img, 0.7, temp_layer, 0.3, 0)

def on_move(x, y):
    global drawing, t, last_point, middle_point, MOUSE_DELAY
    
    if drawing:
        t_2 = time()
        if t_2 - t > MOUSE_DELAY:
            t = t_2
            if not middle_point:
                middle_point = [x, y]
            if not last_point:
                last_point = [x, y]

            MOUSE_QUEUE.put([[x, y], middle_point, last_point])

            last_point = middle_point
            middle_point = [x, y]

listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
)
listener.start()

# while(1):
#     k = cv2.waitKey(1) & 0xFF
#     # cv2.imshow('image',img)

#     # cv.curve = cv.curve(curvePoints, true)
#     if not MOUSE_QUEUE.empty():
#         # [x, y] = [int(x) for x in q.get()]
#         pts = np.array(MOUSE_QUEUE.get(), np.int32)

class Layer:
    pass

@dataclass
class ArtBoard:
    def __init__(self):
        self.width = 1000
        self.height = 500
        self.channels = 4
        self.grid_size = 20
        self.layers: list[Layer] = []
        self.background: Layer = None
        self.active_layer_index = 2
        self.cache = [None, None]

        self.initialize()

        self.new_layer(name='Background', opacity=0.5)
        self.new_layer(opacity=0.5)
        self.new_layer(mode='Subtract', opacity=0.5)
        self.new_layer(mode='Subtract', opacity=0.5, is_selected=True)
        self.new_layer(opacity=0.5)        
        self.new_layer(opacity=0.5)

        # TEMP
        self.CACHE = False

        if self.CACHE:
            self.cache_layers()

    @property
    def current_layer(self):
        return self.layers[self.active_layer_index]

    @current_layer.setter
    def current_layer(self, index):
        self.active_layer_index = index

    def get_ratio(self) -> float:
        return self.width / self.height
        
    def pixmap_to_mat(self, pixmap: QPixmap) -> cv2.Mat:
        image = pixmap.toImage()
        data = image.constBits()
        arr = np.array(data).reshape(image.width(), image.height(), 4)
        arr = cv2.cvtColor(arr, cv2.COLOR_RGBA2BGR)
        return cv2.Mat(arr)

    def mat_to_pixmap(self, mat: cv2.Mat) -> QPixmap:
        height, width, channel = mat.shape
        bytesPerLine = channel * width
        qImg = QImage(mat.data, width, height, bytesPerLine, QImage.Format_RGBA8888)
        return QPixmap.fromImage(qImg)

    def initialize(self):
        self.layers.append(self.draw_checkerboard())

    def new_layer(self, **kwargs):
        image = np.zeros((self.height,self.width,self.channels), np.uint8)
        image.fill(255)
        image[:, :, 1] = 0

        image = self.add_circle_mask(image)

        layer = Layer(
                image=image,
                **kwargs
                # show=False
            )

        self.layers.append(layer)

    def add_circle_mask(self, img):
        # Get the dimensions of the image
        height, width = img.shape[:2]

        # Create a black mask with the same size as the image
        mask = np.zeros((height, width), dtype=np.uint8)

        # Draw a white circle in the center of the mask
        center = (int(width/3), int(height/3))
        radius = int(min(height, width)/4)
        cv2.circle(mask, center, radius, (255, 255, 255), -1, lineType=cv2.LINE_AA)

        # Apply the mask to the image
        result = cv2.bitwise_and(img, img, mask=mask)

        return result

    def move_image(self, image, x_offset, y_offset):
        h, w = image.shape[:2]

        M = np.float32([
            [1, 0, x_offset],
            [0, 1, y_offset]
        ])

        return cv2.warpAffine(image, M, (w, h))

    def cache_layers(self):
        composite = np.zeros((self.height,self.width,self.channels), np.uint8)
        cnt = 0

        print('CACHE')

        x = [[-20, -40], [0, 0], [20, 40], [40, 80], [60, 120], [80, 160]]

        # TODO: Track alpha too
        # Do I need to add some kind of alpha channel to the Layer class?

        for index, layer in enumerate(self.layers[:self.active_layer_index]):
            if layer.show:
                image = np.copy(layer.image)
                image[:, :, 3] = image[:, :, 3] * layer.opacity
                if index == self.active_layer_index:
                    layer.image = self.move_image(layer.image, *x[cnt])
                composite = get_mode(layer.mode)(image, composite)
            # print(x[cnt])
            cnt += 1
        self.cache[0] = np.copy(composite)
        composite.fill(0)
        # cnt += 1

        for index, layer in enumerate(self.layers[self.active_layer_index + 1:]):
            if layer.show:
                image = np.copy(layer.image)
                image[:, :, 3] = image[:, :, 3] * layer.opacity
                if index == self.active_layer_index:
                    layer.image = self.move_image(layer.image, *x[cnt])
                composite = get_mode(layer.mode)(layer.image, composite)
                # print(x[cnt])
                cnt += 1
        self.cache[1] = np.copy(composite)

    def draw_checkerboard(self):
        image = np.zeros((self.height, self.width, self.channels), np.uint8)
        image.fill(255)

        color_1 = (255, 255, 255, 255)
        color_2 = (248, 248, 248, 255)

        for i in range(self.width // (self.grid_size // 2)):
            for j in range(self.height // (self.grid_size // 2)):
                color =  color_1 if (i + j) % 2 != 0 else color_2
                image = cv2.rectangle(
                    image,
                    ((i - 1) * self.grid_size, (j - 1) * self.grid_size, i * self.width, j * self.height),
                    color,
                    -1
                )

        return Layer(
            image=image,
            name='Checkerboard'
        )

    def composite_layers(self) -> cv2.Mat:
        composite = np.zeros((self.height,self.width,self.channels), np.uint8)
        # composite.fill(255)
        out = [[-20, -40], [0, 0], [20, 40], [40, 80], [60, 120], [80, 160], [100, 180]]

        if not self.CACHE:
            for index, layer in enumerate(self.layers):
                if layer.show:
                    image = np.copy(layer.image)
                    image[:, :, 3] = image[:, :, 3] * layer.opacity
                    # out.append([(index - 1) * 20, (index - 1) * 40])
                    if layer.name != 'Checkerboard':
                        if index == self.active_layer_index:
                            layer.image = self.move_image(layer.image, *out[index])

                    composite = get_mode(layer.mode)(image, composite)
                    # print(index, layer.name, layer.opacity, layer.mode)
        else:
            # image = np.copy(layer.image)
            layer = self.layers[self.active_layer_index]
            layer.image[:, :, 3] = layer.image[:, :, 3] * layer.opacity
            # layer.image = self.move_image(layer.image, *[20, 40])
            # composite = get _mode()(self.cache[1], self.cache[0])

            composite = get_mode()(composite, self.cache[0])
            composite = get_mode()(layer.image, self.cache[1])

        return composite

    def render(self) -> QPixmap:
        
        return self.mat_to_pixmap(self.composite_layers())


@dataclass
class Layer:
    __slots__ = [
        'index',
        'layer_id',
        'color',
        'name',
        'alpha_lock',
        'lock',
        'show',
        'image',
        'masks',
        'position',
        'scale',
        'mode',
        'mode_percent',
        'parent',
        'effects',
        'opacity',
        'is_selected',
    ]

    def __init__(
            self,
            layer_id=None,
            index=0,
            color=None,
            name=None,
            alpha_lock=False,
            lock=False,
            show=True,
            image=None,
            masks=[],
            position=[0.0, 0.0], # QPoint
            scale=[1.0, 1.0], # qreal? Double I think.
            mode='Normal',
            mode_percent=1.0,
            parent=None,
            effects=[],
            opacity=1.0,
            is_selected=False,
        ):
        global id
        self.index = index
        if layer_id is None:
            self.layer_id = id
            id += 1
        else:
            self.layer_id = layer_id

        self.color = color

        if name:
            self.name = name
        else:
            self.name = f'Layer {self.layer_id}'

        self.alpha_lock = alpha_lock
        self.lock = lock
        self.show = show
        self.image = image
        self.masks = masks
        self.position = position
        self.scale = scale
        self.mode = mode
        self.mode_percent = mode_percent
        self.parent = parent
        self.effects = effects
        self.opacity = opacity
        self.is_selected = is_selected


@dataclass
class LayerGroup(Layer):
    __slots__ = [
        'children',
        'is_open'
    ]

    def __init__(
            self,
            children: List=[],
            is_open: bool=False,
            *args,
            **kwargs
        ):
        super().__init__(self, *args, **kwargs)
        self.children = children
        self.is_open = is_open


def modes():
    return [
        'Normal',
        'Dissolve', # 2 Added
        # "DestinationOver",
        # "Clear",
        # "Source",
        # "Destination",
        # "SourceIn",
        # "DestinationIn",
        # "SourceOut",
        # "DestinationOut",
        # "SourceAtop",
        # "DestinationAtop",
        "Darken",
        "Multiply",
        "Color Burn",
        "Linear Burn", # Added
        "Darker Color", # 8 Added

        "Lighten",
        "Screen",
        "Color Dodge",
        "Linear Dodge (Add)",
        "Lighter Color", # 14

        "Overlay",
        "Soft Light",
        "Hard Light",
        "Vivid Light", # 19 Added

        "Difference",
        "Exclusion",
        "Subtract", # Added
        "Divide", # 24 Added

        'Hue', # Added
        'Saturation', # Added
        'Color', # Added
        'Luminosity', # 29 Added
        "Xor",
        "Plus",
    ]


def mode_mappings(mode):
    switch = {
        'Normal': QPainter.CompositionMode.CompositionMode_SourceOver,
        "DestinationOver": QPainter.CompositionMode.CompositionMode_DestinationOver,
        "Clear": QPainter.CompositionMode.CompositionMode_Clear,
        "Source": QPainter.CompositionMode.CompositionMode_Source,
        "Destination": QPainter.CompositionMode.CompositionMode_Destination,
        "SourceIn": QPainter.CompositionMode.CompositionMode_SourceIn,
        "DestinationIn": QPainter.CompositionMode.CompositionMode_DestinationIn,
        "SourceOut": QPainter.CompositionMode.CompositionMode_SourceOut,
        "DestinationOut": QPainter.CompositionMode.CompositionMode_DestinationOut,
        "SourceAtop": QPainter.CompositionMode.CompositionMode_SourceAtop,
        "DestinationAtop": QPainter.CompositionMode.CompositionMode_DestinationAtop,
        "Xor": QPainter.CompositionMode.CompositionMode_Xor,
        "Plus": QPainter.CompositionMode.CompositionMode_Plus,
        "Multiply": QPainter.CompositionMode.CompositionMode_Multiply,
        "Screen": QPainter.CompositionMode.CompositionMode_Screen,
        "Overlay": QPainter.CompositionMode.CompositionMode_Overlay,
        "Darken": QPainter.CompositionMode.CompositionMode_Darken,
        "Lighten": QPainter.CompositionMode.CompositionMode_Lighten,
        "Color Dodge": QPainter.CompositionMode.CompositionMode_ColorDodge,
        "Color Burn": QPainter.CompositionMode.CompositionMode_ColorBurn,
        "Hard Light": QPainter.CompositionMode.CompositionMode_HardLight,
        "Soft Light": QPainter.CompositionMode.CompositionMode_SoftLight,
        "Difference": QPainter.CompositionMode.CompositionMode_Difference,
        "Exclusion": QPainter.CompositionMode.CompositionMode_Exclusion,
    }
    return switch[mode] if mode in switch else switch['Normal']


# while(1):
#     k = cv2.waitKey(1) & 0xFF
#     # cv2.imshow('image',img)

#     # cv.curve = cv.curve(curvePoints, true)
#     if not MOUSE_QUEUE.empty():
#         # [x, y] = [int(x) for x in q.get()]
#         # pts = np.array(MOUSE_QUEUE.get(), np.int32)
#         print(MOUSE_QUEUE.get())