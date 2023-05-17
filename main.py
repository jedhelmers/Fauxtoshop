import json
import random
import sys
from pathlib import Path
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, Qt, QEvent, QPoint, QObject, QCoreApplication, QRect
from PySide6.QtGui import QIcon, QPixmap, QImage, QPainter, QColor
from PySide6.QtWidgets import QMainWindow, QFrame, QApplication, QTableWidgetItem, QPushButton, QWidget, QGridLayout, QLabel

from datatypes.layer import Layer, LayerGroup, mode_mappings
from styles.main import main_style
from ui import mainwindow_newui
from workspace import WorkspaceWidget
from widgets.windows.layers import LayersWindowWidget


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


# SIGNALS
class MainSignaler(QtCore.QObject):
    new_layer = QtCore.Signal(Layer)
    set_current_layer = QtCore.Signal(Layer)


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
        self.ui.gridLayout_3.addWidget(self.label)
        self.ui.gridLayout_3.setAlignment(Qt.AlignTop)
        self.zoom = 1.0

        # Windows
        self.windows = {}

        # DATA
        self.layers = []
        self.current_layer = None

        # Signals
        self.signaler.new_layer.connect(self.new_layer)
        self.signaler.set_current_layer.connect(self.set_current_layer)

        # TEMP
        document_dimensions = [1800, 1600]
        offset_dimensions = [300, 300]
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
            self.windows['layers_widget'].update_layers()

    # INITIALIZATION
    def initialize_document(self, new_file_information):
        # Background layer
        self.settings = {**new_file_information, **self.settings}
        background = Layer()
        background.image = QPixmap(QSize(*new_file_information['absolute_dimensions']))
        background.image.fill(new_file_information['color'])
        background.name = 'Background'

        self.layers.append(background)

    # SCRAP
    # SCRAP END

    # UTILITIES
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
                QColor(0, 245, 255, 100)
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

    def def_add_image(self, base_image: QPixmap=None, layer: Layer=None) -> QPixmap:
        mode = mode_mappings(layer.mode)

        resultImage = QImage(QSize(*self.settings['absolute_dimensions']), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(resultImage)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.fillRect(resultImage.rect(), Qt.transparent)

        # painter.scale(*layer.scale)
        # painter.translate(*layer.position)

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

    def set_current_layer(self, layer):
        self.current_layer = layer
        self.windows['layers_widget'].current_layer = self.current_layer

    def render_layers(self):
        if self.layers:
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

    def image_to_pixmap(self, image) -> QPixmap:
        return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)

    # WINDOW PANELS
    def generate_window_panels(self):
        layers_widget = LayersWindowWidget(
            signaler=self.signaler,
            settings=self.settings,
            current_layer=self.current_layer,
            layers=self.layers
        )

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