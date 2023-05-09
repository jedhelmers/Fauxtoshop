import json
import math
import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QImage, QIcon, qRgba, QPixmap


SETTINGS_PATH = './settings.json'


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
    return inches * 96

def pixel_to_inch(pixels):
    """
    Pixels to inches. Round up to nearest inch
    """
    return math.ceil(pixels / 96)
