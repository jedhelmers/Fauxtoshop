from dataclasses import dataclass
from typing import List

import numpy as np
import cv2
from PySide6.QtGui import QPainter, QPixmap, QImage


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

        self.initialize()
        self.layers.append(
            self.new_layer()
        )
        # self.add_layer()

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

        self.layers.append(
            Layer(
                name='Background',
                image=background
            )
        )

    def new_layer(self):
        image = np.zeros((self.width,self.height,self.channels), np.uint8)
        image.fill(255)
        image[:, :, 1] = image[:, :, 1] = 0
        image[:, :, 3] = 0.25 * 255

        height, width, channel = image.shape

        # image = cv2.circle(image, [height // 2, width // 2], 100, [255, 255, 255], -1)

        image = self.add_circle_mask(image)

        return Layer(
                image=image,
                opacity=0.25
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

    def get_alpha_channel(self, img):
        # Split the image into color and alpha channels
        _, _, _, alpha = cv2.split(img)

        # Return the alpha channel as a grayscale image
        return alpha

    def add_layers(self, front: Layer, background: cv2. Mat) -> cv2.Mat:
        result = cv2.addWeighted(
            front.image[..., :3],
            front.opacity,
            background[..., :3],
            0.5,
            0
        )

        try:
            alphas = front.image[..., 3] + background[..., 3]
            print('FRONT SHAPE', front.image[..., 3].shape)
            print('BACK SHAPE', background[..., 3].shape)
            # print(background[..., :3])
            result[..., 3] = np.where(
                alphas == 0,
                0,
                (
                    front.image[..., 3] * 255 + background[..., 3] * 255 - front.image[..., 3] * background[..., 3]
                ) / alphas
            )
        except Exception as e:
            print(e)

        return result

    def composite_images(self, img1, img2, alpha1, alpha2):
        # Normalize the alpha values
        norm_alpha1 = alpha1 / 255.0
        norm_alpha2 = alpha2 / 255.0

        # Combine the images with varying opacities
        result = cv2.addWeighted(img1, norm_alpha1, img2, norm_alpha2, 1)

        return result

    def composite_layers(self) -> cv2.Mat:
        composite = np.zeros((self.width,self.height,self.channels), np.uint8)
        composite.fill(255)
        composite[:, :, 3] = 255
        # composite[:, :, 1] = composite[:, :, 1] / 2
        # composite[:, :, 0] = 190
        # composite[:, :, 2] = 190
        # composite[:, :, 3] = 100
        for layer in self.layers:
            # layer.image[layer.image[:, :, 1:].all(axis=-1)] = 0
            # composite[composite[:, :, 1:].all(axis=-1)] = 0
            # composite = composite & layer.image

            # composite[:, :, 1] = composite[:, :, 1] * layer.opacity
            # composite[:, :, 0] = composite[:, :, 0] * layer.opacity
            # composite[:, :, 2] = composite[:, :, 2] * layer.opacity

            # layer.image[:, :, 1] = layer.image[:, :, 1] * layer.opacity
            # layer.image[:, :, 0] = layer.image[:, :, 0] * layer.opacity
            # layer.image[:, :, 2] = layer.image[:, :, 2] * layer.opacity

            # mask = self.get_alpha_channel(layer.image)
            # composite[:, :, 3] = ~mask

            # composite = cv2.addWeighted(
            #     composite,
            #     (1.0 - layer.opacity),
            #     layer.image,
            #     layer.opacity,
            #     0
            # )

            composite = np.bitwise_and(layer.image, composite)
            # composite = self.composite_images(layer.image, composite, layer.opacity * 255, 255 - (layer.opacity * 255))

            # composite = (composite * 1) + (layer.image * layer.opacity)
            # composite = self.add_layers(layer, composite)
            pass
        # composite = cv2.imread('images/example.png')
        # composite = cv2.cvtColor(composite, cv2.COLOR_RGBA2BGR)
        # return self.new_layer().image
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
