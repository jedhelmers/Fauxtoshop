from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import spot_headlingui


class SpotHeadlingOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = spot_headlingui.Ui_SpotHeadlingOptions()
        self.ui.setupUi(self)
