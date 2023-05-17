import json
import os
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QFrame, QLabel, QGraphicsBlurEffect

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtOpenGL import *

from datatypes.layer import Layer, LayerGroup, mode_mappings
from tool import Tool
from tool import ToolBase
from typing import List
from ui import workspaceui
from utils import load_settings, unit_conversion, pixel_to_inch, inch_to_pixel
from widgets.artboard import ArtBoardWidget
from widgets.window_panel import WindowPanelWidget
from widgets.windowbar import WindowsWidget


class WorkspaceWidget(QWidget):
    def __init__(
            self,
            parent,
            new_file_info,
            signaler
        ):
        super().__init__(parent)
        self.ui = workspaceui.Ui_Workspace()
        self.ui.setupUi(self)
        self.setMouseTracking(True)