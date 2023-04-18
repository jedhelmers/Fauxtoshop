from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import quick_selectionui


class QuickSelectionOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = quick_selectionui.Ui_QuickSelectionOptions()
        self.ui.setupUi(self)
