from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget, QFrame, QLabel
from PySide6.QtGui import QPainter, QImage, QIcon, qRgba, QPixmap

from datas.tools import get_tool_icon
from datatypes.layer import Layer, mode_mappings
from utils import image_to_pixmap

class ToolBase():
    def __init__(self, parent, layer=None) -> None:
        self.parent = parent
        self._layer = layer
        print('WEE')
        self._mode = mode_mappings(layer.mode) if layer else None

        # Brush settings
        self._current_tool = None
        self._brush_size = 80
        self._history_brush_size = 10
        self._mixer_brush_size = 10
        self._eraser_size = 10
        self._slone_size = 10
        self._spot_healing_size = 10

        # Brush shapes
        self._brush_shape = "images/toolbar_brush.svg"

        # Misc
        self.base_zoom = 2.0
        self.drag_speed = 2.0
        self.snap_to = 20 # CANNOT BE ZERO

        # Brush
        self.last_x, self.last_y = None, None
        self.brush_color = qRgba(50, 50, 50, 50)
        self.last_x = None
        self.last_y = None

    @property
    def current_tool(self):
        return self._current_tool

    @current_tool.setter
    def current_tool(self, tool):
        self._current_tool = tool
        tool = get_tool_icon(self.current_tool)
        self.icon = QtGui.QIcon(tool.path).pixmap(QSize(*tool.size))
        self.cursor = QtGui.QCursor(self.icon, *tool.hotPoints)
        self.parent.setCursor(self.cursor)

    @property
    def layer(self):
        return self._layer

    @layer.setter
    def layer(self, layer):
        self._layer = layer
        self._mode = mode_mappings(layer.mode) if layer else None

    def draw(self, event):
        switch = {
            'pen': self.pen,
            'brush': self.brush,
            'erase': self.erase,
            'clone': self.clone
        }

        if self._layer and self.current_tool in switch:
            switch[self.current_tool](event)

    def pen(self, event):
        pass

    def brush(self, event):
        [x_offset, y_offset] = self.layer.position

        x = event.x() * self.drag_speed - x_offset
        y = event.y() * self.drag_speed - y_offset

        if self.last_x is None: # First event.
            self.last_x = x
            self.last_y = y

            return # Ignore the first time.

        resultImage = QImage(self.layer.image.size(), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(resultImage)

        pen = QtGui.QPen()
        pen.setWidth(self._brush_size)
        pen.setColor(self.brush_color)
        pen.setStyle(Qt.SolidLine)
        pen.setCapStyle(Qt.RoundCap)
        pen.setCosmetic(True)
        painter.setPen(pen)

        # Set STAMP
        # brush = QIcon(self._brush_shape).pixmap(QSize(self._brush_size, self._brush_size))
        # pen.setBrush(brush)
        # painter.setPen(pen)

        painter.fillRect(resultImage.rect(), Qt.transparent)
        painter.drawPixmap(0, 0, self.layer.image)
        painter.setCompositionMode(self._mode)
        painter.drawLine(self.last_x, self.last_y, x, y)
        painter.end()

        self.last_x = x
        self.last_y = y

        self.layer.image = image_to_pixmap(resultImage)

    def erase(self, event):
        pass

    def clone(self, event):
        pass

class Tool():
    def __init__(self, settings):
        self.settings = settings

        gradient = QtGui.QLinearGradient(QtCore.QPointF(50, -20), QtCore.QPointF(80, 20))
        gradient.setColorAt(0.0, Qt.white)
        gradient.setColorAt(1.0, QtGui.QColor(0xa6, 0xce, 0x39))

        self.background = QtGui.QBrush(QtGui.QColor(64, 32, 64))
        self.circleBrush = QtGui.QBrush(gradient)
        self.circlePen = QtGui.QPen(Qt.black)
        self.circlePen.setWidth(1)
        self.textPen = QtGui.QPen(Qt.white)
        self.textFont = QtGui.QFont()
        self.textFont.setPixelSize(50)

    def paint(self, painter, event, elapsed):
        painter.fillRect(event.rect(), self.background)
        painter.translate(100, 100)

        painter.save()
        painter.setBrush(self.circleBrush)
        painter.setPen(self.circlePen)
        painter.rotate(elapsed * 0.030)

        r = elapsed/1000.0
        n = 30
        for i in range(n):
            painter.rotate(30)
            radius = 0 + 120.0*((i+r)/n)
            circleRadius = 1 + ((i+r)/n)*20
            painter.drawEllipse(QtCore.QRectF(radius, -circleRadius,
                                       circleRadius*2, circleRadius*2))

        painter.restore()

        painter.setPen(self.textPen)
        painter.setFont(self.textFont)
        painter.drawText(QtCore.QRect(-50, -50, 100, 100), Qt.AlignCenter, "Qt")