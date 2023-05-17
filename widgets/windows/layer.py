from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QSize, QPoint
from PySide6.QtWidgets import QWidget, QMainWindow, QDockWidget, QFrame, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtGui import QIcon

# from styles.window_panel import window_panel_style
from ui.windows import layerui


class LayerWidget(QWidget):
    def __init__(
            self,
            layer,
            parent=None,
            main_signaler=None,
            layer_signaler=None
        ):
        super().__init__()
        self.ui = layerui.Ui_LayerWidget()
        self.ui.setupUi(self)
        self.objectName = layer['name']
        self.main_signaler = main_signaler
        self.layer_signaler = layer_signaler

        if parent:
            self.setParent(parent)

        self.setStyleSheet("""
            QWidget[objectName*=thumbnailWidget] {
                border: 1px solid rgba(0, 0, 0, .5);
            }
            QWidget {
                border: 1px solid rgba(0, 0, 0, .5);
                border-top: none;
                background: rgba(255, 255, 255, .02)
            }
            QLabel {
                background: transparent;
                border: none;
            }
            QPushButton {
                background: transparent;
                border: none;
            }
        """)

        self.hidden = layer['hidden']
        self.is_selected = layer['is_selected']
        self.render()

        self.ui.hidePushButton.clicked.connect(self.show)
        self.ui.layerNameLabel.setText(layer['name'])

    def mousePressEvent(self, event):
        self.main_signaler.set_current_layer.emit(self.objectName)
        self.layer_signaler.update_selected_layer.emit()

    def set_current_layer(self):
        self.main_signaler.set_current_layer.emit()

    def selected(self, is_selected=False):
        # TODO: Update list onClick, and NOT on addNewLayer
        if is_selected:
            self.setStyleSheet("background: rgba(255, 255, 255, .1);")
            # self.setStyleSheet("""
            # QWidget[objectName=LayerWidget] {
            #     border: 1px solid rgba(0, 0, 0, .5);
            #     border-top: none;
            #     background: rgba(255, 255, 255, 255)
            # }
            # """)
        else:
            # self.setStyleSheet("""
            # QWidget[objectName=LayerWidget] {
            #     border: 1px solid rgba(0, 0, 0, .5);
            #     border-top: none;
            #     background: rgba(255, 255, 255, .02)
            # }
            # """)
            self.setStyleSheet("background: rgba(255, 255, 255, .02);")

    def render(self):
        icon = QIcon()

        if self.hidden:
            icon.addFile(u":/images/images/window_hide.svg", QSize(), QIcon.Normal, QIcon.Off)
        else:
            icon.addFile(u":/images/images/window_show.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.hidePushButton.setIcon(icon)

    def show(self):
        self.hidden = not self.hidden
        self.render()

