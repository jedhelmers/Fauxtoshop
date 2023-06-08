# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'color_picker.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ColorPicker(object):
    def setupUi(self, ColorPicker):
        if not ColorPicker.objectName():
            ColorPicker.setObjectName(u"ColorPicker")
        ColorPicker.resize(546, 347)
        self.onlyWebColorsCheckBox = QCheckBox(ColorPicker)
        self.onlyWebColorsCheckBox.setObjectName(u"onlyWebColorsCheckBox")
        self.onlyWebColorsCheckBox.setGeometry(QRect(10, 290, 281, 20))
        self.widget = QWidget(ColorPicker)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 287, 257))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.colorRangeWidget = QWidget(self.widget)
        self.colorRangeWidget.setObjectName(u"colorRangeWidget")
        self.colorRangeWidget.setMinimumSize(QSize(255, 255))
        self.colorRangeWidget.setMaximumSize(QSize(255, 255))
        self.colorRangeWidget.setStyleSheet(u"background: rgba(255, 255, 255, 100)")

        self.horizontalLayout_4.addWidget(self.colorRangeWidget)

        self.hueScaleWidget = QWidget(self.widget)
        self.hueScaleWidget.setObjectName(u"hueScaleWidget")
        self.hueScaleWidget.setMinimumSize(QSize(20, 255))
        self.hueScaleWidget.setMaximumSize(QSize(20, 16777215))
        self.hueScaleWidget.setStyleSheet(u"background: rgba(255, 255, 255, 100)")

        self.horizontalLayout_4.addWidget(self.hueScaleWidget)

        self.widget1 = QWidget(ColorPicker)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(309, 140, 221, 192))
        self.horizontalLayout_16 = QHBoxLayout(self.widget1)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 4, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton = QRadioButton(self.widget1)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.hueLineEdit = QLineEdit(self.widget1)
        self.hueLineEdit.setObjectName(u"hueLineEdit")
        self.hueLineEdit.setMinimumSize(QSize(36, 0))
        self.hueLineEdit.setMaximumSize(QSize(36, 16777215))

        self.horizontalLayout.addWidget(self.hueLineEdit)

        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_2 = QRadioButton(self.widget1)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.saturationLineEdit = QLineEdit(self.widget1)
        self.saturationLineEdit.setObjectName(u"saturationLineEdit")
        self.saturationLineEdit.setMinimumSize(QSize(36, 0))
        self.saturationLineEdit.setMaximumSize(QSize(36, 16777215))

        self.horizontalLayout_2.addWidget(self.saturationLineEdit)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_3 = QRadioButton(self.widget1)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_3.addWidget(self.radioButton_3)

        self.brightnessLineEdit = QLineEdit(self.widget1)
        self.brightnessLineEdit.setObjectName(u"brightnessLineEdit")
        self.brightnessLineEdit.setMinimumSize(QSize(36, 0))
        self.brightnessLineEdit.setMaximumSize(QSize(36, 16777215))

        self.horizontalLayout_3.addWidget(self.brightnessLineEdit)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioButton_4 = QRadioButton(self.widget1)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_5.addWidget(self.radioButton_4)

        self.redLineEdit = QLineEdit(self.widget1)
        self.redLineEdit.setObjectName(u"redLineEdit")
        self.redLineEdit.setMinimumSize(QSize(36, 0))
        self.redLineEdit.setMaximumSize(QSize(36, 16777215))

        self.horizontalLayout_5.addWidget(self.redLineEdit)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton_5 = QRadioButton(self.widget1)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_6.addWidget(self.radioButton_5)

        self.greenLineEdit = QLineEdit(self.widget1)
        self.greenLineEdit.setObjectName(u"greenLineEdit")
        self.greenLineEdit.setMinimumSize(QSize(36, 0))
        self.greenLineEdit.setMaximumSize(QSize(36, 16777215))

        self.horizontalLayout_6.addWidget(self.greenLineEdit)

        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.radioButton_6 = QRadioButton(self.widget1)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_7.addWidget(self.radioButton_6)

        self.blueLineEdit = QLineEdit(self.widget1)
        self.blueLineEdit.setObjectName(u"blueLineEdit")
        self.blueLineEdit.setMinimumSize(QSize(36, 0))
        self.blueLineEdit.setMaximumSize(QSize(36, 16777215))

        self.horizontalLayout_7.addWidget(self.blueLineEdit)

        self.label_7 = QLabel(self.widget1)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_16 = QLabel(self.widget1)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_15.addWidget(self.label_16)

        self.hexLineEdit = QLineEdit(self.widget1)
        self.hexLineEdit.setObjectName(u"hexLineEdit")
        self.hexLineEdit.setMinimumSize(QSize(80, 0))
        self.hexLineEdit.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_15.addWidget(self.hexLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_16.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 4, -1, -1)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.radioButton_12 = QRadioButton(self.widget1)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.horizontalLayout_13.addWidget(self.radioButton_12)

        self.luminanceLineEdit = QLineEdit(self.widget1)
        self.luminanceLineEdit.setObjectName(u"luminanceLineEdit")
        self.luminanceLineEdit.setMinimumSize(QSize(42, 0))
        self.luminanceLineEdit.setMaximumSize(QSize(42, 16777215))

        self.horizontalLayout_13.addWidget(self.luminanceLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.radioButton_9 = QRadioButton(self.widget1)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.horizontalLayout_10.addWidget(self.radioButton_9)

        self.alphaChannelLineEdit = QLineEdit(self.widget1)
        self.alphaChannelLineEdit.setObjectName(u"alphaChannelLineEdit")
        self.alphaChannelLineEdit.setMinimumSize(QSize(42, 0))
        self.alphaChannelLineEdit.setMaximumSize(QSize(42, 16777215))

        self.horizontalLayout_10.addWidget(self.alphaChannelLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.radioButton_10 = QRadioButton(self.widget1)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.horizontalLayout_11.addWidget(self.radioButton_10)

        self.betaChannelLineEdit = QLineEdit(self.widget1)
        self.betaChannelLineEdit.setObjectName(u"betaChannelLineEdit")
        self.betaChannelLineEdit.setMinimumSize(QSize(42, 0))
        self.betaChannelLineEdit.setMaximumSize(QSize(42, 16777215))

        self.horizontalLayout_11.addWidget(self.betaChannelLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_13 = QLabel(self.widget1)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_8.addWidget(self.label_13)

        self.cyanLineEdit = QLineEdit(self.widget1)
        self.cyanLineEdit.setObjectName(u"cyanLineEdit")
        self.cyanLineEdit.setMinimumSize(QSize(36, 0))
        self.cyanLineEdit.setMaximumSize(QSize(36, 16777215))

        self.horizontalLayout_8.addWidget(self.cyanLineEdit)

        self.label_8 = QLabel(self.widget1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(14, 0))
        self.label_8.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_8.addWidget(self.label_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.widget1)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.magentaLineEdit = QLineEdit(self.widget1)
        self.magentaLineEdit.setObjectName(u"magentaLineEdit")
        self.magentaLineEdit.setMinimumSize(QSize(36, 0))
        self.magentaLineEdit.setMaximumSize(QSize(36, 16777215))

        self.horizontalLayout_9.addWidget(self.magentaLineEdit)

        self.label_9 = QLabel(self.widget1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(14, 0))
        self.label_9.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_9.addWidget(self.label_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.widget1)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.yellowLineEdit = QLineEdit(self.widget1)
        self.yellowLineEdit.setObjectName(u"yellowLineEdit")
        self.yellowLineEdit.setMinimumSize(QSize(36, 0))
        self.yellowLineEdit.setMaximumSize(QSize(36, 16777215))

        self.horizontalLayout_12.addWidget(self.yellowLineEdit)

        self.label_12 = QLabel(self.widget1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(14, 0))
        self.label_12.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_12.addWidget(self.label_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.widget1)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.keyLineEdit = QLineEdit(self.widget1)
        self.keyLineEdit.setObjectName(u"keyLineEdit")
        self.keyLineEdit.setMinimumSize(QSize(36, 0))
        self.keyLineEdit.setMaximumSize(QSize(36, 16777215))

        self.horizontalLayout_14.addWidget(self.keyLineEdit)

        self.label_15 = QLabel(self.widget1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(14, 0))
        self.label_15.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout_14.addWidget(self.label_15)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_16.addLayout(self.verticalLayout_2)

        self.widget2 = QWidget(ColorPicker)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(310, 30, 62, 98))
        self.verticalLayout_3 = QVBoxLayout(self.widget2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.widget2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_17)

        self.newColorWidget = QWidget(self.widget2)
        self.newColorWidget.setObjectName(u"newColorWidget")
        self.newColorWidget.setMinimumSize(QSize(60, 32))
        self.newColorWidget.setMaximumSize(QSize(60, 32))
        self.newColorWidget.setStyleSheet(u"background: white")

        self.verticalLayout_3.addWidget(self.newColorWidget)

        self.currentColorWidget = QWidget(self.widget2)
        self.currentColorWidget.setObjectName(u"currentColorWidget")
        self.currentColorWidget.setMinimumSize(QSize(60, 32))
        self.currentColorWidget.setMaximumSize(QSize(60, 32))
        self.currentColorWidget.setStyleSheet(u"background: black")

        self.verticalLayout_3.addWidget(self.currentColorWidget)

        self.label_18 = QLabel(self.widget2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_18)

        self.widget3 = QWidget(ColorPicker)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(400, 10, 145, 134))
        self.verticalLayout_4 = QVBoxLayout(self.widget3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.okPushButton = QPushButton(self.widget3)
        self.okPushButton.setObjectName(u"okPushButton")

        self.verticalLayout_4.addWidget(self.okPushButton)

        self.cancelPushButton = QPushButton(self.widget3)
        self.cancelPushButton.setObjectName(u"cancelPushButton")

        self.verticalLayout_4.addWidget(self.cancelPushButton)

        self.addToSwatchesPushButton = QPushButton(self.widget3)
        self.addToSwatchesPushButton.setObjectName(u"addToSwatchesPushButton")

        self.verticalLayout_4.addWidget(self.addToSwatchesPushButton)

        self.colorLibrariesPushButton = QPushButton(self.widget3)
        self.colorLibrariesPushButton.setObjectName(u"colorLibrariesPushButton")

        self.verticalLayout_4.addWidget(self.colorLibrariesPushButton)


        self.retranslateUi(ColorPicker)

        QMetaObject.connectSlotsByName(ColorPicker)
    # setupUi

    def retranslateUi(self, ColorPicker):
        ColorPicker.setWindowTitle(QCoreApplication.translate("ColorPicker", u"Form", None))
        self.onlyWebColorsCheckBox.setText(QCoreApplication.translate("ColorPicker", u"Only Web Colors", None))
        self.radioButton.setText(QCoreApplication.translate("ColorPicker", u"H:", None))
        self.label_2.setText(QCoreApplication.translate("ColorPicker", u"\u00ba", None))
        self.radioButton_2.setText(QCoreApplication.translate("ColorPicker", u"S:", None))
        self.label_3.setText(QCoreApplication.translate("ColorPicker", u"%", None))
        self.radioButton_3.setText(QCoreApplication.translate("ColorPicker", u"B:", None))
        self.label_4.setText(QCoreApplication.translate("ColorPicker", u"%", None))
        self.radioButton_4.setText(QCoreApplication.translate("ColorPicker", u"R:", None))
        self.label_5.setText(QCoreApplication.translate("ColorPicker", u"\u00ba", None))
        self.radioButton_5.setText(QCoreApplication.translate("ColorPicker", u"G:", None))
        self.label_6.setText(QCoreApplication.translate("ColorPicker", u"\u00ba", None))
        self.radioButton_6.setText(QCoreApplication.translate("ColorPicker", u"B:", None))
        self.label_7.setText(QCoreApplication.translate("ColorPicker", u"\u00ba", None))
        self.label_16.setText(QCoreApplication.translate("ColorPicker", u"#", None))
        self.radioButton_12.setText(QCoreApplication.translate("ColorPicker", u"L:", None))
        self.radioButton_9.setText(QCoreApplication.translate("ColorPicker", u"a:", None))
        self.radioButton_10.setText(QCoreApplication.translate("ColorPicker", u"b:", None))
        self.label_13.setText(QCoreApplication.translate("ColorPicker", u"C:", None))
        self.label_8.setText(QCoreApplication.translate("ColorPicker", u"%", None))
        self.label_11.setText(QCoreApplication.translate("ColorPicker", u"M:", None))
        self.label_9.setText(QCoreApplication.translate("ColorPicker", u"%", None))
        self.label_10.setText(QCoreApplication.translate("ColorPicker", u"Y:", None))
        self.label_12.setText(QCoreApplication.translate("ColorPicker", u"%", None))
        self.label_14.setText(QCoreApplication.translate("ColorPicker", u"K:", None))
        self.label_15.setText(QCoreApplication.translate("ColorPicker", u"%", None))
        self.label_17.setText(QCoreApplication.translate("ColorPicker", u"new", None))
        self.label_18.setText(QCoreApplication.translate("ColorPicker", u"current", None))
        self.okPushButton.setText(QCoreApplication.translate("ColorPicker", u"OK", None))
        self.cancelPushButton.setText(QCoreApplication.translate("ColorPicker", u"Cancel", None))
        self.addToSwatchesPushButton.setText(QCoreApplication.translate("ColorPicker", u"Add to Swatches", None))
        self.colorLibrariesPushButton.setText(QCoreApplication.translate("ColorPicker", u"Color Libraries", None))
    # retranslateUi

