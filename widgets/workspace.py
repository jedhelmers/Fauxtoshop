import json
import os
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QWidget, QFrame, QLabel
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6 import QtOpenGL
from PySide6.QtOpenGLWidgets import QOpenGLWidget

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtOpenGL import *

from datatypes.layer import Layer, mode_mappings
from tool import Tool
from ui import workspaceui
from utils import load_settings, unit_conversion, pixel_to_inch, inch_to_pixel
from widgets.artboard import ArtBoardWidget

toolsettings_json_path = './datas/toolsettings.json'

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


class Widget(QWidget):
    def __init__(self, helper, parent = None):
        QWidget.__init__(self, parent)

        self.helper = helper
        self.elapsed = 0
        self.setFixedSize(600, 600)

    def animate(self):
        self.elapsed = (self.elapsed + self.sender().interval()) % 1000
        self.repaint()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.helper.paint(painter, event, self.elapsed)
        painter.end()


class WorkspaceSignaler(QtCore.QObject):
    mouseMove = QtCore.Signal(int, int)
    remove_layer = QtCore.Signal(int)


class WorkspaceWidget(QWidget):
    def __init__(self, parent, new_file_info):
        super().__init__(parent)
        self.ui = workspaceui.Ui_Workspace()
        self.ui.setupUi(self)
        self.setMouseTracking(True)

        self.tool_settings = {}
        self.get_tool_settings()

        self.signaler = WorkspaceSignaler()
        self.new_file_info = new_file_info
        self._zoom = 1.0
        self.are_rulers_hidden = False
        self.ruler_dimensions = None
        self.settings = load_settings()
        self.absolute_dimentions = []
        self.artboards = []
        self.active_artboard = 0

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

        # artboard = ArtBoardWidget(
        #     self.ui.workspaceBackgroundWidget,
        #     new_file_info,
        #     self.settings,
        #     self.signaler)
        # self.artboards.append(artboard)


        # TODO: Move rule logic to Workspace.
        # TODO: Move mouse tracking to Workspace.
        # TODO: Move Tool to Workspace.
        # TODO: Move Zoom to Workspace.
        # TODO: Add all layers and layer rendering to Artboard.
        # Define layers with a default background layer
        self.layers = [
            Layer(
                name="Background",
                lock=True,
                image=QPixmap("images/test_blue.jpg"),
            )]
        self.layers.append(
            Layer(
                image=QPixmap("images/test_green.jpg"),
                mode='Difference'
            )
        )
        self.layers.append(
            Layer(
                image=QPixmap("images/test_pink.jpg"),
                mode='Multiply'
            )
        )

        try:
            label = QLabel()
            res = self.render_layers()
            res = res.scaledToWidth(400)
            label.setPixmap(res)
        except Exception as e:
            print(e)




        self.ui.gridLayout_3.addWidget(label)

        self.ui.zoomComboBox.currentTextChanged.connect(self.change_zoom_factor)
        self.ui.zoomComboBox.setCurrentText(str(100.0))

        self.signaler.remove_layer.connect(self.remove_layer)

        self.tool = Tool(self.tool_settings)


    @property
    def zoom(self):
        return self._zoom

    @zoom.setter
    def zoom(self, zoom):
        self._zoom = zoom
        self.draw_v_ruler()
        self.draw_h_ruler()

    def render_layers(self):
        composite = self.layers[0].image
        for i in reversed(range(1, len(self.layers))):
            composite = self.def_add_image(composite, self.layers[i])

        return composite

    def def_add_image(self, base_image: QPixmap=None, layer: Layer=None) -> QPixmap:
        mode = mode_mappings(layer.mode)

        resultImage = QImage(base_image.size(), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(resultImage)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.fillRect(resultImage.rect(), Qt.transparent)
        painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
        painter.drawPixmap(0, 0, base_image)
        painter.setCompositionMode(mode)
        painter.drawPixmap(0, 0, layer.image)
        painter.setCompositionMode(QPainter.CompositionMode_DestinationOver)
        painter.fillRect(resultImage.rect(), Qt.white)
        painter.end()

        return QPixmap(base_image.size()).fromImage(resultImage, Qt.ColorOnly)

    def get_tool_settings(self):
        if os.path.exists(toolsettings_json_path):
            f = open(toolsettings_json_path, 'r')
            self.tool_settings = json.load(f)
            f.close()

    def remove_layer(self, index):
        self.artboards.pop(index)

    def move_layer(self, from_index, to_index):
        if to_index > from_index:
            to_index -= 1

        artboard = self.artboards.pop(from_index)
        self.artboards.insert(to_index, artboard)

    def change_zoom_factor(self):
        self.zoom = float(self.ui.zoomComboBox.currentText())

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
            line.move(((i + 1) * tick_width + h_offset) * (self.zoom/100.0), v_offset)

    def draw_v_ruler(self):
        ruler_group = range(self.ui.verticalRulerWidget.layout().count())
        for widget_index in reversed(ruler_group):
            widget = self.ui.verticalRulerWidget.layout().itemAt(
                widget_index).widget()
            if widget:
                widget.setParent(None)

        for i in range(self.ruler_dimensions[1]):
            # print(self.zoom, type(self.zoom))
            self.draw_v_unit(i - self.settings['workspace_spillover'], inch_to_pixel(i))

    def draw_v_unit(self, index, v_offset=0):
        label = QLabel(self.ui.verticalRulerWidget)
        label.setText(str(index))
        label.move(4, v_offset - 6)
        tick_height = 94 / len(inch_ticks)

        for i, h_offset in enumerate(inch_ticks):
            line = QHLine(self.ui.verticalRulerWidget, 20 - h_offset)
            line.move(h_offset, ((i + 1) * tick_height + v_offset) * (self.zoom/100.0))

