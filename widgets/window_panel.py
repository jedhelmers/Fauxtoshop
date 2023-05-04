from PySide6.QtWidgets import QWidget

from styles.window_panel import flyout_panel
from ui import window_flyout_panelui
from widgets.windows.layers import LayersWindowWidget


class WindowPanelWidget(QWidget):
    def __init__(self, parent, windows, signaler=None):
        super().__init__(parent)
        self.ui = window_flyout_panelui.Ui_WindowPanel()
        self.ui.setupUi(self)

        self.windows = windows
        self.ui.windowPanelTabWidget.setStyleSheet(flyout_panel())
        self.setMaximumWidth(240)

        self.current_window = 'Layers'

        # for i in range(4):
        #     widget = QWidget()
        # for window in self.windows:
        #     layers = LayersWindowWidget()
        #     # print(window)
        #     self.ui.windowPanelTabWidget.addTab(layers, 'Name')

        self.setStyleSheet('background: rgba(255, 255, 255, 0.1)')

    def render_window_tabs(self):
        # for window in self.windows:
    #     self.move(100, 100)

    # def set_position(self, stuff):
    #     # [x, y] = stuff
    #     self.move(stuff.width(), stuff.height())
    #     print(stuff.width(), stuff.height())
        pass