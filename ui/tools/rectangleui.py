# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rectangle.ui'
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

class Ui_RectangleOptions(object):
    def setupUi(self, RectangleOptions):
        if not RectangleOptions.objectName():
            RectangleOptions.setObjectName(u"RectangleOptions")
        RectangleOptions.resize(873, 38)
        RectangleOptions.setMinimumSize(QSize(0, 38))
        RectangleOptions.setMaximumSize(QSize(16777215, 38))
        self.gridLayout = QGridLayout(RectangleOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.RectangleOptionsWidget = QWidget(RectangleOptions)
        self.RectangleOptionsWidget.setObjectName(u"RectangleOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.RectangleOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.RectangleOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(RectangleOptions)

        QMetaObject.connectSlotsByName(RectangleOptions)
    # setupUi

    def retranslateUi(self, RectangleOptions):
        RectangleOptions.setWindowTitle(QCoreApplication.translate("RectangleOptions", u"Form", None))
    # retranslateUi

