from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QSize, QPoint
from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QDockWidget, QFrame, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtGui import QIcon

from styles.window_panel import window_panel_style
from ui.windows import layerswindowui
from widgets.windows.layer import LayerWidget
from widgets.windows.layergroup import LayerGroupWidget


class LayersWindowWidget(QWidget):
    def __init__(
            self,
            layers,
            signaler=None
        ):
        super().__init__()
        self.ui = layerswindowui.Ui_LayersWindow()
        self.ui.setupUi(self)

        self.main_signaler = signaler
        self.layers = layers
        self.update_layers(layers)

        layer = LayerWidget(layer={'is_selected': False, 'hidden': True, 'name': 'Stuff'})
        layer2 = LayerWidget(layer={'is_selected': True, 'hidden': False, 'name': 'Stuff'})
        group = LayerGroupWidget(layer={'is_selected': False, 'hidden': True, 'name': 'Stuff'})
        # v = QVBoxLayout()
        self.ui.verticalLayout_3.insertWidget(0, layer)
        self.ui.verticalLayout_3.insertWidget(0, layer2)
        self.ui.verticalLayout_3.insertWidget(0, group)
        # print(len(self.ui.verticalLayout_3.children()))

    def update_layers(self, layers):
        self.layers = layers
        for l in self.layers:
            layer = LayerWidget(layer={'is_selected': False, 'hidden': False, 'name': l.name})
            self.ui.verticalLayout_3.insertWidget(0, layer)
