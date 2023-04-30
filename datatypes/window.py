from dataclasses import dataclass


@dataclass
class Window:
    __slots__ = [
        'tooltip',
        'name',
        'path',
        'widget',
    ]

    def __init__(
            self,
            tooltip,
            name,
            path,
            widget=None,
        ):
        self.tooltip = tooltip
        self.name = name
        self.path = path
        self.widget = widget
