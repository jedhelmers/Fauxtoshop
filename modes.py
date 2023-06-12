import cv2
import numpy as np
from typing import Union

from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, QLineF, QPointF, Qt, QEvent, QPoint, QObject, QCoreApplication, QRect
from PySide6.QtGui import QIcon, QPixmap, QConicalGradient, QBrush, QRadialGradient, QImage, QPainter, QColor, QMouseEvent, qRgba, QPen
from PySide6.QtWidgets import QMainWindow, QScrollArea, QFrame, QApplication, QTableWidgetItem, QGraphicsScene, QGraphicsPixmapItem, QPushButton, QWidget, QGridLayout, QLabel

from datatypes.layer import Layer, LayerGroup, mode_mappings


def invert_image(img: Union[QImage, QPixmap]):
    image = cv2.Mat()
    image[:, :, :] = 255 - image[:, :, :]
    return image

def multiply(a: Union[QImage, QPixmap], b: Union[QImage, QPixmap]):
    return a[:, :, :] * b[:, :, :]

def divide(a: Union[QImage, QPixmap], b: Union[QImage, QPixmap]):
    return a[:, :, :] / b[:, :, :]
