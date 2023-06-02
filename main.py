import json
import random
import sys
from pathlib import Path
from typing import Optional

from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, Qt, QEvent, QPoint, QObject, QCoreApplication, QRect
from PySide6.QtGui import QIcon, QPixmap, QImage, QPainter, QColor, QMouseEvent, qRgba, QPen, QBrush
from PySide6.QtWidgets import QMainWindow, QFrame, QGraphicsView, QGraphicsItemGroup, QStyle, QStyleOptionGraphicsItem, QGraphicsRectItem, QGraphicsItem, QApplication, QTableWidgetItem, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QPushButton, QWidget, QGridLayout, QLabel

from datas.tools import get_tool_icon
from datatypes.layer import Layer, LayerGroup, ArtBoardView, ArtBoard, LayerBase, GraphicsItemBase, GraphicsRectItemBase, GraphicsPixmapItem, mode_mappings
from datatypes.utils import QHLine, QVLine
from styles.main import main_style
from ui import mainwindow_newui
from widgets.toolbar import ToolbarWidget
from widgets.windows.layers import LayersWindowWidget
from workspace import WorkspaceWidget


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
        self._layer = layer
        # TODO: Brush mode
        self._mode = mode_mappings(layer.mode) if layer else None

    def graphics_scene(self):
        scene = QGraphicsScene(self.parent())
        pixmap = QPixmap(QSize(400, 400))
        pixmap.fill(qRgba(250, 50, 50, 50))
        item = QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        return scene

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
        if self.layer and self.layer.image:
            # TODO: why is self.layer None?
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

            pen = QPen()
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

        # TEMP
        document_dimensions = [800, 500]
        offset_dimensions = [100, 100]
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

        # Ruler
        self.x_line = QVLine(self.ui.horizontalRulerWidget, thickness=2)
        self.y_line = QHLine(self.ui.verticalRulerWidget, thickness=2)
        self.x_line.setStyleSheet('border-color: rgba(255, 255, 255, 0.75)')
        self.y_line.setStyleSheet('border-color: rgba(255, 255, 255, 0.75)')

        # UI
        self.label = QLabel()
        self.label.setMouseTracking(True)
        ArtBoard.settings = self.settings
        self.scene = ArtBoard()
        self.scene.setBackgroundBrush(QBrush(QColor(30, 30, 30)))
        ArtBoardView.settings = self.settings
        self.view = ArtBoardView(self.scene)
        # self.scene.setSceneRect(0, 0, 100, 200)
        # self.view.setMask(QRect(50, 50, 400, 400))

        # Prevent scene from scrolling
        self.scene.setSceneRect(self.view.rect())

        self.ui.gridLayout_3.addChildWidget(self.view)

        self.ui.gridLayout_3.setAlignment(Qt.AlignHCenter)

        self.zoom = 1.0
        self.scroll_area_size_pos = [0, 0, 0, 0]

        # Grid
        self.grid = None

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
        # self.signaler.new_layer.connect(self.new_layer)
        # self.signaler.set_current_layer.connect(self.set_current_layer)
        # self.signaler.delete_layer.connect(self.delete_layer)
        # self.signaler.lock_layer.connect(self.lock_layer)
        # self.signaler.hide_layer.connect(self.hide_layer)
        # self.signaler.update_layer_mode.connect(self.update_layer_mode)
        # self.signaler.set_active_tool.connect(self.set_active_tool)


        self.generate_window_panels()

        # Initialize
        # self.scene.setSceneRect(
        #     QRect(0, 0,
        #           *new_file_information['document_dimensions']
        #     )
        # )

        # self.view.setMask(
        #     QRect(0,0,
        #           *new_file_information['document_dimensions'])
        # )

        # self.scene.clip

        # checkboard = GraphicsPixmapItem('Checkboard', 'Normal')
        # #
        # checkboard.setPos(0, 0)
        # checkboard.setPixmap(self.generate_checkerboard())
        # checkboard.setFlag(QGraphicsItem.ItemIsMovable, False)
        # checkboard.setFlag(QGraphicsItem.ItemIsSelectable, False)
        # self.scene.addItem(checkboard)

        # Set scene dimensions
        # self.view.setSceneRect(0, 0, *self.settings['document_dimensions'])
        # self.view.setFixedSize(QSize(*self.settings['document_dimensions']))
        print('MAX SIZE', self.ui.widget.size())
        # self.view.setFixedSize(QSize(502, 702))
        # self.view.setFixedSize(1000, 1000)
        # self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
        self.view.setFixedSize(self.ui.widget.size())
        # self.ui.widget.setFixedSize(1000, 1000)
        # self.ui.gridLayout_3.setGeometry(QRect(0, 0, 1000, 1000))
        # self.view.setEnabled(False)

        # Render
        self.adjust_artboard()
        self.render()

        # TODO: Initial scroll
        # self.ui.scrollArea.scroll(300, 300)

    @property
    def layers(self):
        return self._layers

    @layers.setter
    def layers(self, layers):
        self._layers = layers
        # self.render()

        # TODO: Handle this better
        if 'layers_widget'  in self.windows:
            self.windows['layers_widget'].layers = self.layers
            self.windows['layers_widget'].render_layers()

    @property
    def current_layer(self):
        return self._current_layer

    @current_layer.setter
    def current_layer(self, current_layer):
        self._current_layer = current_layer

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
        # self.render()

    def mouseReleaseEvent(self, event):
        self.tool.reset_mouse_pos()
        self.tool.mousePressEvent(event)

    def resizeEvent(self, event):
        final_button = [c.pos().y() for c in self.ui.toolbarWidget.findChildren(QPushButton)].pop()
        toolbar_size = self.ui.toolbarWidget.size()
        print(event.size().height(), final_button + 69, toolbar_size.height() + 33)

        self.adjust_artboard()

    # INITIALIZATION
    def initialize_document(self, new_file_information):
        # Background layer
        self.settings = {**new_file_information, **self.settings}
        GraphicsItemBase.settings = self.settings
        # Checkboard
        # checkerboard = Layer(
        #     image=self.generate_checkerboard(20),
        #     name='Checkerboard',
        # )

        # Grid
        self.grid = Layer(
            image=self.draw_grid(20),
            name='Grid',
            mode='Multiply'
        )

        # Background layer
        # background = Layer()
        # background.image = QPixmap(QSize(*new_file_information['document_dimensions']))
        # background.image.fill(new_file_information['color'])
        # background.name = 'Background'
        # background.lock = True

        # self.layers.append(checkerboard)
        # self.layers.append(background)

    # SCRAP
    # SCRAP END

    # UTILITIES
    def adjust_artboard(self):
        # Adjust graphics view on window resize
        self.view.setFixedSize(self.ui.widget.size())

    def image_to_pixmap(self, image) -> QPixmap:
        # TODO: Utility
        return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)

    def draw_grid(self, grid_width=50):
        # TODO: Create layer for QLabel that is always present when document is open.
        # Replace all references to self.layers[0]
        if self.settings:
            [w, h] = self.settings['document_dimensions']

            rows = int(h // grid_width)
            cols = int(w // grid_width)

            resultImage = QImage(QSize(*self.settings['document_dimensions']), QImage.Format_ARGB32_Premultiplied)
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
                painter.drawLine(0, r * grid_width, w, r * grid_width)

            for c in range(cols):
                if c % 4 == 0:
                    painter.setPen(QPen(color, 1, Qt.SolidLine, Qt.RoundCap))
                else:
                    painter.setPen(QPen(color, 0.5, Qt.SolidLine, Qt.RoundCap))
                painter.drawLine(c * grid_width, 0, c * grid_width, h)

            painter.end()

            return self.image_to_pixmap(resultImage)
        return QPixmap()
    # def generate_checkerboard(self, checker_width=50) -> QPixmap:
    #     dimensions = self.settings['document_dimensions']
    #     print(dimensions)
    #     grid_cnt = int(max(*dimensions) // checker_width)
    #     image = QImage(QSize(*dimensions), QImage.Format_ARGB32_Premultiplied)
    #     image.fill(Qt.white)
    #     painter = QPainter(image)
    #     color = QColor(Qt.black)
    #     color.setAlphaF(0.25)

    #     for i in range(grid_cnt):
    #         for j in range(grid_cnt):
    #             color = QColor(0, 0, 0, 30) if (i + j) % 2 != 0 else QColor(0, 0, 0, 0)
    #             painter.fillRect(QRect(
    #                 i * checker_width, j * checker_width,
    #                 checker_width, checker_width
    #             ), color)

    #     painter.end()

    #     return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)

    # WINDOW PANELS
    def generate_window_panels(self):
        layers_widget = LayersWindowWidget(
            signaler=self.signaler,
            settings=self.settings,
            current_layer=self.current_layer,
            layers=self.scene
        )

        layers_widget.setMouseTracking(True)
        self.windows['layers_widget'] = layers_widget

        self.ui.windowsWidget.layout().addChildWidget(self.windows['layers_widget'])

    # RULERS

    # MAIN RENDER
    def render(self):
        # Create rect

        brush = QBrush(QColor(255, 255, 255))
        rect0 = GraphicsRectItemBase('Layer 0', 'Normal', 0, 0, 200, 50)
        # rect0.setRotation(45.0)
        brush = QBrush(QColor(10, 255, 10, 255))
        rect0.setPen(Qt.NoPen)
        rect0.setBrush(brush)

        pix = GraphicsPixmapItem('mask', 'Normal')
        p = QPixmap("images/brush.svg")
        # painter = QPainter(p)
        # painter.drawPixmap(0, 0, QPixmap("images/window_link.svg"))
        # painter.setCompositionMode(mode_mappings('DestinationIn'))
        # painter.end()
        # p.fill(Qt.red)
        pix.setPixmap(p)
        pix.setScale(0.5)
        self.scene.addItem(pix)
        self.scene.addItem(rect0)

        pix.index = 1.0

        group = QGraphicsItemGroup()
        rect = GraphicsRectItemBase('Layer 1', 'Normal', 0, 0, 100, 100)
        rect.setBrush(QBrush(QColor(50, 50, 50, 200)))
        # group.addToGroup(rect)
        self.scene.addItem(rect)

        for item in group.childItems():
            print(type(item), item.group())

        print('\n')
        for item in self.scene.items():
            print(type(item))


def main():
    app = QApplication(sys.argv)
    settings_window = MainWindow()
    settings_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
