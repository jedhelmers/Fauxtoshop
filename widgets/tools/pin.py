from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import pinui


class PinOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = pinui.Ui_PinOptions()
        self.ui.setupUi(self)
