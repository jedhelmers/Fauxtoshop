# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'brush.ui'
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

class Ui_BrushOptions(object):
    def setupUi(self, BrushOptions):
        if not BrushOptions.objectName():
            BrushOptions.setObjectName(u"BrushOptions")
        BrushOptions.resize(873, 44)
        self.gridLayout = QGridLayout(BrushOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.BrushOptionsWidget = QWidget(BrushOptions)
        self.BrushOptionsWidget.setObjectName(u"BrushOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.BrushOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.BrushOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(BrushOptions)

        QMetaObject.connectSlotsByName(BrushOptions)
    # setupUi

    def retranslateUi(self, BrushOptions):
        BrushOptions.setWindowTitle(QCoreApplication.translate("BrushOptions", u"Form", None))
    # retranslateUi

