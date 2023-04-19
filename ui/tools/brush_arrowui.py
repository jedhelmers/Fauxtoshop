# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'brush_arrow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QWidget)
import resources_rc

class Ui_BrushArrowOptions(object):
    def setupUi(self, BrushArrowOptions):
        if not BrushArrowOptions.objectName():
            BrushArrowOptions.setObjectName(u"BrushArrowOptions")
        BrushArrowOptions.resize(873, 38)
        BrushArrowOptions.setMinimumSize(QSize(0, 38))
        BrushArrowOptions.setMaximumSize(QSize(16777215, 38))
        self.gridLayout = QGridLayout(BrushArrowOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.BrushArrowOptionsWidget = QWidget(BrushArrowOptions)
        self.BrushArrowOptionsWidget.setObjectName(u"BrushArrowOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.BrushArrowOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.BrushArrowOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(BrushArrowOptions)

        QMetaObject.connectSlotsByName(BrushArrowOptions)
    # setupUi

    def retranslateUi(self, BrushArrowOptions):
        BrushArrowOptions.setWindowTitle(QCoreApplication.translate("BrushArrowOptions", u"Form", None))
    # retranslateUi

