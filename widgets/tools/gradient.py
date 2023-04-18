from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui.tools import gradientui


class GradientOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = gradientui.Ui_GradientOptions()
        self.ui.setupUi(self)
