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

    def __init__(
            self,
            index=0,
            color=None,
            name='Layer',
            alpha_lock=False,
            lock=False,
            show=True,
            image=None,
            mode='Normal',
            chidren=None,
            ):
        self.index = index
        self.color = color
        self.name = name
        self.alpha_lock = alpha_lock
        self.lock = lock
        self.show = show
        self.image = image
        self.mode = mode
        self.chidren = chidren

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
