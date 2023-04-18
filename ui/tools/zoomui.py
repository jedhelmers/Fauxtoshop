# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zoom.ui'
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

class Ui_ZoomOptions(object):
    def setupUi(self, ZoomOptions):
        if not ZoomOptions.objectName():
            ZoomOptions.setObjectName(u"ZoomOptions")
        ZoomOptions.resize(873, 44)
        self.gridLayout = QGridLayout(ZoomOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ZoomOptionsWidget = QWidget(ZoomOptions)
        self.ZoomOptionsWidget.setObjectName(u"ZoomOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.ZoomOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.ZoomOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(ZoomOptions)

        QMetaObject.connectSlotsByName(ZoomOptions)
    # setupUi

    def retranslateUi(self, ZoomOptions):
        ZoomOptions.setWindowTitle(QCoreApplication.translate("ZoomOptions", u"Form", None))
    # retranslateUi

