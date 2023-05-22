import json
import random
import sys
from pathlib import Path

from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, Qt, QEvent, QPoint, QObject, QCoreApplication, QRect
from PySide6.QtGui import QIcon, QPixmap, QImage, QPainter, QColor, QMouseEvent, qRgba, QBrush, QPen, QFont
from PySide6.QtWidgets import QMainWindow, QFrame, QApplication, QTableWidgetItem, QGraphicsPixmapItem, QGraphicsItem, QGraphicsTextItem, QGraphicsItemGroup, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsPixmapItem, QPushButton, QWidget, QGridLayout, QLabel

from ui.testui import Ui_MainWindow

print('https://www.pythonguis.com/tutorials/pyqt-qgraphics-vector-graphics/')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # SETUP
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create text item
        scene = QGraphicsScene(self, 0, 0, 400, 400)
        text = QGraphicsTextItem("Howdy, world!")

        # TODO: Composition mode does not work
        # Create pixmap
        img = QPixmap(100, 100)
        img.fill(QColor(0, 255, 0, 100))
        img_item = QGraphicsPixmapItem(img)
        painter = QPainter(img)
        painter.save()
        brush_9 = QBrush(QColor(0, 0, 255, 100))
        painter.setBackground(brush_9)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Multiply)
        painter.drawPixmap(0, 0, img)
        # painter.end()
        painter.restore()

        # Create rect
        rect = QGraphicsRectItem(0, 0, 200, 50)
        rect.setPos(50, 20)
        brush = QBrush(QColor(0, 0, 255, 100))
        rect.setBrush(brush)

        # Create rect
        rect2 = QGraphicsRectItem(0, 0, 200, 50)
        brush2 = QBrush(QColor(255, 0, 0, 100))
        rect2.setBrush(brush2)

        # Create group and add to it
        group = QGraphicsItemGroup()
        group.addToGroup(rect)
        group.addToGroup(rect2)
        group.addToGroup(text)
        group.addToGroup(img_item)

        # Make movable
        scene.addItem(group)
        group.setFlag(QGraphicsItem.ItemIsMovable)
        group.setFlag(QGraphicsItem.ItemIsSelectable)

        # Create view with scene and add to layout
        view = QGraphicsView(scene)
        view.setBackgroundBrush(brush_9)
        view.setMask(QRect(50, 50, 300, 300))
        self.ui.gridLayout_2.addWidget(view)


def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
