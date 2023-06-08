# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gradient.ui'
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

class Ui_GradientOptions(object):
    def setupUi(self, GradientOptions):
        if not GradientOptions.objectName():
            GradientOptions.setObjectName(u"GradientOptions")
        GradientOptions.resize(873, 38)
        GradientOptions.setMinimumSize(QSize(0, 38))
        GradientOptions.setMaximumSize(QSize(16777215, 38))
        self.gridLayout = QGridLayout(GradientOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.GradientOptionsWidget = QWidget(GradientOptions)
        self.GradientOptionsWidget.setObjectName(u"GradientOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.GradientOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.GradientOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(GradientOptions)

        QMetaObject.connectSlotsByName(GradientOptions)
    # setupUi

    def retranslateUi(self, GradientOptions):
        GradientOptions.setWindowTitle(QCoreApplication.translate("GradientOptions", u"Form", None))
    # retranslateUi

