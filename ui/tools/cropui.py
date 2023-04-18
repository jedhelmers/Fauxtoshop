# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crop.ui'
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

class Ui_CropOptions(object):
    def setupUi(self, CropOptions):
        if not CropOptions.objectName():
            CropOptions.setObjectName(u"CropOptions")
        CropOptions.resize(873, 44)
        self.gridLayout = QGridLayout(CropOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.CropOptionsWidget = QWidget(CropOptions)
        self.CropOptionsWidget.setObjectName(u"CropOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.CropOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.CropOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(CropOptions)

        QMetaObject.connectSlotsByName(CropOptions)
    # setupUi

    def retranslateUi(self, CropOptions):
        CropOptions.setWindowTitle(QCoreApplication.translate("CropOptions", u"Form", None))
    # retranslateUi

