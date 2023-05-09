from dataclasses import dataclass
from typing import List
from typing import Tuple


@dataclass
class ToolIcon():
    __slots__ = [
        'name',
        'path',
        'hotPoints',
        'size'
    ]

    def __init__(
            self,
            name: str="pointer",
            path: str="",
            hotPoints: List=[-1, -1],
            size: List=[28, 28]
    ):
        self.name = name
        self.path = path
        self.hotPoints = hotPoints
        self.size = size

def get_tool_icon(icon: str):
    switch = {
        'default': ToolIcon(path="images/broom.svg"),
        'brush': ToolIcon(path="images/toolbar_brush.svg"),
        'move': ToolIcon(path="images/toolbar_move.svg"),
        'pen': ToolIcon(path="images/cursor_icon_pen.svg"),
        'pen_start_path': ToolIcon(path="images/cursor_icon_pen_start_path.svg"),
        'pen_extend_path': ToolIcon(path="images/cursor_icon_pen_extend_path.svg"),
        'pen_close_path': ToolIcon(path="images/cursor_icon_pen_close_path.svg"),
        'pen_add_point': ToolIcon(path="images/cursor_icon_pen_add_point.svg"),
        'pen_remove_point': ToolIcon(path="images/cursor_icon_pen_remove_point.svg"),
    }
    return switch[icon] if icon in switch else switch['default']