import json
import os
from PySide6 import QtGui
from PySide6.QtGui import QImage
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import QSize, Qt, QRect, QPoint, QCoreApplication
from PySide6.QtWidgets import QWidget
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6 import QtOpenGL

from utils import unit_conversion

artboard_json_path = './datas/artboard.json'


class ActiveTool():
    def __init__(self):
        self._current_tool = 'brush'

    @property
    def current_tool(self):
        return self._current_tool

    @current_tool.setter
    def current_tool(self, tool):
        self.current_tool = tool


class ArtBoardWidget(QWidget):
    def __init__(
            self,
            parent,
            file_info,
            settings,
            signaler):
        super().__init__()
        self.setMouseTracking(True)
        # self.setAutoFillBackground(False)
        self.setStyleSheet('background: white; border: 2px solid white;')

        self.settings = settings
        self.workspace_signaler = signaler
        self.file_info = file_info
        self.setObjectName(file_info['name'])
        self.local_settings = {}

        self.name = 'Background'
        self.is_locked = True
        self.is_alpha_locked = False
        self.opacity = 1.0
        self.color = 'None'
        self.use_previous_layer_for_clipping_mask = False
        self.mode = 'Normal'

        # self.setGeometry(QRect(
        #     0,
        #     0,
        #     self.settings['absolute_dimensions'][0],
        #     self.settings['absolute_dimensions'][1]))

        # self.setMaximumSize(QSize(16777215, 16777215))
        self.setMinimumWidth(200)
        self.setMinimumHeight(200)

    def remove_layer(self, index):
        self.workspace_signaler.remove_layer.emit(index)

    def rename_layer(self, name):
        self.name = name

    def lock_layer(self, lock: bool):
        self.is_locked = lock

    def alpha_lock_layer(self, lock: bool):
        self.is_alpha_locked = lock

    def mousePressEvent(self, event):
        pos = event.pos()
        print('PRESS', pos.x(), pos.y())

    def mouseReleaseEvent(self, event):
        pos = event.pos()
        print('RELEASE', pos.x(), pos.y())

    def mouseMoveEvent(self, event):
        self.workspace_signaler.mouseMove.emit(event.pos().x(), event.pos().y())
        pass

    # def initializeGL(self):
    #     if 'bg_color' in self.file_info:
    #         r = self.file_info['bg_color'].redF()
    #         g = self.file_info['bg_color'].greenF()
    #         b = self.file_info['bg_color'].blueF()
    #         a = self.file_info['bg_color'].alphaF()

    #     self.context().functions().glClearColor(r, g, b, a)
    #     self.context().functions().glEnable(int('0x0C11', 16))
    #     self.context().functions().glScissor(
    #         self.settings['offset_dimensions'][0] * 2,
    #         self.settings['offset_dimensions'][1] * 2,
    #         self.settings['document_dimensions'][0] * 2,
    #         self.settings['document_dimensions'][1] * 2)

    #     self.context().functions().glClear(int('0x00004000', 16))
    #     # self.context().functions()

