from PySide6 import QtGui
from PySide6.QtCore import QSize, Qt, QRect, QPoint, QCoreApplication
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6 import QtOpenGL

def conversion(unit, value):
    print(unit)
    if unit == 'Inches':
        return 96 * value
    elif unit == 'Pixels':
        return value
    elif unit == 'Picas':
        return value / 0.062499992175197
    return value

class ArtBoardWidget(QOpenGLWidget):
    def __init__(self, parent, file_info):
        super().__init__(parent)
        # self.ui.setupUi(self)

        print(self.screen())
        self.setMouseTracking(True)
        self.file_info = file_info

        self.bg_color = (1.0, 1.0, 1.0, 1.0)

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
        print(event.pos())

    def mouseMoveEvent(self, event):
        print(event.pos().x(), event.pos().y())

    def initializeGL(self):
        # VBO = self.__createVBO(self.vertices)

        # # Create and bind here once because we have only one VAO that there's no need to bind every time
        # VAO = self.__createVAO()

        # self.shader_program = self.__compileShaders(path_vertex="shaders/triangle.vs",
        #                                         path_fragment="shaders/triangle.fs")
        # self.attr_position = self.createAttribute(self.shader_program, "a_position", 0)
        print('initialize gl')

        try:
            print(self.context())
            # self.initializeGL()
            self.context().functions().glClearColor(1.0, 1.0, 1.0, 1.0)
        except Exception as e:
            print(e)
        pass

