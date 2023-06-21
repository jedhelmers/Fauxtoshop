from dataclasses import dataclass
from typing import List

import numpy as np
import cv2
from PySide6.QtGui import QPainter, QPixmap, QImage

from modes import get_mode

id = 0
parent_id = 0

class Layer:
    pass

@dataclass
class ArtBoard:
    def __init__(self):
        self.width = 600
        self.height = 600
        self.channels = 4
        self.layers: list[Layer] = []
        self.background: Layer = None

        self.initialize()
        self.layers.append(
            self.new_layer()
        )
        self.layers.append(
            self.new_layer()
        )
        self.layers.append(
            self.new_layer()
        )
        
    def pixmap_to_mat(self, pixmap: QPixmap) -> cv2.Mat:
        image = pixmap.toImage()
        data = image.constBits()
        arr = np.array(data).reshape(image.height(), image.width(), 4)
        arr = cv2.cvtColor(arr, cv2.COLOR_RGBA2BGR)
        return cv2.Mat(arr)

    def mat_to_pixmap(self, mat: cv2.Mat) -> QPixmap:
        height, width, channel = mat.shape
        bytesPerLine = channel * width
        qImg = QImage(mat.data, width, height, bytesPerLine, QImage.Format_RGBA8888)
        return QPixmap.fromImage(qImg)

    def initialize(self):
        background = np.zeros((self.width,self.height,self.channels), np.uint8)
        background.fill(255)

        self.background = Layer(
            name='Background',
            image=background
        )

    def new_layer(self):
        image = np.zeros((self.width,self.height,self.channels), np.uint8)
        image.fill(255)
        image[:, :, 1] = image[:, :, 1] = 0

        image = self.add_circle_mask(image)

        return Layer(
                image=image,
                opacity=0.7,
                # mode='Multiply'
            )

    def add_circle_mask(self, img):
        # Get the dimensions of the image
        height, width = img.shape[:2]

        # Create a black mask with the same size as the image
        mask = np.zeros((height, width), dtype=np.uint8)

        # Draw a white circle in the center of the mask
        center = (int(width/2), int(height/2))
        radius = int(min(height, width)/4)
        cv2.circle(mask, center, radius, (255, 255, 255), -1)

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

    def composite_layers(self) -> cv2.Mat:
        composite = self.background.image

        for index, layer in enumerate(self.layers):
            layer.image[:, :, 3] = layer.image[:, :, 3] * layer.opacity
            layer.image = self.move_image(layer.image, index * 30, index * 30)

            if index == 1:
                layer.mode = 'Subtract'

            composite = get_mode(layer.mode)(composite, layer.image)
            print(layer.name, layer.opacity, layer.mode)

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
