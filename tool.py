from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget, QFrame, QLabel

from datas.tools import get_tool_icon

class ToolBase():
    def __init__(self, parent) -> None:
        self.parent = parent
        self._current_tool = None

    @property
    def current_tool(self):
        return self._current_tool

    @current_tool.setter
    def current_tool(self, tool):
        print(tool)
        self._current_tool = tool
        # TODO:
        # Update the icon to reflect the tool.
        tool = get_tool_icon(self.current_tool)
        self.icon = QtGui.QIcon(tool.path).pixmap(QSize(*tool.size))
        self.cursor = QtGui.QCursor(self.icon, *tool.hotPoints)
        self.parent.setCursor(self.cursor)
        print(tool.name, tool.path, tool.size)

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