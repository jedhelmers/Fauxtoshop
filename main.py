import json
import random
import sys
from pathlib import Path

from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, Qt, QEvent, QPoint, QObject, QCoreApplication, QRect
from PySide6.QtGui import QIcon, QPixmap, QImage, QPainter, QColor, QMouseEvent, qRgba
from PySide6.QtWidgets import QMainWindow, QFrame, QApplication, QTableWidgetItem, QPushButton, QWidget, QGridLayout, QLabel

from datas.tools import get_tool_icon
from datatypes.layer import Layer, LayerGroup, mode_mappings
from styles.main import main_style
from ui import mainwindow_newui
from widgets.toolbar import ToolbarWidget
from widgets.windows.layers import LayersWindowWidget
from workspace import WorkspaceWidget


# RULER LINES
# Create a Ruler class to handle all this.
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


class Tool(QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self._layer = None
        self.brush_color = qRgba(50, 50, 50, 50)
        self.brush_size = 20
        self.last_x = None
        self.last_y = None
        self.drag_speed  = 1.0
        self.down_mouse_pos = [0, 0]
        self.up_mouse_pos = [0, 0]
        self.snap_to = 30 # CANNOT BE ZERO

    @property
    def active_tool(self):
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
        print('self.layer')
        if self.layer and self.layer.image:
            # TODO: why is self.layer None?
            print('brush')
            [x_offset, y_offset] = self.layer.position

            x = event.position().x() * self.drag_speed - x_offset
            y = event.position().y() * self.drag_speed - y_offset

            if self.last_x is None: # First event.
                self.last_x = x
                self.last_y = y

                return # Ignore the first time.

            resultImage = QImage(self.layer.image.size(), QImage.Format_ARGB32_Premultiplied)
            painter = QPainter(resultImage)
            painter.setCompositionMode(QPainter.CompositionMode_Source)
            painter.fillRect(resultImage.rect(), Qt.transparent)

            pen = QtGui.QPen()
            pen.setWidth(self.brush_size)
            pen.setColor(self.brush_color)
            pen.setStyle(Qt.SolidLine)
            pen.setCapStyle(Qt.RoundCap)
            pen.setCosmetic(True)
            painter.setPen(pen)
            painter.fillRect(resultImage.rect(), Qt.transparent)
            painter.drawPixmap(0, 0, self.layer.image)
            painter.setCompositionMode(self._mode)
            painter.drawLine(self.last_x, self.last_y, x, y)
            painter.end()

            self.last_x = x
            self.last_y = y

            self.layer.image = self.image_to_pixmap(resultImage)

# SIGNALS
class MainSignaler(QtCore.QObject):
    new_layer = QtCore.Signal(Layer)
    delete_layer = QtCore.Signal(int)
    lock_layer = QtCore.Signal(int)
    hide_layer = QtCore.Signal(int)
    update_layer_mode = QtCore.Signal(int, str)
    set_current_layer = QtCore.Signal(str)
    set_active_tool = QtCore.Signal(str)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # SETUP
        self.ui = mainwindow_newui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.signaler = MainSignaler()
        self.settings = {}
        self.setStyleSheet(main_style())

        # Ruler
        self.x_line = QVLine(self.ui.horizontalRulerWidget, thickness=2)
        self.y_line = QHLine(self.ui.verticalRulerWidget, thickness=2)
        self.x_line.setStyleSheet('border-color: rgba(255, 255, 255, 0.75)')
        self.y_line.setStyleSheet('border-color: rgba(255, 255, 255, 0.75)')

        # UI
        self.label = QLabel()
        self.label.setMouseTracking(True)
        self.ui.gridLayout_3.addWidget(self.label)
        self.ui.gridLayout_3.setAlignment(Qt.AlignTop)
        self.zoom = 1.0
        self.scroll_area_size_pos = [0, 0, 0, 0]

        # Windows
        self.windows = {}

        # Tools
        self.tool = Tool(self)
        self.tool.setMouseTracking(True)
        self.tool.active_tool = 'brush'
        toolbar = ToolbarWidget(
            main_signaler=self.signaler,
            tool=self.tool
        )
        self.ui.toolbarWidget.layout().addWidget(toolbar)

        # DATA
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

        # TEMP
        document_dimensions = [500, 700]
        offset_dimensions = [200, 200]
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
        # TODO: Initial scroll
        self.ui.scrollArea.scroll(300, 300)

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
        print('layer', layer)
        self.tool.layer = layer

    @property
    def active_tool(self):
        return self._active_tool

    @active_tool.setter
    def active_tool(self, active_tool):
        self._active_tool = active_tool
        self.tool.active_tool = self.active_tool

    # Overrides
    def mouseMoveEvent(self, event: QMouseEvent):
        # print(self.get_workspace_dimensions(event))
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
        print(event.size().height(), final_button + 69, toolbar_size.height() + 33)

    # INITIALIZATION
    def initialize_document(self, new_file_information):
        # Background layer
        self.settings = {**new_file_information, **self.settings}
        background = Layer()
        background.image = QPixmap(QSize(*new_file_information['absolute_dimensions']))
        background.image.fill(new_file_information['color'])
        background.name = 'Background'
        background.lock = True

        self.layers.append(background)

    # SCRAP
    # SCRAP END

    # UTILITIES
    def get_workspace_dimensions(self, event: QMouseEvent):
        # TODO: define pos and size on resize event
        scroll_area_size = self.ui.scrollArea.size()
        scroll_area_point = self.ui.scrollArea.pos()
        self.scroll_area_size_pos = [*scroll_area_size, *scroll_area_point]
        # print(scroll_area_size, scroll_area_point)
        return [0, 0]

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
                QColor(20, 24, 30, 100)
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
        mode = mode_mappings(layer.mode)

        resultImage = QImage(QSize(*self.settings['absolute_dimensions']), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(resultImage)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.fillRect(resultImage.rect(), Qt.transparent)

        # painter.scale(*layer.scale)
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
        print('480 layer', layer)
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
        # TODO: Extend entire length/height of application
        self.draw_v_ruler()
        self.draw_h_ruler()

    def draw_h_ruler(self):
        ruler_dimensions = self.settings['absolute_dimensions']
        for i in range(int(ruler_dimensions[0] // 100)):
            # self.draw_v_unit(i - self.settings['workspace_spillover'], inch_to_pixel(i))
            self.draw_h_unit(i - (self.settings['offset_dimensions'][1] // 100), i * 100)

    def draw_h_unit(self, index, h_offset=0):
        # TODO: create dynamically
        inch_ticks = [
            16, 14, 16, 0
        ]
        label = QLabel(self.ui.horizontalRulerWidget)
        label.setText(str(index))
        label.move(h_offset + 4, -6)
        tick_width = 94 / len(inch_ticks)

        for i, v_offset in enumerate(inch_ticks):
            line = QVLine(self.ui.horizontalRulerWidget, 20 - v_offset)
            line.move(((i + 1) * tick_width + h_offset) * (self.zoom/100.0), v_offset)

    def draw_v_unit(self, index, v_offset=0):
        # TODO: create dynamically
        inch_ticks = [
            16, 14, 16, 0
        ]
        label = QLabel(self.ui.verticalRulerWidget)
        label.setText(str(index))
        label.move(4, v_offset - 6)
        tick_height = 94 / len(inch_ticks)

        for i, h_offset in enumerate(inch_ticks):
            line = QHLine(self.ui.verticalRulerWidget, 20 - h_offset)
            line.move(h_offset, ((i + 1) * tick_height + v_offset) * (self.zoom/100.0))

    def draw_v_ruler(self):
        ruler_group = range(self.ui.verticalRulerWidget.layout().count())
        ruler_dimensions = self.settings['absolute_dimensions']

        for widget_index in ruler_group:
            widget = self.ui.verticalRulerWidget.layout().itemAt(
                widget_index).widget()
            if widget:
                widget.setParent(None)

        # Pixel to mm
        # TODO: Make versatile
        # TODO: Fix lines
        for i in range(int(ruler_dimensions[1] // 100)):
            # print(self.zoom, type(self.zoom))
            # self.draw_v_unit(i - self.settings['offset_dimensions'][0], i)
            self.draw_v_unit(i - (self.settings['offset_dimensions'][0] // 100), i * 100)

    # MAIN RENDER
    def render(self):
        res = self.render_layers()
        res = self.crop_workspace(res)
        if res:
            self.label.setPixmap(res)

def main():
    app = QApplication(sys.argv)
    settings_window = MainWindow()
    settings_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()