import json
import math
import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QImage, QIcon, qRgba, QPixmap
from PySide6.QtWidgets import QMainWindow, QFrame, QApplication, QTableWidgetItem, QGraphicsScene, QGraphicsPixmapItem, QPushButton, QWidget, QGridLayout, QLabel


SETTINGS_PATH = './settings.json'
DPI = 96

def set_dpi(dpi):
    global DPI
    DPI = dpi

def image_to_pixmap(image) -> QPixmap:
    return QPixmap(image.size()).fromImage(image, Qt.ColorOnly)

def load_settings():
    if not os.path.exists(SETTINGS_PATH):
        file = open(SETTINGS_PATH, 'w+')
        file.close()

    file = open(SETTINGS_PATH, 'r')
    file_data = json.load(file)
    file.close()
    return file_data

def save_settings():
    file = open(SETTINGS_PATH, 'w+')
    file_data = json.dumps(file, indent=3, sort_keys=True)
    file.close()
    return file_data

def unit_conversion(unit, value):
    """
    Convert all to pixels.
    """
    if unit == 'Inches':
        return 96 * value
    elif unit == 'Pixels':
        return value
    elif unit == 'Picas':
        return value / 0.062499992175197
    return value

def inch_to_pixel(inches):
    return inches * DPI

def pixel_to_inch(pixels):
    """
    Pixels to inches. Round up to nearest inch
    """
    return pixels / DPI


# RULER LINES
# Create a Ruler class to handle all this.
class QHLine(QFrame):
    def __init__(self, parent, width=20, thickness=1):
        super(QHLine, self).__init__(parent=parent)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setMaximumHeight(thickness)
        self.setMaximumWidth(width)
        self.setStyleSheet('border-color: rgba(255, 255, 255, 0.1)')


class QVLine(QFrame):
    def __init__(self, parent, height=20, thickness=1):
        super(QVLine, self).__init__(parent=parent)
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setMaximumWidth(thickness)
        self.setMaximumHeight(height)
        self.setStyleSheet('border-color: rgba(255, 255, 255, 0.1)')

