from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import eraserui


class EraserOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = eraserui.Ui_EraserOptions()
        self.ui.setupUi(self)
