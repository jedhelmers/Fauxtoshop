from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import penui


class PenOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = penui.Ui_PenOptions()
        self.ui.setupUi(self)
