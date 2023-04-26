# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashed_box.ui'
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

class Ui_DashedBoxOptions(object):
    def setupUi(self, DashedBoxOptions):
        if not DashedBoxOptions.objectName():
            DashedBoxOptions.setObjectName(u"DashedBoxOptions")
        DashedBoxOptions.resize(873, 38)
        DashedBoxOptions.setMinimumSize(QSize(0, 38))
        DashedBoxOptions.setMaximumSize(QSize(16777215, 38))
        self.gridLayout = QGridLayout(DashedBoxOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.DashedBoxOptionsWidget = QWidget(DashedBoxOptions)
        self.DashedBoxOptionsWidget.setObjectName(u"DashedBoxOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.DashedBoxOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.DashedBoxOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(DashedBoxOptions)

        QMetaObject.connectSlotsByName(DashedBoxOptions)
    # setupUi

    def retranslateUi(self, DashedBoxOptions):
        DashedBoxOptions.setWindowTitle(QCoreApplication.translate("DashedBoxOptions", u"Form", None))
    # retranslateUi

