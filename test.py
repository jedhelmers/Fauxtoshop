import json
import random
import sys
from pathlib import Path

from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, Qt, QEvent, QPoint, QObject, QCoreApplication, QRect
from PySide6.QtGui import QIcon, QPixmap, QImage, QPainter, QColor, QMouseEvent, qRgba, QBrush, QPen, QFont
from PySide6.QtWidgets import QMainWindow, QFrame, QApplication, QTableWidgetItem, QStyle, QStyleOptionGraphicsItem, QGraphicsPixmapItem, QGraphicsItem, QGraphicsTextItem, QGraphicsItemGroup, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsPixmapItem, QPushButton, QWidget, QGridLayout, QLabel

from datatypes.layer import LayerBase
from ui.testui import Ui_MainWindow

print('https://www.pythonguis.com/tutorials/pyqt-qgraphics-vector-graphics/')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # SETUP
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet("QGraphicsView {opacity: 0;}")

        # Create text item
        scene = QGraphicsScene(self, 0, 0, 400, 400)
        text = QGraphicsTextItem("Howdy, world!")

        style_option = QStyleOptionGraphicsItem()
        style_option.state = QStyle.State_None
        # TODO: Composition mode does not work
        # Create pixmap
        img = QPixmap(100, 100)
        img.fill(QColor(0, 255, 0, 100))
        img_item = QGraphicsPixmapItem(img)
        painter = QPainter(img)
        painter.save()
        brush_9 = QBrush(QColor(0, 0, 255, 100))
        painter.setBackground (brush_9)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Multiply)
        # painter.drawPixmap(0, 0, img)
        painter.end()
        # painter.restore()

        # Create rect
        rect = QGraphicsRectItem(0, 0, 200, 50)
        rect.setPos(50, 20)
        brush = QBrush(QColor(0, 0, 255, 100))
        rect.setPen(Qt.NoPen)
        rect.setBrush(brush)

        # Create rect
        rect2 = QGraphicsRectItem(0, 0, 200, 50)
        brush2 = QBrush(QColor(255, 0, 0, 100))
        rect2.setBrush(brush2)

        rect_2 = LayerBase()
        rect_2.setRect(0, 0, 200, 50)
        rect_2.setBrush(brush2)
        rect_2.setPos(30, 30)
        rect_2.setPen(Qt.NoPen)

        # print(rect_2.to_pixmap())


        # Create group and add to it
        group = QGraphicsItemGroup()
        group.addToGroup(rect)
        # group.addToGroup(rect2)
        # group.addToGroup(text)
        # group.addToGroup(img_item)
        # group.addToGroup(rect_2)

        # Make movable
        scene.addItem(group)
        group.setFlag(QGraphicsItem.ItemIsMovable)
        group.setFlag(QGraphicsItem.ItemIsSelectable)

        rect_2.setFlag(QGraphicsItem.ItemIsMovable)
        rect_2.setFlag(QGraphicsItem.ItemIsSelectable)
        scene.addItem(rect_2)

        pixmap = QGraphicsPixmapItem()
        # pixmap.setPen(Qt.NoPen)
        pixmap.setOpacity(0.5)
        pixmap_1 = rect_2.to_pixmap()
        pix = QPixmap(QSize(100, 400))
        pix.fill(QColor(255, 255, 0, 200))
        pixmap_1 = rect_2.def_add_image(pix, 'Multiply')
        pixmap.setFlag(QGraphicsItem.ItemIsMovable)
        pixmap.setFlag(QGraphicsItem.ItemIsSelectable)
        pixmap.setPixmap(pixmap_1)
        scene.addItem(pixmap)

        if scene.items():
            try:
                print(scene.items()[1].toPlainText())
            except Exception as e:
                print(e)
            # text.toPlainText()

        # Create view with scene and add to layout
        i = QPixmap(QSize(300, 400))
        i.fill(Qt.transparent)
        p = QPainter(i)
        scene.render(p)

        view = QGraphicsView(scene)
        # view.setHidden(True)
        view.setStyleSheet("opacity: 50")
        view.setWindowOpacity(0.0)
        # view.setBackgroundBrush(brush_9)
        view.setMask(QRect(250, 50, 600, 300))

        label = QLabel()
        # label.setGeometry(60, 0, 400, 400)
        pix = QPixmap(QSize(300, 400))
        pix.fill(QColor(255, 255, 0, 100))
        label.setStyleSheet("margin: 0px; background: transparent")
        # label.setPixmap(pix)
        label.setPixmap(i)

        self.ui.gridLayout_2.addWidget(label, 0, 0, 0, 0)
        self.ui.gridLayout_2.addWidget(view, 0, 0, 0, 0)


def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
