from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import stampui


class StampOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = stampui.Ui_StampOptions()
        self.ui.setupUi(self)
