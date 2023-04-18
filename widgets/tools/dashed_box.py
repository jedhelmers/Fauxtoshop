from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import dashed_boxui


class DashedBoxOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = dashed_boxui.Ui_DashedBoxOptions()
        self.ui.setupUi(self)
