from PySide6.QtWidgets import QWidget

from ui import window_flyout_panelui


class WindowFlyoutPanelWidget(QWidget):
    def __init__(self, parent, name, windows, signaler=None):
        super().__init__(parent)
        self.ui = window_flyout_panelui.Ui_WindowPanel()
        self.ui.setupUi(self)

        self.ui.windowPanelTabWidget.setStyleSheet("""
        QTabBar::tab {
            padding: 4px 10px;
            min-width: 0px;
        }
        QTabWidget::tab-bar {
            left: 0;
            bottom: 0px;
            width: 190px;
        }
        """)

        if windows:
            for window in windows:
                widget = QWidget()
                self.ui.windowPanelTabWidget.addTab(widget, 'Howdy')

        self.setStyleSheet('background: rgba(255, 255, 255, 0.1)')
