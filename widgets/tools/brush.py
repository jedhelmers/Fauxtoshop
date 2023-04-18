from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import brushui


class BrushOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = brushui.Ui_BrushOptions()
        self.ui.setupUi(self)
