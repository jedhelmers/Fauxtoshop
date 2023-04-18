from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import polygon_lassoui


class PolygonLassoOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = polygon_lassoui.Ui_PolygonLassoOptions()
        self.ui.setupUi(self)
