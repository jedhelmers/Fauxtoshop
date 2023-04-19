# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pointer_finger.ui'
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

class Ui_PointerFingerOptions(object):
    def setupUi(self, PointerFingerOptions):
        if not PointerFingerOptions.objectName():
            PointerFingerOptions.setObjectName(u"PointerFingerOptions")
        PointerFingerOptions.resize(873, 38)
        PointerFingerOptions.setMinimumSize(QSize(0, 38))
        PointerFingerOptions.setMaximumSize(QSize(16777215, 38))
        self.gridLayout = QGridLayout(PointerFingerOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.PointerFingerOptionsWidget = QWidget(PointerFingerOptions)
        self.PointerFingerOptionsWidget.setObjectName(u"PointerFingerOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.PointerFingerOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.PointerFingerOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(PointerFingerOptions)

        QMetaObject.connectSlotsByName(PointerFingerOptions)
    # setupUi

    def retranslateUi(self, PointerFingerOptions):
        PointerFingerOptions.setWindowTitle(QCoreApplication.translate("PointerFingerOptions", u"Form", None))
    # retranslateUi

