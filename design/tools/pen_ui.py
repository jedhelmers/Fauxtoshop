# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pen.ui'
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

class Ui_PenOptions(object):
    def setupUi(self, PenOptions):
        if not PenOptions.objectName():
            PenOptions.setObjectName(u"PenOptions")
        PenOptions.resize(873, 44)
        self.gridLayout = QGridLayout(PenOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.PenOptionsWidget = QWidget(PenOptions)
        self.PenOptionsWidget.setObjectName(u"PenOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.PenOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.PenOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(PenOptions)

        QMetaObject.connectSlotsByName(PenOptions)
    # setupUi

    def retranslateUi(self, PenOptions):
        PenOptions.setWindowTitle(QCoreApplication.translate("PenOptions", u"Form", None))
    # retranslateUi

