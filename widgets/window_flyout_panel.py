from PySide6.QtWidgets import QWidget

from ui import window_flyout_panelui


class WindowFlyoutPanelWidget(QWidget):
    def __init__(self, parent, name, signaler=None):
        super().__init__(parent)
        self.ui = window_flyout_panelui.Ui_WindowPanel()
        self.ui.setupUi(self)

        self.setStyleSheet('background: rgba(255, 255, 255, 0.1)')
