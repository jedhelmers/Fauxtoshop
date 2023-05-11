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
            signaler=None
        ):
        super().__init__()
        self.ui = layerui.Ui_LayerWidget()
        self.ui.setupUi(self)

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
        self.show()
        self.selected()

        self.ui.hidePushButton.clicked.connect(self.show)

    def selected(self):
        # if self.is_selected:
        #     self.setStyleSheet("""
        #     QWidget[objectName=LayerWidget] {
        #         border: 1px solid rgba(0, 0, 0, .5);
        #         border-top: none;
        #         background: rgba(255, 255, 255, .1)
        #     }
        #     """)
        # else:
        #     self.setStyleSheet("""
        #     QWidget[objectName=LayerWidget] {
        #         border: 1px solid rgba(0, 0, 0, .5);
        #         border-top: none;
        #         background: rgba(255, 255, 255, .02)
        #     }
        #     """)
        pass

    def show(self):
        self.hidden = not self.hidden
        icon = QIcon()

        if self.hidden:
            icon.addFile(u":/images/images/window_hide.svg", QSize(), QIcon.Normal, QIcon.Off)
        else:
            icon.addFile(u":/images/images/window_show.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.hidePushButton.setIcon(icon)
