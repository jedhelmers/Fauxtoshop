import json
import random
import sys
from pathlib import Path
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, Qt, QEvent, QPoint
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QPushButton, QWidget

from functions import new_file
from styles.main import main_style
from ui import mainwindowui
from widgets.new_file import NewFileWidget
from widgets.text_options import TextOptionsWidget
# from widgets.toolbar import ToolbarWidget

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
        'P': 'pen',
        '0': 'quick_selection',
        '0': 'spot_headling',
        'S': 'stamp',
        '84': 'text',
        '0': 'rotate_view',
        '73_16777248_16777249': 'zoom',
        '78_16777248_16777249': 'NEW_FILE'
    }
    return switch[key] if key in switch else None


# class MainSignaler(Qt.QObject):
#     pass

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainwindowui.Ui_MainWindow()
        self.ui.setupUi(self)
        # self.signaler = MainSignaler()

        self.setMouseTracking(True)
        self.setStyleSheet(main_style())

        self._current_tool = 'text'
        self.keylist = []

        self.render()
        self.current_tool = 'text'

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

        button.setStyleSheet('QPushButton {background-color: rgba(255, 255, 255, .25);}')

        self._current_tool = tool
        self.setup_tool_options_bar() 

    def setup_tool_options_bar(self):
        if self.current_tool == 'text':
            text_options_widget = TextOptionsWidget(self.ui.toolOptionsGridWidget)
            text_options_widget.setObjectName('text_options_widget')
            self.ui.toolOptionsGridWidget.layout().addWidget(text_options_widget)
        else:
            child = self.ui.toolOptionsGridWidget.findChild(QWidget, 'text_options_widget')

            if child is not None:
                self.ui.toolOptionsWidget.layout().removeWidget(child)
                child.setParent(None)

        print(self.current_tool)

    def keyPressEvent(self, event):
        self.firstrelease = True
        astr = event.key()
        self.keylist.append(astr)
        
    def keyReleaseEvent(self, event):
        if self.firstrelease == True: 
            self.processmultikeys(self.keylist)

        self.firstrelease = False

        try:
            del self.keylist[-1]
        except:
            pass

    def processmultikeys(self, keyspressed):
        _keyspressed = [*keyspressed]
        _keyspressed.sort()
        command = '_'.join([str(k) for k in _keyspressed])

        print(command)

        name = key_mappings(command)

        if name == 'NEW_FILE':
            new_file_widget = NewFileWidget(
                self,
                save=new_file.new_file
            )
            new_file_widget.setModal(True)
            new_file_widget.show()
            self.keylist = []
        else:
            self.on_toolbar_icon_click(name)
            self.keylist = []

    def on_toolbar_icon_click(self, name):
        self.current_tool = name

    def add_icon(self, icon_path):
        button = QPushButton(self.ui.toolOptionsWidget)
        button.setObjectName(icon_path['name'])
        button.setMinimumSize(QSize(32, 32))
        button.setMaximumSize(QSize(32, 32))
        button.setToolTip(icon_path['tooltip'])
        icon = QIcon()
        icon.addFile(icon_path['path'], QSize(), QIcon.Normal, QIcon.Off)
        button.setIcon(icon)
        button.setFlat(False)
        self.ui.verticalLayout.addWidget(button)
        self.ui.verticalLayout.insertWidget(self.ui.verticalLayout.count() - 1, button)
        button.setText("")

        button.clicked.connect(
            lambda: self.on_toolbar_icon_click(icon_path['name']))

    def add_toolbar_icons(self):
        toolbar_icons = [
            {'path': u':/images/images/toolbar_move.svg', 'tooltip': 'Move (space)', 'name': 'move'},
            {'path': u':/images/images/toolbar_dashed_box.svg', 'tooltip': 'Selection', 'name': 'dashed_box'},
            {'path': u':/images/images/toolbar_polygon_lasso.svg', 'tooltip': 'Polygon Lasso (w)', 'name': 'polygon_lasso'},
            {'path': u':/images/images/toolbar_a_pointer.svg', 'tooltip': 'Pointer', 'name': 'a_pointer'},
            {'path': u':/images/images/toolbar_rectangle.svg', 'tooltip': 'Rectangle', 'name': 'rectangle'},
            {'path': u':/images/images/toolbar_brush.svg', 'tooltip': 'Brush (b)', 'name': 'brush'},
            {'path': u':/images/images/toolbar_brush_arrow.svg', 'tooltip': 'Brush Arrow', 'name': 'brush_arrow'},
            {'path': u':/images/images/toolbar_crop.svg', 'tooltip': 'Crop (c)', 'name': 'crop'},
            {'path': u':/images/images/toolbar_eraser.svg', 'tooltip': 'Eraser (e)', 'name': 'eraser'},
            {'path': u':/images/images/toolbar_eyedropper.svg', 'tooltip': 'Eyedropper (i)', 'name': 'eyedropper'},
            {'path': u':/images/images/toolbar_frame.svg', 'tooltip': 'Frame', 'name': 'frame'},
            {'path': u':/images/images/toolbar_gradient.svg', 'tooltip': 'Gradient', 'name': 'gradient'},
            {'path': u':/images/images/toolbar_pointer_finger.svg', 'tooltip': 'pointer_finger', 'name': 'pointer_finger'},
            {'path': u':/images/images/toolbar_pin.svg', 'tooltip': 'Pin', 'name': 'pin'},
            {'path': u':/images/images/toolbar_pen.svg', 'tooltip': 'Pen (p)', 'name': 'pen'},
            {'path': u':/images/images/toolbar_quick_selection.svg', 'tooltip': 'quick_selection', 'name': 'quick_selection'},
            {'path': u':/images/images/toolbar_spot_headling.svg', 'tooltip': 'spot_headling', 'name': 'spot_headling'},
            {'path': u':/images/images/toolbar_stamp.svg', 'tooltip': 'Stamp (s)', 'name': 'stamp'},
            {'path': u':/images/images/toolbar_t.svg', 'tooltip': 'Text', 'name': 'text'},
            {'path': u':/images/images/toolbar_rotate_view.svg', 'tooltip': 'rotate_view', 'name': 'rotate_view'},
            {'path': u':/images/images/toolbar_zoom.svg', 'tooltip': 'Zoom (⌘ +/-)', 'name': 'zoom'},
        ]

        try:
            for icon_path in toolbar_icons:
                self.add_icon(icon_path)
        except:
            pass

    def render(self):
        self.add_toolbar_icons()


def main():
    app = QApplication(sys.argv)
    settings_window = MainWindow()
    settings_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()