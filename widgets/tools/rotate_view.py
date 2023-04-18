from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import rotate_viewui


class RotateViewOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = rotate_viewui.Ui_RotateViewOptions()
        self.ui.setupUi(self)
