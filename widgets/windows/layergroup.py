from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QSize, QPoint
from PySide6.QtWidgets import QWidget, QMainWindow, QDockWidget, QFrame, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtGui import QIcon

# from styles.window_panel import window_panel_style
from ui.windows import layergroupui


class LayerGroupWidget(QWidget):
    def __init__(
            self,
            layer,
            signaler=None
        ):
        super().__init__()
        self.ui = layergroupui.Ui_LayerWidget()
        self.ui.setupUi(self)

        self.setStyleSheet("""
            QWidget[objectName*=thumbnailWidget] {
                background-color: white;
                border: 1px solid rgba(0, 0, 0, .25);
            }
            QWidget {
                border: 1px solid rgba(0, 0, 0, .25);
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

        self.ui.hidePushButton.clicked.connect(self.show)

    def show(self):
        self.hidden = not self.hidden
        icon = QIcon()

        if self.hidden:
            icon.addFile(u":/images/images/window_hide.svg", QSize(), QIcon.Normal, QIcon.Off)
        else:
            icon.addFile(u":/images/images/window_show.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.hidePushButton.setIcon(icon)