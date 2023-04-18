# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'polygon_lasso.ui'
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

class Ui_PolygonLassoOptions(object):
    def setupUi(self, PolygonLassoOptions):
        if not PolygonLassoOptions.objectName():
            PolygonLassoOptions.setObjectName(u"PolygonLassoOptions")
        PolygonLassoOptions.resize(873, 44)
        self.gridLayout = QGridLayout(PolygonLassoOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.PolygonLassoOptionsWidget = QWidget(PolygonLassoOptions)
        self.PolygonLassoOptionsWidget.setObjectName(u"PolygonLassoOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.PolygonLassoOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.PolygonLassoOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(PolygonLassoOptions)

        QMetaObject.connectSlotsByName(PolygonLassoOptions)
    # setupUi

    def retranslateUi(self, PolygonLassoOptions):
        PolygonLassoOptions.setWindowTitle(QCoreApplication.translate("PolygonLassoOptions", u"Form", None))
    # retranslateUi

