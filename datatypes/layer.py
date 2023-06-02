from dataclasses import dataclass
from PySide6.QtCore import Qt, QSize, QRectF, QRect
from PySide6.QtGui import QPainter, QRegion, QPixmap, QBrush, QBitmap, QPainterPath, QImage, QColor, QPen, QMouseEvent
from PySide6.QtWidgets import QGraphicsItem, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QGraphicsRectItem, QGraphicsSceneMouseEvent, QWidget, QStyleOptionGraphicsItem, QStyle
from typing import List, Union

id = 0
parent_id = 0


class GraphicsItemBase:
    settings = None
    def __init__(self, mode=None, name=None):
        # TODO: Set ALL non-text/non-path layers to Pixmap upon creation
        super().__init__()
        self.mode = mode
        self.name = name
        self.hidden = False

        # Set flags
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemClipsChildrenToShape)

    def paint(self, painter: QPainter, style_object: QStyleOptionGraphicsItem, widget: QWidget = None):
        style_object.state &= ~QStyle.State_Selected

        self.clip(painter)
        painter.setCompositionMode(mode_mappings(self.mode))
        super().paint(painter, style_object, widget)

    def set_settings(self, settings):
        self.settings = settings

    def clip(self, painter: QPainter):
        # CLip to board
        if self.settings:
            path = QPainterPath()
            path.addRect(QRectF(*[-p for p in self.pos().toTuple()], *self.settings['document_dimensions']))
            painter.setClipPath(path)


class ArtBoard(QGraphicsScene):
    settings = None
    def __init__(self):
        super().__init__()

        pix = QGraphicsPixmapItem()
        pix.setPixmap(self.generate_checkerboard(20))
        self.addItem(pix)

        self.setItemIndexMethod(QGraphicsScene.BspTreeIndex)

    def drawForeground(self, painter: QPainter, rect: QRectF | QRect) -> None:
        # self.painter(painter)
        print('WEEEE')
        self.draw_grid(painter, 20)
        return super().drawForeground(painter, rect)

    def generate_checkerboard(self, checker_width=50) -> QPixmap:
        if self.settings:
            dimensions = self.settings['document_dimensions']
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
                        i * checker_width, j * checker_width,
                        checker_width, checker_width
                    ), color)

            painter.end()

            return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)
        return QPixmap()

    def draw_grid(self, painter: QPainter, grid_width=50):
        if self.settings:
            [w, h] = self.settings['document_dimensions']

            rows = int(h // grid_width)
            cols = int(w // grid_width)

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

        return painter

class ArtBoardView(QGraphicsView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class GraphicsPixmapItem(GraphicsItemBase, QGraphicsPixmapItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        # print('POS', event.pos())
        return super().setSelected(True)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        print('POS', event.pos().toPoint().x(), event.pos().toPoint().y())
        return super().mouseMoveEvent(event)

    def paint(self, painter: QPainter, style_object: QStyleOptionGraphicsItem, widget: QWidget = None):
        color = QColor(Qt.white)

        # print(self.isSelected())
        if self.isSelected():
            pen = QPen(color, 1.5, Qt.DashLine, Qt.RoundCap)
            pen.setDashPattern([4.0, 4.0])
            painter.setPen(pen)
        else:
            pen = Qt.NoPen
            # painter.setPen(pen)

        # # CLip to board
        # path = QPainterPath()
        # path.addRect(QRectF(*[-p for p in self.pos().toTuple()], 400, 400))
        # painter.setClipPath(path)

        painter.setCompositionMode(mode_mappings(self.mode))
        # painter.setPen(pen)
        super().paint(painter, style_object, widget)

class GraphicsRectItemBase(GraphicsItemBase, QGraphicsRectItem):
    def __init__(self, name='Layer', mode='Normal', x=0, y=0, w=0, h=0, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setRect(x, y, w, h)
        self._rotation = 0.0


    # static QPixmap QPixmapFromItem(QGraphicsItem *item){
    #     QPixmap pixmap(item->boundingRect().size().toSize());
    #     pixmap.fill(Qt::transparent);
    #     QPainter painter(&pixmap);
    #     painter.setRenderHint(QPainter::Antialiasing);
    #     QStyleOptionGraphicsItem opt;
    #     item->paint(&painter, &opt);
    #     return pixmap;
    # }
    def to_pixmap(self, size) -> QPixmap:
        pixmap = QPixmap(size)
        # pixmap = QPixmap(self.boundingRect().size().toSize())
        pixmap.fill(Qt.transparent)

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Multiply)
        style_option = QStyleOptionGraphicsItem()
        # style_option.state = ~QStyle.State_None
        self.paint(painter, style_option)
        # painter.drawPixmap(0, 0, pixmap)
        painter.end()

        return pixmap

    # def mousePressEvent(self, event) -> None:
    #     print('WEE')
    #     return super().setSelected(selected)

    def setRotation(self, angle: float) -> None:
        self._rotation = angle
        # return super().setRotation(angle)

    def paint(self, painter: QPainter, style_object: QStyleOptionGraphicsItem, widget: QWidget = None):
        color = QColor(Qt.white)

        if self.isSelected():
            pen = QPen(color, 1.5, Qt.DashLine, Qt.RoundCap)
            pen.setDashPattern([4.0, 4.0])
            # painter.setPen(pen)
        else:
            pen = Qt.NoPen
            # painter.setPen(pen)

        painter.setCompositionMode(mode_mappings(self.mode))
        super().paint(painter, style_object, widget)


@dataclass
class Layer:
    __slots__ = [
        'index',
        'layer_id',
        'color',
        'name',
        'alpha_lock',
        'lock',
        'show',
        'image',
        'masks',
        'position',
        'scale',
        'mode',
        'mode_percent',
        'parent',
        'effects',
        'opacity',
    ]

    def __init__(
            self,
            layer_id=None,
            index=0,
            color=None,
            name=None,
            alpha_lock=False,
            lock=False,
            show=True,
            image=None,
            masks=[],
            position=[0.0, 0.0], # QPoint
            scale=[1.0, 1.0], # qreal? Double I think.
            mode='Normal',
            mode_percent=1.0,
            parent=None,
            effects=[],
            opacity=1.0,
            ):
        global id
        self.index = index
        if layer_id is None:
            self.layer_id = id
            id += 1
        else:
            self.layer_id = layer_id

        self.color = color

        if name:
            self.name = name
        else:
            self.name = f'Layer {self.layer_id}'

        self.alpha_lock = alpha_lock
        self.lock = lock
        self.show = show
        self.image = image
        self.masks = masks
        self.position = position
        self.scale = scale
        self.mode = mode
        self.mode_percent = mode_percent
        self.parent = parent
        self.effects = effects
        self.opacity = opacity


class LayerBase(QGraphicsItem):
    def __init__(
        self,
        layer_id=None,
        index=0,
        color=None,
        name=None,
        alpha_lock=False,
        lock=False,
        show=True,
        image=None,
        masks=[],
        position=[0.0, 0.0], # QPoint
        scale=[1.0, 1.0], # qreal? Double I think.
        mode='Normal',
        mode_percent=1.0,
        parent=None,
        effects=[],
        opacity=1.0,
        ):
        super().__init__()
        global id
        self.index = index
        if layer_id is None:
            self.layer_id = id
            id += 1
        else:
            self.layer_id = layer_id

        self.color = color

        if name:
            self.name = name
        else:
            self.name = f'Layer {self.layer_id}'

        self.alpha_lock = alpha_lock
        self.lock = lock
        self.show = show
        self.image = image
        self.masks = masks
        self.position = position
        self.scale = scale
        self.mode = mode
        self.mode_percent = mode_percent
        self.parent = parent
        self.effects = effects
        self.opacity = opacity
        self.setPos(10, 20)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)

    @property
    def is_selected(self):
        return self._is_selected

    @is_selected.setter
    def is_selected(self, is_selected):
        self._is_selected = is_selected

    def to_pixmap(self) -> QPixmap:
        pixmap = QPixmap(self.boundingRect().size().toSize())
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Multiply)
        style_option = QStyleOptionGraphicsItem()
        # style_option.state = ~QStyle.State_None
        # self.paint(painter, style_option)
        painter.end()

        return pixmap

    def def_add_image(self, layer: QPixmap, mode: str) -> QPixmap:
        mode = mode_mappings(mode)

        resultImage = QImage(self.boundingRect().size().toSize(), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(resultImage)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.fillRect(resultImage.rect(), Qt.transparent)

        # painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
        painter.drawPixmap(0, 0, self.to_pixmap())
        painter.setCompositionMode(mode)
        painter.drawPixmap(0, 0, layer)
        painter.setCompositionMode(QPainter.CompositionMode_DestinationOver)
        painter.fillRect(resultImage.rect(), Qt.transparent)
        painter.end()

        return self.image_to_pixmap(resultImage)

    def image_to_pixmap(self, image) -> QPixmap:
        # TODO: Utility
        return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)

    def paint(self, painter, options, widget):
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Screen)
        super().paint(painter, options, widget)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        # print('WEEEEE', event)

@dataclass
class LayerGroup(Layer):
    __slots__ = [
        'children',
        'is_open'
    ]

    def __init__(
            self,
            children: List=[],
            is_open: bool=False,
            *args,
            **kwargs
        ):
        super().__init__(self, *args, **kwargs)
        self.children = children
        self.is_open = is_open


def modes():
    return [
        'Normal',
        'Dissolve', # 2 Added
        # "DestinationOver",
        # "Clear",
        # "Source",
        # "Destination",
        # "SourceIn",
        # "DestinationIn",
        # "SourceOut",
        # "DestinationOut",
        # "SourceAtop",
        # "DestinationAtop",
        "Darken",
        "Multiply",
        "Color Burn",
        "Linear Burn", # Added
        "Darker Color", # 8 Added

        "Lighten",
        "Screen",
        "Color Dodge",
        "Linear Dodge (Add)",
        "Lighter Color", # 14

        "Overlay",
        "Soft Light",
        "Hard Light",
        "Vivid Light", # 19 Added

        "Difference",
        "Exclusion",
        "Subtract", # Added
        "Divide", # 24 Added

        'Hue', # Added
        'Saturation', # Added
        'Color', # Added
        'Luminosity', # 29 Added
        "Xor",
        "Plus",
    ]


def mode_mappings(mode):
    switch = {
        'Normal': QPainter.CompositionMode.CompositionMode_SourceOver,
        "DestinationOver": QPainter.CompositionMode.CompositionMode_DestinationOver,
        "Clear": QPainter.CompositionMode.CompositionMode_Clear,
        "Source": QPainter.CompositionMode.CompositionMode_Source,
        "Destination": QPainter.CompositionMode.CompositionMode_Destination,
        "SourceIn": QPainter.CompositionMode.CompositionMode_SourceIn,
        "DestinationIn": QPainter.CompositionMode.CompositionMode_DestinationIn,
        "SourceOut": QPainter.CompositionMode.CompositionMode_SourceOut,
        "DestinationOut": QPainter.CompositionMode.CompositionMode_DestinationOut,
        "SourceAtop": QPainter.CompositionMode.CompositionMode_SourceAtop,
        "DestinationAtop": QPainter.CompositionMode.CompositionMode_DestinationAtop,
        "Xor": QPainter.CompositionMode.CompositionMode_Xor,
        "Plus": QPainter.CompositionMode.CompositionMode_Plus,
        "Multiply": QPainter.CompositionMode.CompositionMode_Multiply,
        "Screen": QPainter.CompositionMode.CompositionMode_Screen,
        "Overlay": QPainter.CompositionMode.CompositionMode_Overlay,
        "Darken": QPainter.CompositionMode.CompositionMode_Darken,
        "Lighten": QPainter.CompositionMode.CompositionMode_Lighten,
        "Color Dodge": QPainter.CompositionMode.CompositionMode_ColorDodge,
        "Color Burn": QPainter.CompositionMode.CompositionMode_ColorBurn,
        "Hard Light": QPainter.CompositionMode.CompositionMode_HardLight,
        "Soft Light": QPainter.CompositionMode.CompositionMode_SoftLight,
        "Difference": QPainter.CompositionMode.CompositionMode_Difference,
        "Exclusion": QPainter.CompositionMode.CompositionMode_Exclusion,
    }
    return switch[mode] if mode in switch else switch['Normal']
