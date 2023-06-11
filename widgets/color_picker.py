from typing import Any
from PySide6.QtCore import QRect, QSize, QPointF
from PySide6.QtGui import Qt, QPolygonF, QLinearGradient, QGradient, QColor, QPen, QBrush, QMouseEvent, QPixmap, QPainter, QImage
from PySide6.QtWidgets import QDialog, QGraphicsSceneDragDropEvent, QGraphicsSceneMouseEvent, QGraphicsPolygonItem, QGraphicsItem, QGraphicsEllipseItem, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem

from styles.window_panel import window_panel_style
from ui.color_pickerui import Ui_ColorPicker


class ColorScaleSelectionPolygonItem(QGraphicsPolygonItem):
    def __init__(self):
        super().__init__()
        self.setFlag(QGraphicsItem.ItemIsMovable, True)

        self.left_path = QPolygonF()
        self.left_path.push_back(QPointF(10.2, 20.5))
        self.left_path.push_back(QPointF(-6, 30.2))
        self.left_path.push_back(QPointF(-6, 10.8))
        self.setPolygon(self.left_path)

        self.setBrush(Qt.white)
        self.setPen(QPen(Qt.white))
        self.setScale(0.6)

        # Flags
        self.is_pressed = False

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        self.is_pressed = True
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        self.is_pressed = False
        return super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if self.is_pressed:
            self.left_path.translate(0, event.pos().y())
            # pos = QPointF(0, event.pos().y() / 2.5)
            # self.setPos(pos)
            self.setY(event.pos().y() / 1.75)

        # return super().mouseMoveEvent(_event)


class ColorPaletteSelectionEllipseItem(QGraphicsEllipseItem):
    def __init__(self, set_new_color):
        super().__init__()
        self.setBoundingRegionGranularity(0)

        self.set_new_color = set_new_color

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

    def is_within_bounds(self, event):
        [x, y] = event.pos().toTuple()
        pos = QPointF(
            min(255, max(0, x)),
            min(255, max(0, y))
        )
        event.setPos(pos)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        self.is_within_bounds(event)
        super().mouseMoveEvent(event)
        
        if self.set_new_color:
            rect = self.rect()
            offset_x = rect.width() / 2
            offset_y = rect.height() / 2
            pos = QPointF(
                self.pos().x() + offset_x,
                self.pos().y() + offset_y
            )
            self.set_new_color(pos)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        self.is_within_bounds(event)
        super().mouseReleaseEvent(event)

        if self.set_new_color:
            self.set_new_color(self.pos())


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
        # print(event.pos())
        return super().mousePressEvent(event)

    def get_color(self, event):
        for item in self.items():
            if isinstance(item, ColorPaletteSelectionEllipseItem):
                # Set position of selector
                item.setPos(event.pos().x(), event.pos().y())
            elif isinstance(item, ColorPalettePixmapItem):
                spot_color = item.pixmap().toImage().pixelColor(event.pos().x(), event.pos().y())
                # print(spot_color)


class ColorPaletteScene(QGraphicsScene):
    def __init__(self, size):
        super().__init__()
        self.size = size

    def mousePressEvent(self, event: QMouseEvent) -> None:
        # print('SCENE', event.pos().x(), event.pos().y())
        for item in self.items():
            if isinstance(item, ColorPaletteSelectionEllipseItem):
                print(type(item))
                print('WEE')
                # self.sendEvent(item, ColorPaletteSelectionEllipseItem.mousePressEvent)
        # self.update(QRect(0, 0, 250, 250))
        # self.sendEvent()
        return super().mousePressEvent(event)

class ColorPickerWidget(QDialog):
    def __init__(self, parent, current_color: QColor=QColor(0, 0, 0), signaler=None):
        super().__init__(parent)
        self.ui = Ui_ColorPicker()
        self.ui.setupUi(self)

        self.new_color = QColor(255, 255, 255)
        self.current_color = current_color
        self.current_hue = QColor(255, 0, 0)

        # New/Old colors
        self.new_color_pix = QPixmap(self.ui.newColorLabel.size())
        self.new_color_pix.fill(self.new_color)
        self.ui.newColorLabel.setPixmap(self.new_color_pix)
        self.current_color_pix = QPixmap(self.ui.currentColorLabel.size())
        self.current_color_pix.fill(self.current_color)
        self.ui.currentColorLabel.setPixmap(self.current_color_pix)

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

        # Hue Scale selector
        self.hue_selector = ColorScaleSelectionPolygonItem()
        self.hue_scene.addItem(self.hue_selector)

        # Palette selection tool
        self.palette_tool = ColorPaletteSelectionEllipseItem(self.set_new_color)
        self.palette_scene.addItem(self.palette_tool)

        # Actions
        self.ui.okPushButton.clicked.connect(self.accept)
        self.ui.redLineEdit.textEdited.connect(lambda val: self.update_color_line_edit(val, 'redLineEdit'))
        self.ui.greenLineEdit.textEdited.connect(lambda val: self.update_color_line_edit(val, 'greenLineEdit'))
        self.ui.blueLineEdit.textEdited.connect(lambda val: self.update_color_line_edit(val, 'blueLineEdit'))
        self.ui.cyanLineEdit.textEdited.connect(lambda val: self.update_color_line_edit(val, 'cyanLineEdit'))
        self.ui.magentaLineEdit.textEdited.connect(lambda val: self.update_color_line_edit(val, 'magentaLineEdit'))
        self.ui.yellowLineEdit.textEdited.connect(lambda val: self.update_color_line_edit(val, 'yellowLineEdit'))
        self.ui.keyLineEdit.textEdited.connect(lambda val: self.update_color_line_edit(val, 'keyLineEdit'))
        self.ui.hueLineEdit.textEdited.connect(lambda val: self.update_color_line_edit(val, 'hueLineEdit'))
        self.ui.brightnessLineEdit.textEdited.connect(lambda val: self.update_color_line_edit(val, 'brightnessLineEdit'))
        self.ui.luminanceLineEdit.textEdited.connect(lambda val: self.update_color_line_edit(val, 'luminanceLineEdit'))
        self.ui.saturationLineEdit.textEdited.connect(lambda val: self.update_color_line_edit(val, 'saturationLineEdit'))
        self.ui.hexLineEdit.textEdited.connect(lambda val: self.update_color_line_edit(val, 'hexLineEdit'))

        # Test
        # self.find_pixel(QColor(200, 0, 0))


    @property
    def new_color(self):
        return self._new_color

    @new_color.setter
    def new_color(self, new_color):
        self._new_color = new_color

    def close(self) -> bool:
        return super().close()

    def move_dot(self):
        x1 = self.percent_to_num(float(self.ui.saturationLineEdit.text()))
        y1 = self.percent_to_num(float(self.ui.brightnessLineEdit.text()))
        [x2, y2] = self.palette_tool.pos().toTuple()

        # Move by difference of x2, x1
        self.palette_tool.moveBy((x1 - x2), (y1 - y2))

    def normalize_255(self, num: int) -> int:
        if num < 0:
            return 0

        if num > 255:
            return 255

        return num

    def num_to_percent(self, num: float) -> float:
        percent = self.normalize_255(num) / 2.55
        return float('%.1f' % percent)

    def percent_to_num(self, num: float) -> float:
        return self.normalize_255(2.55 * num)

    def to_hex(self, num: int):
        hex_val = hex(self.normalize_255(num))[2:].upper()

        if len(hex_val) == 1:
            return '0' + hex_val

        return hex_val

    def find_pixel(self, color: QColor):
        # H 360º is hue scale
        # S horizontal
        # B vertical

        pass

    def update_color_line_edit(self, val, key: str):
        print(key, val)
        # Update color palette
        self.move_dot()
        # Update form fields
        # Move dot

    def set_new_color(self, pos: QPointF):
        # New Color swatch
        [x, y] = pos.toTuple()

        pos = QPointF(
            min(248, max(0, x)),
            min(248, max(0, y))
        )
        new_color = self.palette_pix.pixmap().toImage().pixelColor(pos.toPoint())
        self.new_color = new_color
        pix = QPixmap(self.ui.newColorLabel.size())
        pix.fill(new_color)
        self.ui.newColorLabel.setPixmap(pix)

        # R G B
        [r, g, b, a] = new_color.toTuple()
        self.ui.redLineEdit.setText(str(self.normalize_255(r)))
        self.ui.greenLineEdit.setText(str(self.normalize_255(g)))
        self.ui.blueLineEdit.setText(str(self.normalize_255(b)))

        # C M Y K
        [c, m, y, k, a] = new_color.toCmyk().toTuple()
        self.ui.cyanLineEdit.setText(str(self.normalize_255(c)))
        self.ui.magentaLineEdit.setText(str(self.normalize_255(m)))
        self.ui.yellowLineEdit.setText(str(self.normalize_255(y)))
        self.ui.keyLineEdit.setText(str(self.normalize_255(k)))

        # H L S B
        [h, l, s, a] = new_color.toHsl().toTuple()
        [_, _, b, _] = new_color.toHsv().toTuple()
        self.ui.hueLineEdit.setText(str(self.normalize_255(h)))
        self.ui.luminanceLineEdit.setText(str(self.normalize_255(s)))
        self.ui.saturationLineEdit.setText(str(self.num_to_percent(l)))
        self.ui.brightnessLineEdit.setText(str(self.num_to_percent(b)))

        # Hex
        _hex = self.to_hex(r)
        _hex += self.to_hex(g)
        _hex += self.to_hex(b)
        self.ui.hexLineEdit.setText(_hex)

        # a b

    def set_color_palette(self):
        # A colored background based on hue
        colorGradient = QLinearGradient(0, 0, self.palette_scene.size, 0)
        colorGradient.setSpread(QGradient.RepeatSpread)
        colorGradient.setColorAt(0, QColor(255,255,255))
        colorGradient.setColorAt(1, self.current_hue)

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

        scale = [
            [255, 0, 0],
            [255, 0, 255],
            [0, 0, 255],
            [0, 255, 255],
            [0, 255, 0],
            [255, 255, 0],
            [255, 0, 0]
        ]


        self.hue_scene.setSceneRect(QRect(0, 0, width * 0.8, height))

        colorGradient = QLinearGradient(0, 0, 0, self.hue_scene.size)
        colorGradient.setSpread(QGradient.RepeatSpread)

        for index, step in enumerate(scale):
            i = index / (len(scale) - 1)
            colorGradient.setColorAt(i, QColor(*step))

        p = QPixmap(width, height)
        p.fill(Qt.white)
        painter = QPainter(p)
        painter.fillRect(p.rect(), colorGradient)
        painter.end()

        # print('COLOR AT', p.toImage().pixelColor(10, 100).toRgb())


        self.hue_pix.setPixmap(p)

