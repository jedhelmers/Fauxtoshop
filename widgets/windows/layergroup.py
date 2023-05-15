from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QSize, QPoint
from PySide6.QtWidgets import QWidget, QMainWindow, QDockWidget, QFrame, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtGui import QIcon, QPixmap

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
        self.is_open = False
        # print('self.is_open', layer)
        self.is_selected = layer['is_selected']
        self.show()

        self.ui.hidePushButton.clicked.connect(self.show)
        self.ui.openPushButton.clicked.connect(self.open)

    def open(self):
        self.is_open = not self.is_open
        icon = QIcon()
        # icon_folder = QPixmap()
        
        if self.is_open:
            icon.addFile(u":images/images/window_open.svg", QSize(12, 12), QIcon.Normal, QIcon.Off)
            self.ui.folderLabel.setPixmap(QPixmap(u":images/images/window_group_closed.svg"))
        else:
            icon.addFile(u":images/images/window_close.svg", QSize(12, 12), QIcon.Normal, QIcon.Off)
            self.ui.folderLabel.setPixmap(QPixmap(u":images/images/window_group_open.svg"))

        self.ui.openPushButton.setIcon(icon)

    def show(self):
        self.hidden = not self.hidden
        icon = QIcon()

        if self.hidden:
            icon.addFile(u":/images/images/window_hide.svg", QSize(), QIcon.Normal, QIcon.Off)
        else:
            icon.addFile(u":/images/images/window_show.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.hidePushButton.setIcon(icon)