from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QSize, QPoint, QRect
from PySide6.QtWidgets import QWidget, QMainWindow, QGraphicsScene, QGraphicsItemGroup, QVBoxLayout, QDockWidget, QFrame, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtGui import QIcon, QPixmap, QColor, QPainter, QPen, QImage

from datatypes.layer import Layer, modes, mode_mappings, GraphicsRectItemBase
from styles.window_panel import window_panel_style
from ui.windows import layerswindowui
from widgets.windows.layer import LayerWidget
from widgets.windows.layergroup import LayerGroupWidget


# SIGNALS
class LayerSignaler(QtCore.QObject):
    update_selected_layer = QtCore.Signal()
    hide_layer = QtCore.Signal(int)


class LayersWindowWidget(QWidget):
    def __init__(
            self,
            layers: QGraphicsScene,
            current_layer,
            settings,
            signaler=None
        ):
        super().__init__()
        self.ui = layerswindowui.Ui_LayersWindow()
        self.ui.setupUi(self)

        self.signaler = LayerSignaler()
        self.main_signaler = signaler
        self.layers = layers
        self.current_layer = current_layer
        self.settings = settings

        # Signals
        self.signaler.update_selected_layer.connect(self.update_selected_layer)
        self.signaler.hide_layer.connect(self.hide_layer)

        # Clicks
        self.ui.newLayerPushButton.clicked.connect(self.new_layer)
        self.ui.deleteLayerPushButton.clicked.connect(self.delete_layer)
        self.ui.layerLockPushButton.clicked.connect(self.lock_layer)
        self.ui.modeComboBox.currentTextChanged.connect(self.update_layer_mode)

        # UI
        self.ui.modeComboBox.addItems(modes())
        self.ui.modeComboBox.insertSeparator(2)
        self.ui.modeComboBox.insertSeparator(8)
        self.ui.modeComboBox.insertSeparator(14)
        self.ui.modeComboBox.insertSeparator(19)
        self.ui.modeComboBox.insertSeparator(24)
        self.ui.modeComboBox.insertSeparator(29)

        self.render_layers()

        self.setStyleSheet("""
            QComboBox {
                background: rgba(0, 0, 0, .2);
            }

    QScrollBar:vertical
    {

        background-color: pink;
        width: 15px;CompositionMode
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

    @property
    def current_layer(self):
        return self._current_layer

    @current_layer.setter
    def current_layer(self, current_layer):
        self._current_layer = current_layer
        layer = self.get_layer()
        if layer:
            self.update_layer_mode(layer.mode)
        # print(self.current_layer)

    def update_selected_layer(self):
        self.update_layers_selected()

    def new_layer(self):
        layer = Layer()
        layer.image = QPixmap(QSize(*self.settings['absolute_dimensions']))
        layer.image.fill(QColor(255, 255, 0, 100))
        self.main_signaler.new_layer.emit(layer)

    def get_layer(self) -> LayerWidget:
        return self.ui.scrollAreaWidgetContents.findChild(LayerWidget, self.current_layer)

    def image_to_pixmap(self, image) -> QPixmap:
        # TODO: Move this into a utils
        return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)

    def merge_images(self, image_1, image_2, mode: str='Normal'):
        # TODO: Move this into a utils
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
                color = QColor(0, 0, 0, 30) if (i + j) % 2 != 0 else QColor(0, 0, 0, 0)
                painter.fillRect(QRect(
                    i * checker_width, j * checker_width,
                    checker_width, checker_width
                ), color)

        painter.end()

        return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)

    def update_layers_selected(self):
        for child in self.ui.scrollAreaWidgetContents.findChildren(LayerWidget):
            child.selected(child.objectName == self.current_layer)

    def delete_layer(self):
        layer = self.get_layer()
        self.main_signaler.delete_layer.emit(layer.layer_id)
        layer.setParent(None)
        self.current_layer = None

    def hide_layer(self, layer_id):
        self.main_signaler.hide_layer.emit(layer_id)

    def update_layer_mode(self, mode=None):
        layer = self.get_layer()
        if layer and mode:
            self.ui.modeComboBox.setCurrentText(mode)
            self.main_signaler.update_layer_mode.emit(layer.layer_id, mode)

    def lock_layer(self):
        layer = self.get_layer()
        self.main_signaler.lock_layer.emit(layer.layer_id)

    def lock_layer_ui(self, layer):
        lock = QIcon('images/window_lock.svg').pixmap(QSize(12, 12))
        layer.ui.lockLabel.setPixmap(lock)

    def render_layers(self, index=0):
        # Remove all existing layers from layout
        for child in self.ui.scrollAreaWidgetContents.findChildren(LayerWidget):
            child.setParent(None)

        # Add all layers to layout
        for item in self.layers.items(Qt.AscendingOrder):
            # print(item)
            if isinstance(item, GraphicsRectItemBase):
            #     print('GROUP', item, id(item))
            # else:
                # print('ITEM', id(item))
            # for l in self.layers[1:]:
                layer = LayerWidget(
                    parent=self.ui.verticalLayout_3.widget(),
                    main_signaler=self.main_signaler,
                    layer_signaler=self.signaler,
                    layer_id=id(item),
                    layer={
                        'is_selected': False,
                        'hidden': False,
                        'name': item.name,
                        'mode': item.mode
                    }
                )
                layer.setObjectName(item.name)
                self.ui.verticalLayout_3.insertWidget(index, layer)

                # Thumbnails
                if self.settings['aspect_ratio'][0] < self.settings['aspect_ratio'][1]:
                    layer.ui.thumbnailWidget.setFixedWidth(36 * self.settings['aspect_ratio'][0])
                else:
                    layer.ui.thumbnailWidget.setFixedHeight(36 * self.settings['aspect_ratio'][1])

                # Lock UI
                # if l.lock:
                #     self.lock_layer_ui(layer)

                # Add thumbnail to thumbnailwidget
                # self.layers.sceneRect
                # print(self.layers.sceneRect().size().toSize())
                pixmap = item.to_pixmap(self.layers.sceneRect().size().toSize())
                # pixmap.fill(Qt.white)
                thumb = QLabel(layer.ui.thumbnailWidget)
                thumb.setPixmap(self.merge_images(self.generate_checkerboard(dimensions=self.settings['document_dimensions']), pixmap))

