import json
import random
import sys
from pathlib import Path
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, Qt, QEvent, QPoint, QObject, QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QPushButton, QWidget, QGridLayout

from datas.misc import get_window_controls
from functions import new_file
from styles.main import main_style
from tool import ToolBase
from ui import mainwindowui
from widgets.new_file import NewFileWidget
import widgets.tools as Tools
from widgets.tools.text_options import TextOptionsWidget
from widgets.toolbar import ToolbarWidget
from widgets.windowbar import WindowsWidget
from widgets.window_panel import WindowPanelWidget
from widgets.workspace import WorkspaceWidget
from widgets.windows.layers import LayersWindowWidget


def command_mappings(key):
    # 16777249
    switch = {
        Qt.Key_I: 'big'
    }
    return switch[key] if key in switch else None

def shift_mappings(key):
    # 16777248
    switch = {
        Qt.Key_I: 'butts',
    }
    return switch[key] if key in switch else None

def key_mappings(key):
    switch = {
        # TOOLS
        '73': 'eyedropper',
        '86': 'move',
        '77': 'dashed_box',
        '76': 'polygon_lasso',
        '65': 'a_pointer',
        '85': 'rectangle',
        '66': 'brush',
        '67': 'crop',
        '0': 'eraser',
        '0': 'frame',
        '0': 'gradient',
        '0': 'pointer_finger',
        '0': 'pin',
        '80': 'pen',
        '0': 'quick_selection',
        '0': 'spot_headling',
        'S': 'stamp',
        '84': 'text',
        '0': 'rotate_view',
        '73_16777248_16777249': 'zoom',
        # MAIN FUNCTIONS
        '78_16777249': 'NEW_FILE',
        # WORKSPACE
        '82_16777249': 'HIDE_RULERS',
        '78_16777248_16777249': 'NEW_LAYER',
        '73_16777249': 'INVERT_IMAGE',
        '61_16777249': 'ZOOM_IN',
        '45_16777249': 'ZOOM_OUT',
        '67_16777249': 'COPY',
        '86_16777249': 'PASTE',
        '88_16777249': 'CUT',
        '90_16777249': 'UNDO',
        '90_16777248_16777249': 'REDO',
    }
    return switch[key] if key in switch else None

def tooloptions_mappings(tool_name):
    switch = {
        'text': Tools.TextOptionsWidget,
        'eyedropper': Tools.EyedropperOptionsWidget,
        'move': Tools.MoveOptionsWidget,
        'dashed_box': Tools.DashedBoxOptionsWidget,
        'polygon_lasso': Tools.PolygonLassoOptionsWidget,
        'a_pointer': Tools.APointerOptionsWidget,
        'rectangle': Tools.RectangleOptionsWidget,
        'brush': Tools.BrushArrowOptionsWidget,
        'crop': Tools.CropOptionsWidget,
        'eraser': Tools.EraserOptionsWidget,
        'frame': Tools.FrameOptionsWidget,
        'gradient': Tools.GradientOptionsWidget,
        'pointer_finger': Tools.PointerFingerOptionsWidget,
        'pin': Tools.PinOptionsWidget,
        'pen': Tools.PenOptionsWidget,
        'quick_selection': Tools.QuickSelectionOptionsWidget,
        'spot_headling': Tools.SpotHeadlingOptionsWidget,
        'stamp': Tools.StampOptionsWidget,
        'rotate_view': Tools.RotateViewOptionsWidget,
    }
    return switch[tool_name] if tool_name in switch else None


class MainSignaler(QtCore.QObject):
    select_tool = QtCore.Signal(str)
    show_window_panel = QtCore.Signal(dict)
    select_window = QtCore.Signal(str)
    layer_manager = QtCore.Signal(list)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainwindowui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.signaler = MainSignaler()

        self.setMouseTracking(True)
        self.setStyleSheet(main_style())

        self._current_tool = 'brush'
        self.keylist = []
        self.window_controls = get_window_controls()
        self.current_window = None
        self.current_options_widget = None
        self.tab_index = 0
        self.tabs = []
        self.current_tab = None
        self.layers = []

        toolbar = ToolbarWidget(signaler=self.signaler)
        self.ui.toolbarWidget.layout().addWidget(toolbar)

        windows = WindowsWidget(signaler=self.signaler)
        self.ui.windowsWidget.layout().addWidget(windows)

        self.signaler.select_tool.connect(self.select_tool)
        self.signaler.show_window_panel.connect(self.show_window_panel)
        self.signaler.select_window.connect(self.select_window)
        self.signaler.layer_manager.connect(self.layer_manager)

        self.setup_window_controls()

        self.WindowPanelWidget = WindowPanelWidget(
            parent=self,
            signaler=self.signaler,
            windows=self.window_controls,
            layers=self.layers)
        self.WindowPanelWidget.hide()
        self.current_tool = 'brush'
        # self.current_window = 'Layers'

        # self.icon = QIcon("images/toolbar_brush.svg").pixmap(QSize(52, 52))
        # self.cursor = QtGui.QCursor(self.icon, 0, 0)

        # self.setCursor(self.cursor)

    @property
    def current_tool(self):
        return self._current_tool

    @current_tool.setter
    def current_tool(self, tool):
        """
        Set tool and remove button style from previously selected tool.
        """
        old_button = self.findChild(QPushButton, self.current_tool)
        button = self.findChild(QPushButton, tool)

        if old_button is not None:
            old_button.setStyleSheet('QPushButton {background-color: transparent;}')

        if button is not None:
            button.setStyleSheet('QPushButton {background-color: rgba(255, 255, 255, .25);}')

        self._current_tool = tool
        # self.tool.current_tool = tool
        if self.current_tab:
            self.current_tab.current_tool = tool
        self.setup_tool_options_bar()

    def test(self):
        workspace = self.ui.workspaceTabWidget.currentWidget()

        if workspace:
            print('WORKSPACE', workspace.get_layers())
            self.layer_manager(workspace.get_layers())

    def layer_manager(self, layers):
        self.layers = layers
        self.window_controls['Layers'].update_layers(self.layers)

    def setup_window_controls(self):
        self.window_controls['Layers'] = LayersWindowWidget(
            signaler=self.signaler,
            layers=self.layers
        )

    def resizeEvent(self, event):
        self.adjust_window_panel_pos(event.size() - event.oldSize())
        # self.WindowPanelWidget.set_position(event.size() - event.oldSize())

    def render_layers_panel(self, layers):
        print(layers)

    def select_window(self, window):
        print(window)
        if window['name'] == 'Layers':
            self.render_layers_panel(None)

    def adjust_window_panel_pos(self, e):
        x = self.WindowPanelWidget.x() + e.width()
        y = self.WindowPanelWidget.y()
        self.WindowPanelWidget.move(x, y)

    def show_window_panel(self, window=None):
        if window and (self.current_window is None or self.current_window['name'] != window['name']):
            self.current_window = window
            print(self.current_window)
            self.WindowPanelWidget.current_window = self.current_window
            self.WindowPanelWidget.show()
            x = window['pos'].x() - self.pos().x()
            y = window['pos'].y() - self.pos().y()
            flyout_width = self.WindowPanelWidget.width()
            self.WindowPanelWidget.move(x - flyout_width - 4, y - 30)
            self.select_window(window)
        else:
            self.WindowPanelWidget.hide()
            self.current_window = None

    def select_tool(self, tool_name):
        self.current_tool = tool_name

    def setup_tool_options_bar(self):
        if self.current_tool:
            mapped_tool = tooloptions_mappings(self.current_tool)

            if self.current_options_widget:
                self.ui.toolOptionsGridWidget.layout().removeWidget(self.current_options_widget)
                self.current_options_widget.setParent(None)

            if mapped_tool:
                self.current_options_widget = mapped_tool(self.ui.toolOptionsGridWidget)
                self.current_options_widget.setObjectName(f'{self.current_tool}_widget')
                self.ui.toolOptionsGridWidget.layout().addWidget(self.current_options_widget)

    def keyPressEvent(self, event):
        self.firstrelease = True
        astr = event.key()
        self.keylist.append(astr)
        self.test()

    def keyReleaseEvent(self, event):
        if self.firstrelease == True:
            self.processmultikeys(self.keylist)

        self.firstrelease = False

        try:
            del self.keylist[-1]
        except:
            pass

    def new_file(self, new_file_info):
        tab = WorkspaceWidget(
            self,
            new_file_info,
            signaler=self.signaler
        )
        self.current_tab = tab
        self.tabs.append(tab)

        self.ui.workspaceTabWidget.addTab(tab, "")
        self.ui.workspaceTabWidget.setTabText(
            self.ui.workspaceTabWidget.indexOf(tab),
            QCoreApplication.translate(
                "MainWindow",
                new_file_info['name'], None))

        self.tab_index = len(self.tabs)
        # print(self.tab_index)
        self.ui.workspaceTabWidget.setCurrentWidget(tab)

    def processmultikeys(self, keyspressed):
        _keyspressed = [*keyspressed]
        _keyspressed.sort()
        command = '_'.join([str(k) for k in _keyspressed])

        print(command)

        name = key_mappings(command)

        if name == 'NEW_FILE':
            new_file_widget = NewFileWidget(
                self,
                save=self.new_file,
            )
            new_file_widget.setModal(True)
            new_file_widget.show()
            self.keylist = []
        elif name == 'HIDE_RULERS':
            current_tab = self.ui.workspaceTabWidget.currentWidget()
            current_tab.toggle_rulers()
        else:
            self.on_toolbar_icon_click(name)
            self.keylist = []

    def on_toolbar_icon_click(self, name):
        self.current_tool = name


def main():
    app = QApplication(sys.argv)
    settings_window = MainWindow()
    settings_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()