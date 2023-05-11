from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QSize, QPoint
from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QDockWidget, QFrame, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtGui import QIcon

from styles.window_panel import window_panel_style
from ui.windows import layerswindowui
from widgets.windows.layer import LayerWidget
from widgets.windows.layergroup import LayerGroupWidget


class LayersWindowWidget(QWidget):
    def __init__(self, signaler=None):
        super().__init__()
        self.ui = layerswindowui.Ui_LayersWindow()
        self.ui.setupUi(self)

        layer = LayerWidget(layer={'is_selected': False, 'hidden': True})
        layer2 = LayerWidget(layer={'is_selected': True, 'hidden': False})
        group = LayerGroupWidget(layer={'is_selected': False, 'hidden': True})
        # v = QVBoxLayout()
        self.ui.verticalLayout_3.insertWidget(0, layer)
        self.ui.verticalLayout_3.insertWidget(0, layer2)
        self.ui.verticalLayout_3.insertWidget(0, group)
        # print(len(self.ui.verticalLayout_3.children()))

