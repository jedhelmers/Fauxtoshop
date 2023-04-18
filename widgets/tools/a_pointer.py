from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import a_pointerui


class APointerOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = a_pointerui.Ui_APointerOptions()
        self.ui.setupUi(self)
