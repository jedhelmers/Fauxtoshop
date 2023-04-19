from PySide6.QtWidgets import QWidget

from ui import window_flyout_panelui


class WindowFlyoutPanelWidget(QWidget):
    def __init__(self, parent, name, window, signaler=None):
        super().__init__(parent)
        self.ui = window_flyout_panelui.Ui_WindowPanel()
        self.ui.setupUi(self)

        self.current_window = window
        print(self.current_window)

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

        # print(self.current_window)
        if self.current_window and 'panel_contents' in self.current_window:
            for w in self.current_window['panel_contents']:
                print(w)
                widget = QWidget()
                self.ui.windowPanelTabWidget.addTab(widget, w['name'])

        self.setStyleSheet('background: rgba(255, 255, 255, 0.1)')
