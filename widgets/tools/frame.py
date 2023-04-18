from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import frameui


class FrameOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = frameui.Ui_FrameOptions()
        self.ui.setupUi(self)
