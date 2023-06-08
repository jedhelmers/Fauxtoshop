# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frame.ui'
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

class Ui_FrameOptions(object):
    def setupUi(self, FrameOptions):
        if not FrameOptions.objectName():
            FrameOptions.setObjectName(u"FrameOptions")
        FrameOptions.resize(873, 38)
        FrameOptions.setMinimumSize(QSize(0, 38))
        FrameOptions.setMaximumSize(QSize(16777215, 38))
        self.gridLayout = QGridLayout(FrameOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.FrameOptionsWidget = QWidget(FrameOptions)
        self.FrameOptionsWidget.setObjectName(u"FrameOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.FrameOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.FrameOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(FrameOptions)

        QMetaObject.connectSlotsByName(FrameOptions)
    # setupUi

    def retranslateUi(self, FrameOptions):
        FrameOptions.setWindowTitle(QCoreApplication.translate("FrameOptions", u"Form", None))
    # retranslateUi

