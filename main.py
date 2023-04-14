import json
import sys
from pathlib import Path
from PySide6 import QtCore
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QPushButton

from styles.main import main_style
from ui import mainwindowui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainwindowui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(main_style())

        self.current_tool = None

        self.render()

    def on_toolbar_icon_click(self, button):
        selected_tool = button.objectName()
        self.current_tool = selected_tool
        # print(self.current_tool)
        # self.render()

    def refresh_toolbar_icons(self):
        # icon_buttons = range(self.ui.verticalLayout.count())

        # for widget_index in reversed(icon_buttons):
        #     # Instead of iterating over the children of
        #     # self.ui.buttonGroupWidget, a reversed index to the
        #     # widget must be used, otherwise it will result in
        #     # segmentation faults.
        #     widget = self.ui.verticalLayout.layout().itemAt(
        #         widget_index).widget()

        #     # if not_widget_decrement_button and not_widget_increment_button:
        #     self.ui.verticalLayout.layout().removeWidget(widget)
        #     widget.setParent(None)


        # # self.ui.verticalLayout.children()
        # print(self.ui.verticalLayout.count())
        # for i in range(self.ui.verticalLayout.count()):
        #     print(i)
        pass

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


        for icon_path in icons:
            button = QPushButton(self.ui.toolOptionsWidget)

            button.setObjectName(icon_path['name'])
            button.setMinimumSize(QSize(32, 32))
            button.setMaximumSize(QSize(32, 32))
            button.setToolTip(icon_path['tooltip'])
            icon = QIcon()
            icon.addFile(icon_path['path'], QSize(), QIcon.Normal, QIcon.Off)
            button.setIcon(icon)
            button.setFlat(False)
            button.setStyleSheet("QPushButton")
            self.ui.verticalLayout.addWidget(button)
            self.ui.verticalLayout.insertWidget(self.ui.verticalLayout.count() + 1, button)
            button.setText("")
            button.clicked.connect(
                lambda: self.on_toolbar_icon_click(button))

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