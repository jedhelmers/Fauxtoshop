from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import brush_arrowui


class BrushArrowOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = brush_arrowui.Ui_BrushArrowOptions()
        self.ui.setupUi(self)
