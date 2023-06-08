from PySide6.QtWidgets import QDialog

from styles.window_panel import window_panel_style
from ui.color_pickerui import Ui_ColorPicker


class ColorPickerWidget(QDialog):
    def __init__(self, parent, signaler=None):
        super().__init__(parent)
        self.ui = Ui_ColorPicker()
        self.ui.setupUi(self)
        