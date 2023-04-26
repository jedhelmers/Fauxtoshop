# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pin.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QWidget)
import resources_rc

class Ui_PinOptions(object):
    def setupUi(self, PinOptions):
        if not PinOptions.objectName():
            PinOptions.setObjectName(u"PinOptions")
        PinOptions.resize(873, 38)
        PinOptions.setMinimumSize(QSize(0, 38))
        PinOptions.setMaximumSize(QSize(16777215, 38))
        self.gridLayout = QGridLayout(PinOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.PinOptionsWidget = QWidget(PinOptions)
        self.PinOptionsWidget.setObjectName(u"PinOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.PinOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.PinOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(PinOptions)

        QMetaObject.connectSlotsByName(PinOptions)
    # setupUi

    def retranslateUi(self, PinOptions):
        PinOptions.setWindowTitle(QCoreApplication.translate("PinOptions", u"Form", None))
    # retranslateUi

