from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import moveui


class MoveOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = moveui.Ui_MoveOptions()
        self.ui.setupUi(self)
