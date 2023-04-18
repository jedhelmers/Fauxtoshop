from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import pointer_fingerui


class PointerFingerOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = pointer_fingerui.Ui_PointerFingerOptions()
        self.ui.setupUi(self)
