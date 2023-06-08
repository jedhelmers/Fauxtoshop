from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import Qt, QLinearGradient, QGradient, QColor, QPen, QBrush, QMouseEvent, QPixmap, QPainter, QImage
from PySide6.QtWidgets import QDialog, QGraphicsSceneMouseEvent, QGraphicsPolygonItem, QGraphicsItem, QGraphicsEllipseItem, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem

from styles.window_panel import window_panel_style
from ui.color_pickerui import Ui_ColorPicker


class ColorScaleSelectionPolygonItem(QGraphicsPolygonItem):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        return super().mousePressEvent(event)


class ColorPaletteSelectionEllipseItem(QGraphicsEllipseItem):
    def __init__(self):
        super().__init__()

        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        # self.setFlag(QGraphicsItem.ItemIsSelectable, True)

        self.setRect(0, 0, 10, 10)
        self.setBrush(Qt.transparent)
        pen = QPen()
        pen.setColor(Qt.white)
        self.setPen(pen)
        # print(self.scene())
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
        # print(color)
        return super().mousePressEvent(event)


class ColorPaletteView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)

    # def mouseMoveEvent(self, event: QMouseEvent) -> None:
    #     for item in self.items():
    #         if isinstance(item, ColorPaletteSelectionEllipseItem):
    #             # Set position of selector
    #             item.setPos(event.pos().x(), event.pos().y())
    #         elif isinstance(item, ColorPalettePixmapItem):
    #             spot_color = item.pixmap().toImage().pixelColor(event.pos().x(), event.pos().y())
    #             print(spot_color)

    #     return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.get_color(event)
        return super().mouseReleaseEvent(event)


    def mousePressEvent(self, event: QMouseEvent) -> None:
        print(event.pos())
        return super().mousePressEvent(event)

    def get_color(self, event):
        for item in self.items():
            if isinstance(item, ColorPaletteSelectionEllipseItem):
                # Set position of selector
                item.setPos(event.pos().x(), event.pos().y())
            elif isinstance(item, ColorPalettePixmapItem):
                spot_color = item.pixmap().toImage().pixelColor(event.pos().x(), event.pos().y())
                print(spot_color)


class ColorPaletteScene(QGraphicsScene):
    def __init__(self, size):
        super().__init__()
        self.size = size

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
        self.palette_view = ColorPaletteView()
        self.palette_scene = ColorPaletteScene(250)
        self.palette_scene.setSceneRect(QRect(0, 0, 250, 250))
        self.palette_view.setScene(self.palette_scene)
        self.palette_pix = ColorPalettePixmapItem()
        self.palette_pix.setPixmap(QPixmap(250, 250))
        self.palette_scene.addItem(self.palette_pix)
        self.ui.colorGridLayout.addWidget(self.palette_view)
        self.set_color_palette()

        # Hue Scale
        self.hue_view = ColorPaletteView()
        self.hue_scene = ColorPaletteScene(250)
        self.hue_view.setScene(self.hue_scene)
        self.hue_pix = ColorPalettePixmapItem()
        self.hue_pix.setPixmap(QPixmap(100, 250))
        self.hue_scene.addItem(self.hue_pix)
        self.ui.colorScaleGridLayout.addWidget(self.hue_view)
        self.draw_scale()

        self.palette_tool = ColorPaletteSelectionEllipseItem()
        self.palette_scene.addItem(self.palette_tool)

    def set_color_palette(self):
        # A colored background based on hue
        colorGradient = QLinearGradient(0, 0, self.palette_scene.size, 0)
        colorGradient.setSpread(QGradient.RepeatSpread)
        colorGradient.setColorAt(0, QColor(255,255,255))
        colorGradient.setColorAt(1, self.currentHue)

        blackGradient = QLinearGradient(0, 0, 0, self.palette_scene.size)
        blackGradient.setSpread(QGradient.RepeatSpread)
        blackGradient.setColorAt(0, QColor(0,0,0,0))
        blackGradient.setColorAt(1, QColor(0,0,0,255))

        p = QPixmap(self.palette_scene.size, self.palette_scene.size)
        p.fill(Qt.white)
        painter = QPainter(p)
        painter.fillRect(p.rect(), colorGradient)
        painter.end()
        # self.palette_pix.setPixmap(p)

        p2 = QPixmap(self.palette_scene.size, self.palette_scene.size)
        p2.fill(Qt.transparent)
        painter = QPainter(p2)
        painter.fillRect(p2.rect(), blackGradient)
        painter.end()
        self.palette_pix.setPixmap(self.add_pixmaps(p, p2))

    def image_to_pixmap(self, image) -> QPixmap:
        # TODO: Utility
        return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)

    def add_pixmaps(self, base_image: QPixmap=None, second_image: QPixmap=None) -> QPixmap:
        resultImage = QImage(base_image.size(), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(resultImage)
        painter.fillRect(resultImage.rect(), Qt.transparent)

        painter.drawPixmap(0, 0, base_image)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
        painter.drawPixmap(0, 0, second_image)

        painter.end()

        return self.image_to_pixmap(resultImage)

    def draw_scale(self):
        height = self.ui.hueScaleWidget.height()
        width = self.ui.hueScaleWidget.width()

        height = 250
        width = 20

        self.hue_scene.setSceneRect(QRect(0, 0, width * 0.8, height))

        colorGradient = QLinearGradient(0, 0, 0, self.hue_scene.size)
        colorGradient.setSpread(QGradient.RepeatSpread)
        colorGradient.setColorAt(0, QColor(0, 255, 0))
        colorGradient.setColorAt(0.2, QColor(255, 255, 0))
        colorGradient.setColorAt(0.4, QColor(0, 0, 255))
        colorGradient.setColorAt(0.6, QColor(255, 0, 255))
        colorGradient.setColorAt(0.8, QColor(255, 0, 0))
        colorGradient.setColorAt(1, QColor(0, 255, 255))

        p = QPixmap(width, height)
        p.fill(Qt.white)
        painter = QPainter(p)
        painter.fillRect(p.rect(), colorGradient)
        painter.end()

        print('COLOR AT', p.toImage().pixelColor(10, 100).toRgb())


        self.hue_pix.setPixmap(p)

