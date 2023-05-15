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
        # self.update_layers(layers)

        layer = LayerWidget(layer={'is_selected': False, 'hidden': True, 'name': 'Stuff'})
        layer2 = LayerWidget(layer={'is_selected': True, 'hidden': False, 'name': 'Stuff'})
        group = LayerGroupWidget(layer={'is_selected': False, 'hidden': True, 'name': 'Stuff'})
        # v = QVBoxLayout()
        self.ui.verticalLayout_3.insertWidget(0, layer)
        self.ui.verticalLayout_3.insertWidget(0, layer2)
        self.ui.verticalLayout_3.insertWidget(0, group)
        # print(len(self.ui.verticalLayout_3.children()))

        self.ui.newLayerPushButton.clicked.connect(self.test)

        self.setStyleSheet("""
            QComboBox {
                background: rgba(0, 0, 0, .2);
            }

    QScrollBar:vertical
    {

        background-color: pink;
        width: 15px;
        margin: 15px 3px 15px 3px;
        border: 1px transparent #2A2929;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical
    {
        background-color: rgba(255, 255, 255, .5);
        min-height: 5px;
        border-radius: 2px;
    }

    QScrollBar::sub-line:vertical
    {
        border-radius: 2px;
        border-image: url(:/qss_icons/rc/up_arrow_disabled.png);
        height: 10px;
        width: 10px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }

    QScrollBar::add-line:vertical
    {
        margin: 3px 0px 3px 0px;
        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);
        height: 10px;
        width: 10px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }

    QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on
    {
        border-image: url(:/qss_icons/rc/up_arrow.png);
        height: 10px;
        width: 10px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }

    QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on
    {
        border-image: url(:/qss_icons/rc/down_arrow.png);
        height: 10px;
        width: 10px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
        background-color: pink;
    }

    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
    {
        background: rgba(255, 255, 255, .2);
        border-radius: 2px;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
    {
        background: none;
    }

        """)

    def test(self):
        self.ui.verticalLayout_3.insertWidget(0, LayerWidget(layer={'is_selected': False, 'hidden': True, 'name': 'Test'}))

    def update_layers(self, layers=None):
        self.layers = layers
        # layer = LayerWidget(layer={'is_selected': False, 'hidden': False, 'name': "l.name"})
        self.ui.verticalLayout_3.insertWidget(0, LayerWidget(layer={'is_selected': False, 'hidden': False, 'name': "l.name"}))
        for l in self.layers:
            # layer = LayerWidget(layer={'is_selected': False, 'hidden': False, 'name': l.name})
            self.ui.verticalLayout_3.insertWidget(0, LayerWidget(layer={'is_selected': False, 'hidden': False, 'name': l.name}))
            print(l.name)
