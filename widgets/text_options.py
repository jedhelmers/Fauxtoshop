from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from ui import text_optionsui


class TextOptionsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = text_optionsui.Ui_TextOptions()
        self.ui.setupUi(self)
        self.parent = parent

        self.font = 'Helvetica'
        self.font_size = 12
        self.font_style = 'Regular'
        self.sharp = 'Sharp'

        self.alignment = 'alignLeft'

        self.ui.fontComboBox.setCurrentText(self.font)
        self.ui.fontSizeComboBox.setCurrentText(str(self.font_size))
        self.ui.fontStyleComboBox.setCurrentText(self.font_style)
        self.ui.fontSharpnessComboBox.setCurrentText(self.sharp)

        if self.alignment == 'alignLeft':
            self.ui.textAlignLeftPushButton.setStyleSheet('QPushButton {background-color: rgba(255, 255, 255, .25);}')


