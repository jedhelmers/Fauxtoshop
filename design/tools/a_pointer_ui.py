# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'a_pointer.ui'
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

class Ui_APointerOptions(object):
    def setupUi(self, APointerOptions):
        if not APointerOptions.objectName():
            APointerOptions.setObjectName(u"APointerOptions")
        APointerOptions.resize(873, 44)
        self.gridLayout = QGridLayout(APointerOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.APointerOptionsWidget = QWidget(APointerOptions)
        self.APointerOptionsWidget.setObjectName(u"APointerOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.APointerOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.APointerOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(APointerOptions)

        QMetaObject.connectSlotsByName(APointerOptions)
    # setupUi

    def retranslateUi(self, APointerOptions):
        APointerOptions.setWindowTitle(QCoreApplication.translate("APointerOptions", u"Form", None))
    # retranslateUi

