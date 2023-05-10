import json
import os
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QFrame, QLabel, QGraphicsBlurEffect

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtOpenGL import *

from datatypes.layer import Layer, LayerGroup, mode_mappings
from tool import Tool
from tool import ToolBase
from typing import List
from ui import workspaceui
from utils import load_settings, unit_conversion, pixel_to_inch, inch_to_pixel
from widgets.artboard import ArtBoardWidget
from widgets.window_panel import WindowPanelWidget
from widgets.windowbar import WindowsWidget

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
    show_window_panel = QtCore.Signal(dict)


class WorkspaceWidget(QWidget):
    def __init__(self, parent, new_file_info):
        super().__init__(parent)
        self.ui = workspaceui.Ui_Workspace()
        self.ui.setupUi(self)
        self.setMouseTracking(True)

        self.tool_settings = {}
        self.get_tool_settings()
        self._parent = parent

        self._current_layer = None
        self.tool = ToolBase(parent=self._parent, layer=self.current_layer)

        self.signaler = WorkspaceSignaler()
        self.new_file_info = new_file_info
        self._zoom = 1.0
        self.are_rulers_hidden = False
        self.ruler_dimensions = None
        self.settings = load_settings()
        self.absolute_dimentions = []
        self.artboards = []
        self.active_artboard = 0
        self.current_window = None

        self.offset = unit_conversion(
            self.settings['document_units'],
            self.settings['workspace_spillover'])

        # Mouse tracking lines.
        self.x_line = QVLine(self.ui.horizontalRulerWidget, thickness=2)
        self.y_line = QHLine(self.ui.verticalRulerWidget, thickness=2)
        self.x_line.setStyleSheet('border-color: rgba(255, 255, 255, 0.75)')
        self.y_line.setStyleSheet('border-color: rgba(255, 255, 255, 0.75)')

        self.signaler.mouseMove.connect(self.mouse_move_event)
        self.ui.scrollArea.setWidgetResizable(True)

        self.label = QLabel()
        self.ui.gridLayout_3.addWidget(self.label)
        self.down_mouse_pos = [0, 0]
        self.up_mouse_pos = [0, 0]
        self.base_width = 600
        self.base_zoom = 2.0
        self.drag_speed = 2.0
        self.snap_to = 30 # CANNOT BE ZERO

        # Brush
        self.last_x, self.last_y = None, None
        self.brush_color = qRgba(50, 50, 50, 50)
        self.brush_size = 30


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


        # TODO: Move rule logic to Workspace.
        # TODO: Move mouse tracking to Workspace.
        # TODO: Move Tool to Workspace.
        # TODO: Move Zoom to Workspace.
        # TODO: Move all Window code to Workspace.
        # TODO: Add all layers and layer rendering to Artboard.
        # Define layers with a default background layer
        self.layers = []

        self.flat_layers = []
        self.layers_dict = []

        # Background - Layer 0
        self.flat_layers.append(
            Layer(
                image=QPixmap("images/test_pink.jpg"),
                mode='Normal',
                name="Background",
            )
        )

        self.layers.append(
            Layer(
                image=QPixmap("images/test_pink.jpg"),
                mode='Normal',
                name="Background",
            )
        )

        self.layers.append(
            LayerGroup(
                image=QPixmap(self.layers[0].image.size()),
                name="Group 1",
                children=[
                    LayerGroup(
                        image=QPixmap(self.layers[0].image.size()),
                        mode="Multiply",
                        children=[
                            Layer(
                                image=QPixmap("images/test_green.jpg"),
                                mode='Normal'
                            ),
                        ]
                    ),
                    Layer(
                        image=QPixmap("images/test_green.jpg"),
                        mode='Multiply'
                    ),
                    Layer(
                        image=QPixmap("images/example.jpg"),
                        mode='Normal'
                    ),
                ],
                mode="HardLight"
            )
        )

        self.layers.append(
            Layer(
                lock=True,
                image=QPixmap("images/test_blue.jpg"),
                mode='Difference'
            )
        )

        self.grid = Layer(
            lock=True,
            name="Grid",
            image=self.draw_grid()
        )

        self.layers.append(self.grid)

        self.render()

        self.ui.zoomComboBox.currentTextChanged.connect(self.change_zoom_factor)
        self.ui.zoomComboBox.setCurrentText(str(80.0))
        self._zooms(80.0)
        self.ui.zoomComboBox.currentTextChanged.connect(self._zooms)

        self.signaler.remove_layer.connect(self.remove_layer)
        self.signaler.show_window_panel.connect(self.show_window_panel)

        self.temp = False
        self.current_layer = self.layers[0]

    @property
    def current_layer(self):
        return self._current_layer

    @current_layer.setter
    def current_layer(self, current_layer):
        self._current_layer = current_layer
        self.tool.layer = self._current_layer

    @property
    def current_tool(self):
        return self._current_tool

    @current_tool.setter
    def current_tool(self, current_tool):
        self._current_tool = current_tool
        self.tool.current_tool = current_tool
        print('current_tool', current_tool)

    @property
    def zoom(self):
        return self._zoom

    @zoom.setter
    def zoom(self, zoom):
        self._zoom = zoom
        self.draw_v_ruler()
        self.draw_h_ruler()
        self.render()

    def mouseEventFilter(self, event):
        print(event)

    def mouseMoveEvent(self, event):
        if self.temp:
            self.move(event)
        else:
            self.paint(event)

        self.render()
        self.mouse_move_event(event.pos().x(), event.pos().y())

    def _zooms(self, val):
        self.base_zoom = float(val) / 100.0
        self.zoom = self.base_zoom
        # print(val, self.base_zoom)

    def mouseReleaseEvent(self, event):
        self.up_mouse_pos = [0, 0]
        self.down_mouse_pos = [0, 0]

        # Brush
        self.last_x = None
        self.last_y = None

        self.temp = not self.temp
        # TODO: Translate layer position if moved
        self.current_layer.image = self.translate(self.current_layer.image, self.current_layer.position)
        self.current_layer.position = [0, 0]

    def mousePressEvent(self, event):
        self.down_mouse_pos = [event.x(), event.y()]
        self.up_mouse_pos = [event.x(), event.y()]

    def crop_workspace(self, image) -> QPixmap:
        # Crop image to a square:
        artboard = QImage(QSize(*self.absolute_dimentions), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(artboard)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.fillRect(
            QRect(
                0,
                0,
                *self.absolute_dimentions
            ),
            Qt.black
        )
        painter.fillRect(QRect(
                *self.settings['offset_dimensions'],
                *self.settings['document_dimensions'],
            ),
            image
        )
        painter.end()

        return self.image_to_pixmap(artboard)

    def translate_layer(self, base_image) -> QPixmap:
        resultImage = QImage(base_image.size(), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(resultImage)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.fillRect(resultImage.rect(), Qt.transparent)

        painter.translate(self.settings['offset_dimensions'][0], 0)

        painter.drawPixmap(0, 0, base_image)
        painter.setCompositionMode(QPainter.CompositionMode_DestinationOver)
        painter.fillRect(resultImage.rect(), Qt.white)
        painter.end()

        return self.image_to_pixmap(resultImage)

    def render(self):
        try:
            self.label.clear()
            res = self.render_layers()
            res = self.crop_workspace(res)
            res = res.scaledToWidth(self.base_zoom * self.base_width)
            self.label.setPixmap(res)
            # self.ui.gridLayout_3.addWidget(self.label)
        except Exception as e:
            print(e)

    def on_click(self):
        self.render()

    def render_layers(self):
        composite = self.layers[0].image

        for i in range(len(self.layers)):
            if isinstance(self.layers[i], LayerGroup):
                child_count = len(self.layers[i].children)
                group_composite = self.layers[i].children[0].image

                if child_count > 1:
                    for j in (range(child_count)):
                        group_composite = self.def_add_image(group_composite, self.layers[i].children[j])

                self.layers[i].image = group_composite

            composite = self.def_add_image(composite, self.layers[i])

        return composite

    def scale(self, layer, event):
        pass

    def invert(self):
        layer = self.current_layer

        temp_image = layer.image.toImage()
        temp_image.invertPixels(QImage.InvertRgba)
        temp_image = self.image_to_pixmap(temp_image)
        layer.image = temp_image

        self.render()

    def image_to_pixmap(self, image) -> QPixmap:
        return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)

    def quantize(self, num):
        return num - (num % self.snap_to)

    def move(self, event):
        self.down_mouse_pos = [
            self.quantize(event.x()),
            self.quantize(event.y())]

        [x, y] = self.current_layer.position
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

        self.current_layer.position = [dx, dy]
        self.up_mouse_pos = self.down_mouse_pos

    def change_mode(self, layer, mode):
        layer.mode = mode
        pass

    def draw_grid(self):
        layer = self.layers[0]
        w = layer.image.width()
        h = layer.image.height()
        gap = 100

        rows = h // gap
        cols = w // gap

        resultImage = QImage(layer.image.size(), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(resultImage)
        color = QColor(Qt.white)
        color.setAlphaF(0.5)
        painter.setPen(QPen(color, 2, Qt.SolidLine, Qt.RoundCap))

        for r in range(rows):
            painter.drawLine(0, r * gap, w, r * gap)

        for c in range(cols):
            painter.drawLine(c * gap, 0, c * gap, h)

        painter.end()

        return self.image_to_pixmap(resultImage)

    def update_layer(self, layer) -> QPixmap:
        resultImage = QImage(layer.image.size(), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(resultImage)
        painter.scale(*layer.scale)
        painter.translate(*layer.position)
        painter.drawPixmap(0, 0, layer.image)
        painter.fillRect(resultImage.rect(), Qt.transparent)
        painter.end()
        return self.image_to_pixmap(resultImage)

    def merge_images(self, image_1, image_2, mode: str='Normal'):
        mode = mode_mappings(mode)

        # layer.image = self.update_layer(layer)

        resultImage = QImage(image_1.size(), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(resultImage)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.fillRect(resultImage.rect(), Qt.transparent)

        painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
        painter.drawPixmap(0, 0, image_1)
        painter.setCompositionMode(mode)
        painter.drawPixmap(0, 0, image_2)
        painter.setCompositionMode(QPainter.CompositionMode_DestinationOver)
        painter.fillRect(resultImage.rect(), Qt.white)
        painter.end()

        return self.image_to_pixmap(resultImage)

    def paint(self, event):
        # layer = self.current_layer
        # [x_offset, y_offset] = layer.position
        # mode = mode_mappings(layer.mode)

        # x = event.x() * self.drag_speed - x_offset
        # y = event.y() * self.drag_speed - y_offset

        # if self.last_x is None: # First event.
        #     self.last_x = x
        #     self.last_y = y

        #     return # Ignore the first time.

        # resultImage = QImage(layer.image.size(), QImage.Format_ARGB32_Premultiplied)
        # painter = QPainter(resultImage)

        # pen = QtGui.QPen()
        # pen.setWidth(self.brush_size)
        # pen.setColor(self.brush_color)
        # # pen.setCosmetic(True)

        # space = 4
        # dashes = [1, space]
        # pen.setDashPattern(dashes)

        # pen.setStyle(Qt.SolidLine)
        # pen.setCapStyle(Qt.RoundCap)

        # # circle = QPixmap(QSize(self.brush_size, self.brush_size))
        # # circle.draw
        # # painter.drawEllipse(QPoint(0, 0), self.brush_size, self.brush_size)
        # # painter.drawEllipse(300, 300, 70, 70)

        # # Set brush from vector
        # brush = QIcon("images/toolbar_brush.svg").pixmap(QSize(self.brush_size, self.brush_size))
        # pen.setBrush(brush)
        # painter.setPen(pen)

        # painter.fillRect(resultImage.rect(), Qt.transparent)
        # painter.drawPixmap(0, 0, layer.image)
        # painter.setCompositionMode(mode)
        # painter.drawLine(self.last_x, self.last_y, x, y)
        # painter.end()

        # self.last_x = x
        # self.last_y = y

        # layer.image = self.image_to_pixmap(resultImage)
        # print(self.current_layer.image)
        try:
            # self.current_layer.image = self.tool.draw(event)
            self.tool.draw(event)
        except Exception as e:
            print(e)

    def translate(self, image: QPixmap, position: List) -> QPixmap:
        resultImage = QImage(image.size(), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(resultImage)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.fillRect(resultImage.rect(), Qt.transparent)
        # painter.translate(*position)
        painter.drawPixmap(*position, image)
        painter.setCompositionMode(mode_mappings('Normal'))
        painter.setCompositionMode(QPainter.CompositionMode_DestinationOver)
        painter.fillRect(resultImage.rect(), Qt.transparent)
        painter.end()

        return self.image_to_pixmap(resultImage)

    def def_add_image(self, base_image: QPixmap=None, layer: Layer=None) -> QPixmap:
        mode = mode_mappings(layer.mode)

        resultImage = QImage(base_image.size(), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(resultImage)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.fillRect(resultImage.rect(), Qt.transparent)

        painter.scale(*layer.scale)
        painter.translate(*layer.position)

        # painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
        painter.drawPixmap(0, 0, base_image)
        painter.setCompositionMode(mode)
        painter.drawPixmap(0, 0, layer.image)
        painter.setCompositionMode(QPainter.CompositionMode_DestinationOver)
        painter.fillRect(resultImage.rect(), Qt.transparent)
        painter.end()

        return self.image_to_pixmap(resultImage)
        # return QPixmap(base_image.size()).fromImage(resultImage, Qt.ColorOnly)

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
        # print(x, y)

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

        for widget_index in ruler_group:
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

    def select_window(self, window):
        print(window)
        if window['name'] == 'Layers':
            self.render_layers_panel(None)

    def adjust_window_panel_pos(self, e):
        x = self.WindowPanelWidget.x() + e.width()
        y = self.WindowPanelWidget.y()
        self.WindowPanelWidget.move(x, y)

    def show_window_panel(self, window=None):
        if window and (self.current_window is None or self.current_window['name'] != window['name']):
            self.current_window = window
            self.WindowPanelWidget.current_window = self.current_window
            self.WindowPanelWidget.show()
            x = window['pos'].x() - self.pos().x()
            y = window['pos'].y() - self.pos().y()
            flyout_width = self.WindowPanelWidget.width()
            self.WindowPanelWidget.move(x - flyout_width - 4, y - 30)
            self.select_window(window)
        else:
            self.WindowPanelWidget.hide()
            self.current_window = None
