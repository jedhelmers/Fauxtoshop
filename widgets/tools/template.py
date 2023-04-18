from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import UI_NAME_LOWERui


class UI_NAMEOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = UI_NAME_LOWERui.Ui_UI_NAMEOptions()
        self.ui.setupUi(self)
