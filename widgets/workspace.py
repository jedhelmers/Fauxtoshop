from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QFrame, QLabel

from ui import workspaceui
from utils import load_settings, unit_conversion, pixel_to_inch, inch_to_pixel
from widgets.artboard import ArtBoardWidget

inch_ticks = [
    16, 14, 16, 0
]


class QHLine(QFrame):
    def __init__(self, parent, width=20, thickness=1):
        super(QHLine, self).__init__(parent=parent)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setMaximumHeight(thickness)
        self.setMaximumWidth(width)
        self.setStyleSheet('border-color: rgba(255, 255, 255, 0.1)')


class QVLine(QFrame):
    def __init__(self, parent, height=20, thickness=1):
        super(QVLine, self).__init__(parent=parent)
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setMaximumWidth(thickness)
        self.setMaximumHeight(height)
        self.setStyleSheet('border-color: rgba(255, 255, 255, 0.1)')


class WorkspaceSignaler(QtCore.QObject):
    mouseMove = QtCore.Signal(int, int)


class WorkspaceWidget(QWidget):
    def __init__(self, parent, new_file_info):
        super().__init__(parent)
        self.ui = workspaceui.Ui_Workspace()
        self.ui.setupUi(self)
        self.signaler = WorkspaceSignaler()
        self.new_file_info = new_file_info
        self.zoom = 1.0
        self.are_rulers_hidden = False
        self.ruler_dimensions = None
        self.settings = load_settings()
        self.absolute_dimentions = []

        self.offset = unit_conversion(
            self.settings['document_units'],
            self.settings['workspace_spillover'])

        # Mouse tracking lines.
        self.x_line = QVLine(self.ui.horizontalRulerWidget, thickness=2)
        self.y_line = QHLine(self.ui.verticalRulerWidget, thickness=2)
        self.x_line.setStyleSheet('border-color: rgba(255, 255, 255, 0.75)')
        self.y_line.setStyleSheet('border-color: rgba(255, 255, 255, 0.75)')

        self.signaler.mouseMove.connect(self.mouse_move_event)
        self.ui.workspaceBackgroundWidget.setStyleSheet('padding: 40px;')

        self.ui.scrollArea.setWidgetResizable(True)

        self.width = unit_conversion(
            self.new_file_info['units_w'],
            float(self.new_file_info['width']))
        self.height = unit_conversion(
            self.new_file_info['units_h'],
            float(self.new_file_info['height']))

        self.absolute_dimentions = [
            self.width + self.offset + self.offset,
            self.height + self.offset + self.offset
        ]

        self.settings['offset_dimensions'] = [self.offset, self.offset]
        self.settings['document_dimensions'] = [self.width, self.height]

        self.settings['absolute_dimensions'] = self.absolute_dimentions

        self.ruler_dimensions = [
            pixel_to_inch(self.absolute_dimentions[0]),
            pixel_to_inch(self.absolute_dimentions[1])
        ]

        print('SETTINGS', self.settings)

        self.draw_v_ruler()
        self.draw_h_ruler()

        ArtBoardWidget(
            self.ui.workspaceBackgroundWidget,
            new_file_info,
            self.settings,
            self.signaler)

    def toggle_rulers(self):
        if self.are_rulers_hidden:
            self.show_rulers()
        else:
            self.hide_rulers()

    def hide_rulers(self):
        self.are_rulers_hidden = True
        self.ui.horizontalRulerWidget.hide()
        self.ui.verticalRulerWidget.hide()

    def show_rulers(self):
        self.are_rulers_hidden = False
        self.ui.horizontalRulerWidget.show()
        self.ui.verticalRulerWidget.show()

    def mouse_move_event(self, x, y):
        self.y_line.move(0, y)
        self.x_line.move(x, 0)

    def draw_h_ruler(self):
        for i in range(self.ruler_dimensions[0]):
            self.draw_h_unit(i - self.settings['workspace_spillover'], inch_to_pixel(i))

    def draw_h_unit(self, index, h_offset=0):
        label = QLabel(self.ui.horizontalRulerWidget)
        label.setText(str(index))
        label.move(h_offset + 4, -6)
        tick_width = 94 / len(inch_ticks)

        for i, v_offset in enumerate(inch_ticks):
            line = QVLine(self.ui.horizontalRulerWidget, 20 - v_offset)
            line.move((i + 1) * (tick_width * self.zoom) + h_offset, v_offset)

    def draw_v_ruler(self):
        for i in range(self.ruler_dimensions[1]):
            self.draw_v_unit(i - self.settings['workspace_spillover'], inch_to_pixel(i))

    def draw_v_unit(self, index, v_offset=0):
        label = QLabel(self.ui.verticalRulerWidget)
        label.setText(str(index))
        label.move(4, v_offset - 6)
        tick_height = 94 / len(inch_ticks)

        for i, h_offset in enumerate(inch_ticks):
            line = QHLine(self.ui.verticalRulerWidget, 20 - h_offset)
            line.move(h_offset, (i + 1) * (tick_height * self.zoom) + v_offset)

