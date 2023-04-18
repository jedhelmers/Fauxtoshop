from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import eyedropperui


class EyedropperOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = eyedropperui.Ui_EyedropperOptions()
        self.ui.setupUi(self)
