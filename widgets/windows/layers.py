from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QSize, QPoint, QRect
from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QDockWidget, QFrame, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtGui import QIcon, QPixmap, QColor, QPainter, QPen, QImage

from datatypes.layer import Layer
from styles.window_panel import window_panel_style
from ui.windows import layerswindowui
from widgets.windows.layer import LayerWidget
from widgets.windows.layergroup import LayerGroupWidget


class LayersWindowWidget(QWidget):
    def __init__(
            self,
            layers,
            settings,
            signaler=None
        ):
        super().__init__()
        self.ui = layerswindowui.Ui_LayersWindow()
        self.ui.setupUi(self)

        self.main_signaler = signaler
        self.layers = layers
        self.settings = settings

        self.ui.newLayerPushButton.clicked.connect(self.new_layer)
        self.update_layers()

        self.setStyleSheet("""
            QComboBox {
                background: rgba(0, 0, 0, .2);
            }

    QScrollBar:vertical
    {

        background-color: pink;
        width: 15px;
        margin: 15px 3px 15px 3px;
        border: 1px transparent #2A2929;
        border-radius: 4px;
    }

    QScrollBar::handle:vertical
    {
        background-color: rgba(255, 255, 255, .5);
        min-height: 5px;
        border-radius: 2px;
    }

    QScrollBar::sub-line:vertical
    {
        border-radius: 2px;
        border-image: url(:/qss_icons/rc/up_arrow_disabled.png);
        height: 10px;
        width: 10px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }

    QScrollBar::add-line:vertical
    {
        margin: 3px 0px 3px 0px;
        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);
        height: 10px;
        width: 10px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }

    QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on
    {
        border-image: url(:/qss_icons/rc/up_arrow.png);
        height: 10px;
        width: 10px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }

    QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on
    {
        border-image: url(:/qss_icons/rc/down_arrow.png);
        height: 10px;
        width: 10px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
        background-color: pink;
    }

    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
    {
        background: rgba(255, 255, 255, .2);
        border-radius: 2px;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
    {
        background: none;
    }

        """)

    def new_layer(self):
        layer = Layer()
        layer.image = QPixmap(QSize(*self.settings['absolute_dimensions']))
        layer.image.fill(QColor(255, 255, 0, 100))
        self.main_signaler.new_layer.emit(layer)

    def image_to_pixmap(self, image) -> QPixmap:
        return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)

    def merge_images(self, image_1, image_2, mode: str='Normal'):
        mode = QPainter.CompositionMode.CompositionMode_SourceOver

        resultImage = QImage(QSize(*self.settings['absolute_dimensions']), QImage.Format_ARGB32_Premultiplied)
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

    def generate_checkerboard(self, dimensions=[0, 0], checker_width=5, grid_cnt=10):
        image = QImage(QSize(*dimensions), QImage.Format_ARGB32_Premultiplied)
        image.fill(Qt.white)
        painter = QPainter(image)
        color = QColor(Qt.black)
        color.setAlphaF(0.5)

        for i in range(grid_cnt):
            for j in range(grid_cnt):
                color = QColor(0, 0, 0, 100) if (i + j) % 2 != 0 else QColor(0, 0, 0, 0)
                painter.fillRect(QRect(
                    i * checker_width, j * checker_width,
                    checker_width, checker_width
                ), color)

        painter.end()

        return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)

    def update_layers(self, index=0):
        # Remove all existing layers from layout
        for child in self.ui.scrollAreaWidgetContents.findChildren(LayerWidget):
            child.setParent(None)

        # Add all layers to layout
        for l in self.layers:
            layer = LayerWidget(parent=self.ui.verticalLayout_3.widget(), layer={'is_selected': False, 'hidden': False, 'name': l.name})

            if self.settings['aspect_ratio'][0] < self.settings['aspect_ratio'][1]:
                layer.ui.thumbnailWidget.setFixedWidth(32 * self.settings['aspect_ratio'][0])
            else:
                layer.ui.thumbnailWidget.setFixedHeight(32 * self.settings['aspect_ratio'][1])

            # Add thumbnail to thumbnailwidget
            thumb = QLabel(layer.ui.thumbnailWidget)
            thumb.setPixmap(self.merge_images(self.generate_checkerboard(dimensions=self.settings['document_dimensions']), l.image))
            self.ui.verticalLayout_3.insertWidget(index, layer)
