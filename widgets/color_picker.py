from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import Qt, QLinearGradient, QGradient, QColor, QBrush, QMouseEvent, QPixmap, QPainter, QImage
from PySide6.QtWidgets import QDialog, QGraphicsItem, QGraphicsEllipseItem, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem

from styles.window_panel import window_panel_style
from ui.color_pickerui import Ui_ColorPicker


class ColorPaletteSelectionEllipseItem(QGraphicsEllipseItem):
    def __init__(self):
        super().__init__()

        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        # self.setFlag(QGraphicsItem.ItemIsSelectable, True)

        self.setRect(20, 20, 10, 10)
        self.setBrush(Qt.white)
        print(self.scene())
        # for item in self.scene().items():
        #     print(type(item))

    def mousePressEvent(self, event: QMouseEvent) -> None:
        # print('ITEM', event.pos().x(), event.pos().y())
        # color = self.pixmap().toImage().pixelColor(event.pos().x(), event.pos().y()).toRgb()
        # print(color)
        return super().mousePressEvent(event)


class ColorPalettePixmapItem(QGraphicsPixmapItem):
    def _init__(self):
        super().__init__()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        # print('ITEM', event.pos().x(), event.pos().y())
        color = self.pixmap().toImage().pixelColor(event.pos().x(), event.pos().y()).toRgb()
        print(color)
        return super().mousePressEvent(event)


class ColorPaletteScene(QGraphicsScene):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        # print('SCENE', event.pos().x(), event.pos().y())
        # for item in self.items():
        #     print(type(item))

        return super().mousePressEvent(event)

class ColorPickerWidget(QDialog):
    def __init__(self, parent, signaler=None):
        super().__init__(parent)
        self.ui = Ui_ColorPicker()
        self.ui.setupUi(self)

        self.currentHue = QColor(255, 0, 0)

        # Color Palette
        self.palette_view = QGraphicsView()
        self.palette_scene = ColorPaletteScene()
        self.palette_view.setScene(self.palette_scene)
        self.palette_pix = ColorPalettePixmapItem()
        self.palette_pix.setPixmap(QPixmap(255, 255))
        self.palette_scene.addItem(self.palette_pix)
        self.ui.colorRangeWidget.layout().addWidget(self.palette_view)
        self.set_color_palette()

        self.palette_tool = ColorPaletteSelectionEllipseItem()
        self.palette_scene.addItem(self.palette_tool)

    def set_color_palette(self):
        # A colored background based on hue
        colorGradient = QLinearGradient(0, 0, 250, 0)
        colorGradient.setSpread(QGradient.RepeatSpread)
        colorGradient.setColorAt(0, QColor(255,255,255))
        colorGradient.setColorAt(1, self.currentHue)

        blackGradient = QLinearGradient(0, 0, 0, 250)
        blackGradient.setSpread(QGradient.RepeatSpread)
        blackGradient.setColorAt(0, QColor(0,0,0,0))
        blackGradient.setColorAt(1, QColor(0,0,0,255))

        p = QPixmap(250, 250)
        p.fill(Qt.white)
        painter = QPainter(p)
        painter.fillRect(p.rect(), colorGradient)
        painter.end()
        # self.palette_pix.setPixmap(p)

        p2 = QPixmap(250, 250)
        p2.fill(Qt.transparent)
        painter = QPainter(p2)
        painter.fillRect(p2.rect(), blackGradient)
        painter.end()
        self.palette_pix.setPixmap(self.add_pixmaps(p, p2))

    def image_to_pixmap(self, image) -> QPixmap:
        # TODO: Utility
        return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)

    def add_pixmaps(self, base_image: QPixmap=None, second_image: QPixmap=None) -> QPixmap:
        resultImage = QImage(QSize(250, 250), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(resultImage)
        painter.fillRect(resultImage.rect(), Qt.transparent)

        painter.drawPixmap(0, 0, base_image)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
        painter.drawPixmap(0, 0, second_image)

        painter.end()

        return self.image_to_pixmap(resultImage)
