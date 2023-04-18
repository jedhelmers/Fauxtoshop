from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import textui


class TextOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = textui.Ui_TextOptions()
        self.ui.setupUi(self)
