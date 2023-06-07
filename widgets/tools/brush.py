import re

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from datatypes.layer import Layer, modes, mode_mappings
from ui.tools import brushui


class BrushOptionsWidget(QWidget):
    def __init__(
            self,
            parent,
            tool
        ):
        super().__init__(parent)
        self.ui = brushui.Ui_BrushOptions()
        self.ui.setupUi(self)
        self.tool = tool

        self.ui.opacityComboBox.addItems([f'{i * 10.0}%' for i in range(1, 11)])
        self.ui.flowComboBox.addItems([f'{i * 10.0}%' for i in range(1, 11)])

        # Modes
        self.ui.modeComboBox.addItems(modes())
        self.ui.modeComboBox.insertSeparator(2)
        self.ui.modeComboBox.insertSeparator(8)
        self.ui.modeComboBox.insertSeparator(14)
        self.ui.modeComboBox.insertSeparator(19)
        self.ui.modeComboBox.insertSeparator(24)
        self.ui.modeComboBox.insertSeparator(29)

        self.ui.modeComboBox.currentTextChanged.connect(self.update_mode)
        self.ui.opacityComboBox.currentTextChanged.connect(self.update_opacity)
        self.ui.flowComboBox.currentTextChanged.connect(self.update_flow)

        self.ui.opacityComboBox.setCurrentText(f'{self.tool.opacity * 100}%')
        self.ui.flowComboBox.setCurrentText(f'{self.tool.opacity * 100}%')

    def keyPressEvent(self, event):
        if event.key() == 16777220: # Enter
            self.setFocus()

    def update_mode(self, mode):
        self.tool.mode = mode

    def update_opacity(self, opacity):
        self.tool.opacity = float(re.sub('\D', '', opacity)) / 100

    def update_flow(self, flow):
        self.tool.flow = float(re.sub('\D', '', flow)) / 100