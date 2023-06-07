from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, QLineF, QPointF, Qt, QEvent, QPoint, QObject, QCoreApplication, QRect
from PySide6.QtGui import QIcon, QPixmap, QConicalGradient, QBrush, QRadialGradient, QImage, QPainter, QColor, QMouseEvent, qRgba, QPen
from PySide6.QtWidgets import QMainWindow, QScrollArea, QFrame, QApplication, QTableWidgetItem, QGraphicsScene, QGraphicsPixmapItem, QPushButton, QWidget, QGridLayout, QLabel

from datas.tools import get_tool_icon
from datatypes.layer import Layer, mode_mappings
from utils import image_to_pixmap

class Tool(QWidget):
    def __init__(
            self,
            canvas: QScrollArea,
            parent
        ) -> None:
        super().__init__(parent)
        self.canvas = canvas
        self._layer = None

        # Brush settings
        self.brush_color = QColor(150, 50, 50, 50)
        self.brush_size = 80
        self.hardness = 0.20
        self.opacity = 1.0
        self.flow = 1.0
        self.mode = 'Normal'

        # Mouse stuff
        self.last_x = None
        self.last_y = None
        self.drag_speed  = 1.0
        self.down_mouse_pos = [0, 0]
        self.up_mouse_pos = [0, 0]
        self.snap_to = 30 # CANNOT BE ZERO

    @property
    def opacity(self):
        return self._opacity

    @opacity.setter
    def opacity(self, opacity: float):
        print(self.brush_color.alpha(), int(255 * opacity))
        self.brush_color.setAlpha(255 * opacity)
        self._opacity = opacity

    @property
    def flow(self):
        return self._flow

    @flow.setter
    def flow(self, flow: float):
        self.brush_color.setAlpha(255 * flow)
        self._flow = flow

    @property
    def active_tool(self):
        # print('active_tool', self._active_tool)
        return self._active_tool

    @active_tool.setter
    def active_tool(self, active_tool):
        self._active_tool = active_tool
        self.draw_cursor()

    @property
    def brush_size(self):
        return self._brush_size

    @brush_size.setter
    def brush_size(self, brush_size):
        self._brush_size = brush_size

    @property
    def layer(self):
        return self._layer

    @layer.setter
    def layer(self, layer):
        print('78', layer)
        self._layer = layer
        # TODO: Brush mode
        self._mode = mode_mappings(layer.mode) if layer else None

    def mousePressEvent(self, event):
        self.down_mouse_pos = [event.position().x(), event.position().y()]
        self.up_mouse_pos = [event.position().x(), event.position().y()]

    def quantize(self, num):
        return num - (num % self.snap_to)

    def reset_mouse_pos(self):
        self.last_x = None
        self.last_y = None

    def draw_cursor(self):
        tool = get_tool_icon(self.active_tool)
        print('BUTTS', tool.name)
        if tool.name == "brush":
            size = self.brush_size
            box_size = size * 1.3

            half_size = size * 0.35
            hardness_size = half_size * self.hardness

            b = QPixmap(box_size, box_size)
            b.fill(Qt.transparent)

            p = QPainter(b)
            # p.setRenderHint(QPainter.Antialiasing, True)

            pen = QPen()
            pen.setColor(QColor(0, 0, 0, 200))
            pen.setWidth(1)
            p.setPen(pen)

            # Move painter
            p.translate(half_size, half_size)
            # Outer
            p.drawEllipse(QPoint(0, 0), half_size, half_size)
            # Inner
            p.drawEllipse(QPoint(0, 0), hardness_size, hardness_size)
            p.end()

            self.cursor = QtGui.QCursor(b, -1, -1)
        else:
            self.icon = QtGui.QIcon(tool.path).pixmap(QSize(15, 15))
            self.cursor = QtGui.QCursor(self.icon, *tool.hotPoints)

        self.parent().setCursor(self.cursor)

    def draw(self, event):
        # TODO: Figure out why the brush is offset
        # print(self.active_tool)
        switch = {
            # 'pen': self.pen,
            'brush': self.brush,
            # 'erase': self.erase,
            # 'clone': self.clone,
            'move': self.move
        }

        if self.layer and self.active_tool in switch:
            switch[self.active_tool](event)

    def image_to_pixmap(self, image) -> QPixmap:
        if image:
            return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)

    def move(self, event):
        self.down_mouse_pos = [
            self.quantize(event.x()),
            self.quantize(event.y())]

        [x, y] = self.layer.position
        [x1, y1] = self.down_mouse_pos
        [x2, y2] = self.up_mouse_pos
        dx = ((x1 - x2) * self.drag_speed) + x
        dy = ((y1 - y2) * self.drag_speed) + y

        # # Snap to
        # if self.snap_to:
        #     if dx % self.snap_to != 0:
        #         dx = x
        #     if dy % self.snap_to != 0:
        #         dy = y

        self.layer.position = [dx, dy]
        self.up_mouse_pos = self.down_mouse_pos

    # def move(self, event):
    #     [x_offset, y_offset] = self.layer.position

    #     x = event.position().x() * self.drag_speed - x_offset
    #     y = event.position().y() * self.drag_speed - y_offset

    #     if self.last_x is None: # First event.
    #         self.last_x = x
    #         self.last_y = y

    #     resultImage = QImage(self.layer.image.size(), QImage.Format_ARGB32_Premultiplied)
    #     painter = QPainter(resultImage)
    #     painter.fillRect(resultImage.rect(), Qt.transparent)
    #     # painter.translate(self.last_x, self.last_y)
    #     painter.drawPixmap(x, y, self.layer.image)
    #     painter.end()
    #     self.layer.image = self.image_to_pixmap(resultImage)

    def brush(self, event):
        if self.layer and self.layer.image:
            # TODO: why is self.layer None?
            scroll_offset_x = self.canvas.horizontalScrollBar().value()
            scroll_offset_y = self.canvas.verticalScrollBar().value()

            [x_offset, y_offset] = self.parent().pos().toTuple()
            x = scroll_offset_x + event.position().x() * self.drag_speed - x_offset - 70
            y = scroll_offset_y + event.position().y() * self.drag_speed - y_offset - 40

            if self.last_x is None: # First event.
                self.last_x = x
                self.last_y = y

                return # Ignore the first time.

            resultImage = QImage(self.layer.image.size(), QImage.Format_ARGB32_Premultiplied)
            painter = QPainter(resultImage)
            painter.setCompositionMode(QPainter.CompositionMode_Source)
            painter.fillRect(resultImage.rect(), Qt.transparent)

            gradient = QRadialGradient(QPoint(x, y), self.brush_size / 2)
            gradient.setCenter(x, y)
            gradient.setColorAt(0.0, self.brush_color)
            gradient.setColorAt(self.hardness, self.brush_color)
            gradient.setColorAt(1.0, Qt.transparent)

            pen = QPen(gradient, self.brush_size)
            pen.setStyle(Qt.SolidLine)
            pen.setCapStyle(Qt.RoundCap)
            painter.setPen(pen)

            painter.drawPixmap(0, 0, self.layer.image)
            painter.setCompositionMode(mode_mappings(self.mode))
            painter.drawLine(self.last_x, self.last_y, x, y)
            painter.end()

            self.last_x = x
            self.last_y = y

            self.layer.image = self.image_to_pixmap(resultImage)
