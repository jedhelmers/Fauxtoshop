import argparse
import cv2
import numpy as np
from typing import Union

from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, QLineF, QPointF, Qt, QEvent, QPoint, QObject, QCoreApplication, QRect
from PySide6.QtGui import QIcon, QPixmap, QConicalGradient, QBrush, QRadialGradient, QImage, QPainter, QColor, QMouseEvent, qRgba, QPen
from PySide6.QtWidgets import QMainWindow, QScrollArea, QFrame, QApplication, QTableWidgetItem, QGraphicsScene, QGraphicsPixmapItem, QPushButton, QWidget, QGridLayout, QLabel

# from datatypes.layer import Layer, LayerGroup

def gammaCorrection(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)

def invert_image(img):
    image = cv2.Mat()
    image[:, :, :] = 255 - image[:, :, :]
    return image

def multiply(a, b):
    # store the alpha channels only
    return cv2.multiply(a, b)

def divide(a, b):
    return a[:, :, :] / b[:, :, :]

def subtract(a, b):
    # store the alpha channels only
    black = np.zeros_like(a)
    black.fill(255)

    m1 = a[:,:,3]
    a = normal(a, black)
    a = gammaCorrection(a, 0.00001) 
    a = cv2.bitwise_not(a)

    a[:, :, 3] = m1

    composite = normal(a, b)

    return composite

def normal(a, b):
    # return a + (b * (1 - a))
    # store the alpha channels only
    m1 = a[:,:,3]
    m2 = b[:,:,3]

    # invert the alpha channel and obtain 3-channel mask of float data type
    m1 = cv2.bitwise_not(m1)
    alpha1i = cv2.cvtColor(m1, cv2.COLOR_GRAY2BGRA)/255.0

    m2 = cv2.bitwise_not(m2)
    alpha2i = cv2.cvtColor(m2, cv2.COLOR_GRAY2BGRA)/255.0

    # Perform blending and limit pixel values to 0-255 (convert to 8-bit)
    b1i = cv2.convertScaleAbs(b * (alpha1i) + a * (1 - alpha1i))

    # Finding common ground between both the inverted alpha channels
    mul = cv2.multiply(alpha2i, alpha1i)

    # converting to 8-bit
    mulint = cv2.normalize(mul, dst=None, alpha=0, beta=255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # again create 3-channel mask of float data type
    alpha = cv2.cvtColor(mulint[:,:,2], cv2.COLOR_GRAY2BGRA)/255.0

    # perform blending using previous output and multiplied result
    output = cv2.convertScaleAbs(
        cv2.add(b1i * (1 - alpha), mulint * (alpha))
    )

    return gammaCorrection(output, 0.7)

def get_mode(mode: str='Normal'):
    switch = {
        'Normal': normal,
        'Subtract': subtract,
        'Multiply': multiply,
        'Divide': divide
    }

    return switch['Normal'] if mode not in switch else switch[mode]