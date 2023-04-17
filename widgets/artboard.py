from PySide6 import QtGui
from PySide6.QtCore import QSize, Qt, QRect, QPoint, QCoreApplication
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6 import QtOpenGL

def conversion(unit, value):
    if unit == 'Inches':
        return 96 * value
    elif unit == 'Pixels':
        return value
    elif unit == 'Picas':
        return value / 0.062499992175197
    return value

class ArtBoardWidget(QOpenGLWidget):
    def __init__(self, parent, file_info, signaler):
        super().__init__(parent)
        self.setMouseTracking(True)

        self.signaler = signaler
        self.file_info = file_info
        self.setObjectName(file_info['name'])
        self.setGeometry(QRect(
            0,
            0,
            conversion(
                self.file_info['units_w'],
                float(self.file_info['width'])),
            conversion(
                self.file_info['units_h'],
                float(self.file_info['height']))
        ))

        self.setMaximumSize(QSize(16777215, 16777215))

    def mousePressEvent(self, event):
        pos = event.pos()
        print('PRESS', pos.x(), pos.y())

    def mouseReleaseEvent(self, event):
        pos = event.pos()
        print('RELEASE', pos.x(), pos.y())

    def mouseMoveEvent(self, event):
        # print(event.pos().x(), event.pos().y())
        self.signaler.mouseMove.emit(event.pos().x(), event.pos().y())
        pass

    def initializeGL(self):
        if 'bg_color' in self.file_info:
            r = self.file_info['bg_color'].redF()
            g = self.file_info['bg_color'].greenF()
            b = self.file_info['bg_color'].blueF()
            a = self.file_info['bg_color'].alphaF()

        self.context().functions().glClearColor(r, g, b, a)


