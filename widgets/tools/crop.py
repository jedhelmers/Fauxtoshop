from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import cropui


class CropOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = cropui.Ui_CropOptions()
        self.ui.setupUi(self)
