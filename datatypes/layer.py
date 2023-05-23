from dataclasses import dataclass
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QGraphicsItem, QGraphicsRectItem
from typing import List

id = 0
parent_id = 0

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


class LayerBase(QGraphicsRectItem):
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
        super().__init__(parent)
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
        self.setPos(10, 20)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)

    @property
    def is_selected(self):
        return self._is_selected

    @is_selected.setter
    def is_selected(self, is_selected):
        self._is_selected = is_selected

    # def itemChange(self, e):
    #     super().itemChange(e)
    #     print('WEE', e)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        print('WEEEEE', event)

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
