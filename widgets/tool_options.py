from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget, QFrame, QLabel, QPushButton
from PySide6.QtGui import QIcon

from ui.tools.baseui import Ui_BaseOptions
from widgets.tools.brush import BrushOptionsWidget
from widgets.new_file import NewFileWidget
from widgets.tools.text_options import TextOptionsWidget


class ToolOptionsWidget(QWidget):
    def __init__(self, main_signaler, tool):
        super().__init__()
        self.ui = Ui_BaseOptions()
        self.ui.setupUi(self)

        self.ui.gridLayout.addWidget(BrushOptionsWidget(self))
