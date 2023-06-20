import json
import random
import sys
from pathlib import Path
from typing import Any

import cv2
import numpy as np
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, QLineF, QPointF, Qt, QEvent, QPoint, QObject, QCoreApplication, QRect
from PySide6.QtGui import QIcon, QPixmap, QConicalGradient, QBrush, QRadialGradient, QImage, QPainter, QColor, QMouseEvent, qRgba, QPen
from PySide6.QtWidgets import QMainWindow, QScrollArea, QFrame, QApplication, QTableWidgetItem, QGraphicsScene, QGraphicsPixmapItem, QPushButton, QWidget, QGridLayout, QLabel

from datas.tools import get_tool_icon
from datatypes.layer import ArtBoard, Layer, LayerGroup, mode_mappings
from keymappings import key_mappings
from styles.main import main_style
from tool import Tool
from ui import mainwindow_newui
from utils import QHLine, QVLine, set_dpi, inch_to_pixel, pixel_to_inch
from widgets.tool_options import ToolOptionsWidget
from widgets.toolsidebar import ToolSidebarWidget
from widgets.windows.layers import LayersWindowWidget
from workspace import WorkspaceWidget

# import roman
# print('ROMAN', roman.int_to_roman_string(4))
# print('ROMAN', roman.ButtsWidget)

def create_mask():
    im = cv2.imread("spectacles.png", cv2.IMREAD_UNCHANGED)
    _, mask = cv2.threshold(im[:, :, 3], 0, 255, cv2.THRESH_BINARY)
    cv2.imwrite('mask.jpg', mask)


# SIGNALS
class MainSignaler(QtCore.QObject):
    new_layer = QtCore.Signal(Layer)
    delete_layer = QtCore.Signal(int)
    lock_layer = QtCore.Signal(int)
    hide_layer = QtCore.Signal(int)
    update_layer_mode = QtCore.Signal(int, str)
    set_current_layer = QtCore.Signal(str)
    set_active_tool = QtCore.Signal(str)
    update_tool_property = QtCore.Signal(dict)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP
        self.ui = mainwindow_newui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.signaler = MainSignaler()
        self.settings = {}
        self.keylist = []
        self.firstrelease = True
        self.setStyleSheet(main_style())

        # Ruler
        self.x_line = QVLine(self.ui.horizontalRulerWidget, thickness=2)
        self.y_line = QHLine(self.ui.verticalRulerWidget, thickness=2)
        self.x_line.setStyleSheet('border-color: rgba(255, 255, 255, 0.75)')
        self.y_line.setStyleSheet('border-color: rgba(255, 255, 255, 0.75)')

        # UI
        self.label = QLabel()
        self.label.setMouseTracking(True)
        # bs = roman.ButtsWidget()
        # bs.ui.label.setText('WEEE')
        # self.ui.gridLayout_3.addWidget(bs)
        self.ui.gridLayout_3.addWidget(self.label)
        self.ui.gridLayout_3.setAlignment(Qt.AlignHCenter)
        # self.ui.gridLayout_3.setAlignment(Qt.AlignTop)
        self.zoom = 1.0
        self.scroll_area_size_pos = [0, 0, 0, 0]

        # Grid
        self.grid = None

        # Windows
        self.windows = {}

        # Tools
        self.tool = Tool(
            self.ui.scrollArea,
            self.label,
        )
        self.tool.setMouseTracking(True)
        self.tool.active_tool = 'brush'
        self.toolbar = ToolSidebarWidget(
            main_signaler=self.signaler,
            tool=self.tool
        )
        self.ui.toolbarWidget.layout().addWidget(self.toolbar)

        # Tool Options
        tool_options = ToolOptionsWidget(
            main_signaler=self.signaler,
            tool=self.tool
        )
        self.ui.toolOptionsWidget.layout().addWidget(tool_options)

        # DATA
        self.artboard = ArtBoard()
        self.layers = []
        self.current_layer = None

        # Signals
        self.signaler.new_layer.connect(self.new_layer)
        self.signaler.set_current_layer.connect(self.set_current_layer)
        self.signaler.delete_layer.connect(self.delete_layer)
        self.signaler.lock_layer.connect(self.lock_layer)
        self.signaler.hide_layer.connect(self.hide_layer)
        self.signaler.update_layer_mode.connect(self.update_layer_mode)
        self.signaler.set_active_tool.connect(self.set_active_tool)
        self.signaler.update_tool_property.connect(self.update_tool_property)

        # TEMP
        document_dimensions = [800, 700]
        offset_dimensions = [250, 200]
        absolute_dimensions = [
            document_dimensions[0] + offset_dimensions[0],
            document_dimensions[1] + offset_dimensions[1],
        ]
        new_file_information = {
            'document_dimensions': document_dimensions,
            'absolute_dimensions': absolute_dimensions,
            'color': QColor(155, 245, 255, 255),
            'offset_dimensions': offset_dimensions,
            'aspect_ratio': [
                document_dimensions[0] / document_dimensions[1],
                document_dimensions[1] / document_dimensions[0],
            ]
        }
        self.initialize_document(new_file_information)
        self.draw_rulers()
        self.generate_window_panels()
        self.render()

        # Set focus to label widget
        self.ui.scrollArea.ensureWidgetVisible(self.label, 0, 0)

        pixel_to_inch(12345)

    @property
    def layers(self):
        return self._layers

    @layers.setter
    def layers(self, layers):
        self._layers = layers
        self.render()

        # TODO: Handle this better
        if 'layers_widget'  in self.windows:
            self.windows['layers_widget'].layers = self.layers
            self.windows['layers_widget'].render_layers()

    @property
    def current_layer(self):
        return self._current_layer

    @current_layer.setter
    def current_layer(self, current_layer):
        print('current_layer', current_layer)
        self._current_layer = current_layer
        layer = self.get_layer()
        self.tool.layer = layer

    @property
    def active_tool(self):
        return self._active_tool

    @active_tool.setter
    def active_tool(self, active_tool):
        self._active_tool = active_tool
        self.tool.active_tool = self.active_tool

    # Overrides
    def keyPressEvent(self, event):
        print(event)
        self.firstrelease = True
        astr = event.key()
        self.keylist.append(astr)

    def keyReleaseEvent(self, event):
        if self.firstrelease == True:
            self.processmultikeys(self.keylist)

        self.firstrelease = False

        try:
            del self.keylist[-1]
        except:
            pass

    def mouseMoveEvent(self, event: QMouseEvent):
        # print(self.get_workspace_dimensions(event))
        # print(event)
        # self.get_workspace_dimensions(event)
        # print(event.windowPos(), self.ui.scrollArea.geometry())
        self.tool.draw(event)
        self.render()

    def mouseReleaseEvent(self, event):
        self.tool.reset_mouse_pos()
        self.tool.mousePressEvent(event)

        layer = self.get_layer()
        if layer:
            layer.image = self.translate(layer.image, layer.position)
            layer.position = [0, 0]

    def resizeEvent(self, event):
        final_button = [c.pos().y() for c in self.ui.toolbarWidget.findChildren(QPushButton)].pop()
        toolbar_size = self.ui.toolbarWidget.size()
        # print(event.size().height(), final_button + 69, toolbar_size.height() + 33)
        # print(self.label.pos())
        self.draw_rulers()

    # INITIALIZATION
    def initialize_document(self, new_file_information):
        # Background layer
        self.settings = {**new_file_information, **self.settings}
        # Checkboard
        checkerboard = Layer(
            image=self.generate_checkerboard(20),
            name='Checkerboard',
        )

        # Draw Grid
        # self.create_grid()

        # Background layer
        background = Layer()
        background.image = QPixmap(QSize(*new_file_information['absolute_dimensions']))
        background.image.fill(new_file_information['color'])
        background.name = 'Background'
        background.lock = True

        self.layers.append(checkerboard)
        self.layers.append(background)

    # SCRAP
    # SCRAP END

    # UTILITIES
    def create_grid(self):
        # Grid
        self.grid = Layer(
            image=self.draw_grid(20),
            name='Grid',
            mode='Multiply'
        )

    def processmultikeys(self, keyspressed):
        _keyspressed = [*keyspressed]
        _keyspressed.sort()
        command = '_'.join([str(k) for k in _keyspressed])
        name = key_mappings(command)

        print(command)

        if name == 'SWAP_SWATCHES':
            self.toolbar.color_swatches.flip_active()
            self.keylist = []
        elif name == 'GRID':
            if self.grid:
                self.grid = None
            else:
                self.grid = self.draw_grid()
        elif name == 'INVERT_IMAGE':
            if self.current_layer:
                pass
        # if name == 'NEW_FILE':
        #     # new_file_widget = NewFileWidget(
        #     #     self,
        #     #     save=self.new_file,
        #     # )
        #     # new_file_widget.setModal(True)
        #     # new_file_widget.show()
        #     print('NEW FILE')
        #     self.keylist = []
        # elif name == 'HIDE_RULERS':
        #     current_tab = self.ui.workspaceTabWidget.currentWidget()
        #     current_tab.toggle_rulers()
        # else:
        #     # self.on_toolbar_icon_click(name)
        #     self.keylist = []

    def draw_grid(self, grid_width=50):
        # TODO: Create layer for QLabel that is always present when document is open.
        # Replace all references to self.layers[0]
        if 'absolute_dimensions' in self.settings:
            [w, h] = self.settings['absolute_dimensions']
            [w_off, h_off] = self.settings['offset_dimensions']

            rows = int(h // grid_width)
            cols = int(w // grid_width)

            resultImage = QImage(QSize(*self.settings['absolute_dimensions']), QImage.Format_ARGB32_Premultiplied)
            resultImage.fill(Qt.transparent)
            painter = QPainter(resultImage)
            color = QColor(Qt.transparent)
            color.setAlphaF(0.15)
            painter.setPen(QPen(color, 0.5, Qt.SolidLine, Qt.RoundCap))

            for r in range(rows):
                if r % 4 == 0:
                    painter.setPen(QPen(color, 1, Qt.SolidLine, Qt.RoundCap))
                else:
                    painter.setPen(QPen(color, 0.5, Qt.SolidLine, Qt.RoundCap))
                painter.drawLine(0, r * grid_width + h_off, w, r * grid_width + h_off)

            for c in range(cols):
                if c % 4 == 0:
                    painter.setPen(QPen(color, 1, Qt.SolidLine, Qt.RoundCap))
                else:
                    painter.setPen(QPen(color, 0.5, Qt.SolidLine, Qt.RoundCap))
                painter.drawLine(c * grid_width + w_off, 0, c * grid_width + w_off, h)

            painter.end()

            return self.image_to_pixmap(resultImage)

    def generate_checkerboard(self, checker_width=50):
        dimensions = self.settings['absolute_dimensions']
        [w_off, h_off] = self.settings['offset_dimensions']
        grid_cnt = int(max(*dimensions) // checker_width)
        image = QImage(QSize(*dimensions), QImage.Format_ARGB32_Premultiplied)
        image.fill(Qt.white)
        painter = QPainter(image)
        color = QColor(Qt.black)
        color.setAlphaF(0.25)

        for i in range(grid_cnt):
            for j in range(grid_cnt):
                color = QColor(0, 0, 0, 30) if (i + j) % 2 != 0 else QColor(0, 0, 0, 0)
                painter.fillRect(QRect(
                    i * checker_width + w_off, j * checker_width + h_off,
                    checker_width, checker_width
                ), color)

        painter.end()

        return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)

    def get_workspace_dimensions(self, event: QMouseEvent):
        # TODO: define pos and size on resize event
        scroll_area_size = self.ui.scrollArea.size()
        scroll_area_point = self.ui.scrollArea.pos()
        self.scroll_area_size_pos = [*scroll_area_size, *scroll_area_point]
        # print(scroll_area_size, scroll_area_point)
        return [0, 0]
    
    # SIGNALS
    def update_tool_property(self, obj: dict):
        if obj['key'] == 'brush_color':
            self.tool.brush_color = obj['value']
        elif obj['key'] == 'opacity':
            self.tool.opacity = obj['value']

    def set_active_tool(self, tool):
        self.active_tool = tool

    def crop_workspace(self, image) -> QPixmap:
        if 'absolute_dimensions' in self.settings:
            artboard = QImage(QSize(*self.settings['absolute_dimensions']), QImage.Format_ARGB32_Premultiplied)
            painter = QPainter(artboard)
            painter.setCompositionMode(QPainter.CompositionMode_Source)
            painter.fillRect(
                QRect(
                    0,
                    0,
                    *self.settings['absolute_dimensions']
                ),
                Qt.transparent
            )

            # TODO: Move to new_file_information dict.
            document_dimensions = [*self.settings['absolute_dimensions']]
            document_dimensions[0] -= self.settings['offset_dimensions'][0] * 2
            document_dimensions[1] -= self.settings['offset_dimensions'][1] * 2
            painter.fillRect(QRect(
                    *self.settings['offset_dimensions'],
                    *document_dimensions,
                ),
                image
            )
            painter.end()

            return self.image_to_pixmap(artboard)
        return image

    def translate(self, image: QPixmap, position) -> QPixmap:
        resultImage = QImage(QSize(*self.settings['absolute_dimensions']), QImage.Format_ARGB32_Premultiplied)
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
        if hasattr(layer, 'mode'):
            mode = mode_mappings(layer.mode)
            resultImage = QImage(QSize(*self.settings['absolute_dimensions']), QImage.Format_ARGB32_Premultiplied)

            painter = QPainter(resultImage)
            # painter.setCompositionMode(QPainter.CompositionMode_Source)

            # Fill with background color
            painter.fillRect(resultImage.rect(), QColor('#101010'))

            # painter.scale(*layer.scale)
            # painter.translate(*layer.position)

            # painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
            painter.drawPixmap(0, 0, base_image)
            painter.setCompositionMode(mode)
            painter.drawPixmap(0, 0, layer.image)
            # painter.setCompositionMode(QPainter.CompositionMode_DestinationOver)
            # painter.fillRect(resultImage.rect(), Qt.transparent)
            painter.end()

            return self.image_to_pixmap(resultImage)
        else:
            return base_image

    def new_layer(self, layer):
        self.layers += [layer]
        self.set_current_layer(layer=layer.name)

    def delete_layer(self, layer_id: int):
        # TODO: Handle groups
        self.layers = [l for l in self.layers if l.layer_id != layer_id or l.lock]

    def update_layer_mode(self, layer_id: int, mode: str):
        layers = []
        for l in self.layers:
            if l.layer_id == layer_id:
                l.mode = mode
            layers.append(l)

        self.layers = layers      

    def lock_layer(self, layer_id):
        layers = []
        for l in self.layers:
            if l.layer_id == layer_id:
                l.lock = not l.lock
            layers.append(l)

        self.layers = layers

    def hide_layer(self, layer_id):
        layers = []
        for l in self.layers:
            if l.layer_id == layer_id:
                l.show = not l.show
            layers.append(l)

        self.layers = layers

    def get_layer(self) -> Layer:
        # TODO: Change current_layer to a unique ID
        layer = None

        for l in self.layers:
            if l.name == self.current_layer:
                layer = l
                break

        return layer

    def set_current_layer(self, layer):
        self.current_layer = layer
        # print('480 layer', layer)
        self.windows['layers_widget'].current_layer = self.current_layer

    def render_layers(self):
        if self.layers:
            composite = self.layers[0].image

            for i in range(len(self.layers)):
                if self.layers[i].show:
                    if isinstance(self.layers[i], LayerGroup):
                        child_count = len(self.layers[i].children)
                        group_composite = self.layers[i].children[0].image

                        if child_count > 1:
                            for j in (range(child_count)):
                                group_composite = self.def_add_image(group_composite, self.layers[i].children[j])

                        self.layers[i].image = group_composite

                    composite = self.def_add_image(composite, self.layers[i])

            return composite

    def image_to_pixmap(self, image) -> QPixmap:
        # TODO: Utility
        return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)

    # WINDOW PANELS
    def generate_window_panels(self):
        layers_widget = LayersWindowWidget(
            signaler=self.signaler,
            settings=self.settings,
            current_layer=self.current_layer,
            layers=self.layers
        )

        layers_widget.setMouseTracking(True)
        self.windows['layers_widget'] = layers_widget

        self.ui.windowsWidget.layout().addChildWidget(self.windows['layers_widget'])

    # RULERS
    def draw_rulers(self):
        [x, y] = self.label.pos().toTuple()
        [w_offset, h_offset] = self.settings['offset_dimensions']
        w = self.label.rect().width()
        h = self.label.rect().height()

        width_to_label = x + w_offset
        height_to_label = y + h_offset

        full_width = width_to_label + w
        full_height = h + height_to_label
        # print(full_width, full_height)

        for i in range(full_width):
            if i % 50 == 0:
                # print(pixel_to_inch(i - width_to_label))
                pass
    # def draw_rulers(self):
    #     # TODO: Extend entire length/height of application
    #     self.draw_v_ruler()
    #     self.draw_h_ruler()

    # def draw_h_ruler(self):
    #     ruler_dimensions = self.settings['absolute_dimensions']
    #     for i in range(int(ruler_dimensions[0] // 100)):
    #         # self.draw_v_unit(i - self.settings['workspace_spillover'], inch_to_pixel(i))
    #         self.draw_h_unit(i - (self.settings['offset_dimensions'][1] // 100), i * 100)

    # def draw_h_unit(self, index, h_offset=0):
    #     # TODO: create dynamically
    #     inch_ticks = [
    #         16, 14, 16, 0
    #     ]
    #     label = QLabel(self.ui.horizontalRulerWidget)
    #     label.setText(str(index))
    #     label.move(h_offset + 4, -6)
    #     tick_width = 94 / len(inch_ticks)

    #     for i, v_offset in enumerate(inch_ticks):
    #         line = QVLine(self.ui.horizontalRulerWidget, 20 - v_offset)
    #         line.move(((i + 1) * tick_width + h_offset) * (self.zoom/100.0), v_offset)

    # def draw_v_unit(self, index, v_offset=0):
    #     # TODO: create dynamically
    #     inch_ticks = [
    #         16, 14, 16, 0
    #     ]
    #     label = QLabel(self.ui.verticalRulerWidget)
    #     label.setText(str(index))
    #     label.move(4, v_offset - 6)
    #     tick_height = 94 / len(inch_ticks)

    #     for i, h_offset in enumerate(inch_ticks):
    #         line = QHLine(self.ui.verticalRulerWidget, 20 - h_offset)
    #         line.move(h_offset, ((i + 1) * tick_height + v_offset) * (self.zoom/100.0))

    # def draw_v_ruler(self):
    #     ruler_group = range(self.ui.verticalRulerWidget.layout().count())
    #     ruler_dimensions = self.settings['absolute_dimensions']

    #     for widget_index in ruler_group:
    #         widget = self.ui.verticalRulerWidget.layout().itemAt(
    #             widget_index).widget()
    #         if widget:
    #             widget.setParent(None)

    #     # Pixel to mm
    #     # TODO: Make versatile
    #     # TODO: Fix lines
    #     for i in range(int(ruler_dimensions[1] // 100)):
    #         # print(self.zoom, type(self.zoom))
    #         # self.draw_v_unit(i - self.settings['offset_dimensions'][0], i)
    #         self.draw_v_unit(i - (self.settings['offset_dimensions'][0] // 100), i * 100)

    # MAIN RENDER
    def render(self):
        # res = self.render_layers()
        # res = self.crop_workspace(res)

        # if self.grid:
        #     res = self.def_add_image(res, self.grid)

        # if res:
        #     self.label.setPixmap(res)
        self.label.setPixmap(self.artboard.render())


def main():
    app = QApplication(sys.argv)

    # Get and set DPI
    dpi = app.screens()[0].physicalDotsPerInch()
    set_dpi(dpi)

    settings_window = MainWindow()
    settings_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()