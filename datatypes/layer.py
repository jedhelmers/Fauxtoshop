from dataclasses import dataclass
from PySide6.QtGui import QPainter


@dataclass
class Layer:
    __slots__ = [
        'index',
        'color',
        'name',
        'alpha_lock',
        'lock',
        'show',
        'image',
        'position',
        'scale',
        'mode',
        'mode_percent',
        'children',
    ]

    def __init__(
            self,
            index=0,
            color=None,
            name='Layer',
            alpha_lock=False,
            lock=False,
            show=True,
            image=None,
            position=[0.0, 0.0], # QPoint
            scale=[1.0, 1.0], # qreal? Double I think.
            mode='Normal',
            mode_percent=1.0,
            children=[],
            ):
        self.index = index
        self.color = color
        self.name = name
        self.alpha_lock = alpha_lock
        self.lock = lock
        self.show = show
        self.image = image
        self.position = position
        self.scale = scale
        self.mode = mode
        self.mode_percent = mode_percent
        self.children = children


@dataclass
class LayerGroup(Layer):
    __slots__ = ['is_collapsed']

    def __init__(self, is_collapsed: bool=False):
        super().__init__(self)
        self.is_collapsed = is_collapsed


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
        "ColorDodge": QPainter.CompositionMode.CompositionMode_ColorDodge,
        "ColorBurn": QPainter.CompositionMode.CompositionMode_ColorBurn,
        "HardLight": QPainter.CompositionMode.CompositionMode_HardLight,
        "SoftLight": QPainter.CompositionMode.CompositionMode_SoftLight,
        "Difference": QPainter.CompositionMode.CompositionMode_Difference,
        "Exclusion": QPainter.CompositionMode.CompositionMode_Exclusion,
    }
    return switch[mode] if mode in switch else switch['Normal']
