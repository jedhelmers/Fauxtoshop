from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QFrame, QLabel

from ui import workspaceui
from widgets.artboard import ArtBoardWidget

inch_ticks = [
    0, 16, 14, 16
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
        self.dimensions = [30, 30]
        self.dimensions_offset = [2, 2]

        # Mouse tracking lines.
        self.x_line = QVLine(self.ui.horizontalRulerWidget, thickness=2)
        self.y_line = QHLine(self.ui.verticalRulerWidget, thickness=2)
        self.x_line.setStyleSheet('border-color: rgba(255, 255, 255, 0.75)')
        self.y_line.setStyleSheet('border-color: rgba(255, 255, 255, 0.75)')

        self.draw_v_ruler()
        self.draw_h_ruler()

        self.signaler.mouseMove.connect(self.mouse_move_event)
        self.ui.workspaceBackgroundWidget.setStyleSheet('padding: 40px;')

        self.ui.scrollArea.setWidgetResizable(True)

        ArtBoardWidget(self.ui.workspaceBackgroundWidget, new_file_info, self.dimensions_offset, self.signaler)

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
        # print(x, y)
        self.y_line.move(0, y)
        self.x_line.move(x, 0)

    def draw_h_ruler(self):
        for i in range(self.dimensions[0]):
            # print(i)
            self.draw_h_unit(i - self.dimensions_offset[0], i * 40)

    def draw_h_unit(self, index, h_offset=0):
        label = QLabel(self.ui.horizontalRulerWidget)
        label.setText(str(index))
        label.move(h_offset + 4, -6)

        for i, v_offset in enumerate(inch_ticks):
            line = QVLine(self.ui.horizontalRulerWidget, 20 - v_offset)
            line.move(i * (10 * self.zoom) + h_offset, v_offset)

    def draw_v_ruler(self):
        for i in range(self.dimensions[1]):
            self.draw_v_unit(i - self.dimensions_offset[1], i * 40)

    def draw_v_unit(self, index, v_offset=0):
        label = QLabel(self.ui.verticalRulerWidget)
        label.setText(str(index))
        label.move(4, v_offset - 6)

        for i, h_offset in enumerate(inch_ticks):
            line = QHLine(self.ui.verticalRulerWidget, 20 - h_offset)
            line.move(h_offset, i * (10 * self.zoom) + v_offset)

