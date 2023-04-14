import json
import sys
from pathlib import Path
from PySide6 import QtCore
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QPushButton

from styles.main import main_style
from ui import mainwindowui

def keymappings(key):
    switch = {
        73: 'eyedropper',
        77: 'move',
        0: 'dashed_box',
        0: 'polygon_lasso',
        0: 'a_pointer',
        0: 'box',
        66: 'brush',
        67: 'crop',
        0: 'eraser',
        0: 'frame',
        0: 'gradient',
        0: 'pointer_finger',
        0: 'pin',
        80: 'pen',
        0: 'quick_selection',
        0: 'spot_headling',
        83: 'stamp',
        0: 't',
        0: 'rotate_view',
        0: 'zoom',
    }
    return switch[key] if key in switch else None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainwindowui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(main_style())

        self.current_tool = None

        self.render()

    def keyPressEvent(self, e):
        # print(e.key())
        self.current_tool = keymappings(e.key())

        if e.key() == Qt.Key_F5:
            self.close()

        button = self.ui.toolOptionsWidget.findChild(QPushButton, self.current_tool)
        print('button', button)
        if button is not None:
            self.on_toolbar_icon_click(button, self.current_tool)

    def on_toolbar_icon_click(self, button, name):
        self.refresh_toolbar_icons()
        self.current_tool = name
        button.setStyleSheet('QPushButton {background-color: rgba(255, 255, 255, .25);}')

    def refresh_toolbar_icons(self):
        for widget in self.ui.toolbarWidget.children():
            if isinstance(widget, QPushButton):
                widget.setStyleSheet('QPushButton {background-color: transparent;}')

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
            lambda: self.on_toolbar_icon_click(button, icon_path['name']))

    def add_toolbar_icons(self):
        icons = [
            {'path': u':/images/images/toolbar_move.svg', 'tooltip': 'Move (space)', 'name': 'move'},
            {'path': u':/images/images/toolbar_dashed_box.svg', 'tooltip': 'Selection', 'name': 'dashed_box'},
            {'path': u':/images/images/toolbar_polygon_lasso.svg', 'tooltip': 'Polygon Lasso (w)', 'name': 'polygon_lasso'},
            {'path': u':/images/images/toolbar_a_pointer.svg', 'tooltip': 'Pointer', 'name': 'a_pointer'},
            {'path': u':/images/images/toolbar_box.svg', 'tooltip': 'Box', 'name': 'box'},
            {'path': u':/images/images/toolbar_brush.svg', 'tooltip': 'Brush (b)', 'name': 'brush'},
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
            {'path': u':/images/images/toolbar_t.svg', 'tooltip': 'Font', 'name': 't'},
            {'path': u':/images/images/toolbar_rotate_view.svg', 'tooltip': 'rotate_view', 'name': 'rotate_view'},
            {'path': u':/images/images/toolbar_zoom.svg', 'tooltip': 'Zoom (⌘ +/-)', 'name': 'zoom'},
        ]


        try:
            for icon_path in icons:
                self.add_icon(icon_path)
        except:
            pass

    def render(self):
        self.refresh_toolbar_icons()
        self.add_toolbar_icons()


def main():
    app = QApplication(sys.argv)
    settings_window = MainWindow()
    settings_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()