from dataclasses import dataclass
from PySide6.QtGui import QImage, QPainter

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
        'mode',
        'chidren',
    ]

    def __init__(self):
        self.index: int = 0
        self.color: str = None
        self.name: str = 'Layer'
        self.alpha_lock: bool = False
        self.lock: bool = False
        self.show: bool = True
        self.image: QImage
        self.mode: str = 'Normal'
        self.chidren: list = []

def mode_mappings(mode):
    switch = {
        'Normal': QPainter.CompositionMode.CompositionMode_SourceOver,
        'Multiply': QPainter.CompositionMode.CompositionMode_Multiply,
        'Difference': QPainter.CompositionMode.CompositionMode_Difference,
        'Darken': QPainter.CompositionMode.CompositionMode_Darken,
        'Lighten': QPainter.CompositionMode.CompositionMode_Lighten,
        'Overlay': QPainter.CompositionMode.CompositionMode_Overlay,
        'Difference': QPainter.CompositionMode.CompositionMode_Difference,
        # '': QPainter.CompositionMode.CompositionMode_,
    }
    return switch[mode] if mode else switch['Normal']
