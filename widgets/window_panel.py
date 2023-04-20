from PySide6.QtWidgets import QWidget

from styles.window_panel import flyout_panel
from ui import window_flyout_panelui


class WindowPanelWidget(QWidget):
    def __init__(self, parent, signaler=None):
        super().__init__(parent)
        self.ui = window_flyout_panelui.Ui_WindowPanel()
        self.ui.setupUi(self)

        self.ui.windowPanelTabWidget.setStyleSheet(flyout_panel())
       
        for i in range(4):
            widget = QWidget()
            self.ui.windowPanelTabWidget.addTab(widget, str(i))

        self.setStyleSheet('background: rgba(255, 255, 255, 0.1)')

