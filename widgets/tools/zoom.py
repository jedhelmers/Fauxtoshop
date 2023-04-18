from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import zoomui


class ZoomOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = zoomui.Ui_ZoomOptions()
        self.ui.setupUi(self)
