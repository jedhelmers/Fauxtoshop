from PySide6.QtGui import QLinearGradient, QGradient, QColor, QBrush, QMouseEvent
from PySide6.QtWidgets import QDialog, QGraphicsView, QGraphicsScene

from styles.window_panel import window_panel_style
from ui.color_pickerui import Ui_ColorPicker


class ColorPaletteView(QGraphicsView):
    def __init__(self):
        super().__init__(self)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        # print(self.pix)
        return super().mousePressEvent(event)

class ColorPickerWidget(QDialog):
    def __init__(self, parent, signaler=None):
        super().__init__(parent)
        self.ui = Ui_ColorPicker()
        self.ui.setupUi(self)

        self.currentHue = QColor(255, 0, 0)

        # Color Palette
        self.palette_view = ColorPaletteView()
        self.palette_scene = QGraphicsScene()
        self.palette_view.setScene(self.palette_scene)
        self.ui.colorRangeWidget.layout().addWidget(self.palette_view)
        self.set_color_palette()

    def set_color_palette(self):
        # A colored background based on hue
        colorGradient = QLinearGradient(self.ui.colorRangeWidget.width() * 0.5, 0, self.ui.colorRangeWidget.width() * 1.5, 0)
        colorGradient.setSpread(QGradient.RepeatSpread)
        colorGradient.setColorAt(0, QColor(255,255,255))
        colorGradient.setColorAt(1, self.currentHue)

        blackGradient = QLinearGradient(0, self.ui.colorRangeWidget.height() * 0.5, 0, self.ui.colorRangeWidget.height() * 1.5)
        blackGradient.setSpread(QGradient.RepeatSpread)
        blackGradient.setColorAt(0, QColor(0,0,0,0))
        blackGradient.setColorAt(1, QColor(0,0,0,255))

        colorGradiantBrush = QBrush(colorGradient)
        blackGradiantBrush = QBrush(blackGradient)
        self.palette_scene.setBackgroundBrush(colorGradiantBrush)
        self.palette_scene.setForegroundBrush(blackGradiantBrush)
