import os
from PySide6 import QtGui
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import QSize, Qt, QRect, QPoint, QCoreApplication
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6 import QtOpenGL

from utils import unit_conversion


class ArtBoardWidget(QOpenGLWidget):
    def __init__(
            self,
            parent,
            file_info,
            settings,
            signaler):
        super().__init__(parent)
        self.setMouseTracking(True)

        self.settings = settings
        self.signaler = signaler
        self.file_info = file_info
        self.setObjectName(file_info['name'])

        # path = './images/broom.svg'

        # x = QSvgRenderer(path)
        # image = QtGui.QPixmap()
        # image.fill(Qt.transparent)
        # painter = QtGui.QPainter()
        # painter.begin(image)
        # x.render(painter)
        # painter.end()
        # print('X', image)

        # icon = QtGui.QIcon(path).pixmap(QSize())
        # print('icon', icon)
        # cursor = QtGui.QCursor(image)
        # print('cursor', cursor)
        # self.setCursor(cursor)

        self.setGeometry(QRect(
            0,
            0,
            self.settings['absolute_dimensions'][0],
            self.settings['absolute_dimensions'][1]))

        self.setMaximumSize(QSize(16777215, 16777215))

    def mousePressEvent(self, event):
        pos = event.pos()
        print('PRESS', pos.x(), pos.y())

    def mouseReleaseEvent(self, event):
        pos = event.pos()
        print('RELEASE', pos.x(), pos.y())

    def mouseMoveEvent(self, event):
        self.signaler.mouseMove.emit(event.pos().x(), event.pos().y())
        pass

    def initializeGL(self):
        if 'bg_color' in self.file_info:
            r = self.file_info['bg_color'].redF()
            g = self.file_info['bg_color'].greenF()
            b = self.file_info['bg_color'].blueF()
            a = self.file_info['bg_color'].alphaF()

        self.context().functions().glClearColor(r, g, b, a)
        self.context().functions()



