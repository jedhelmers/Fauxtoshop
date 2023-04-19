# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'move.ui'
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

class Ui_MoveOptions(object):
    def setupUi(self, MoveOptions):
        if not MoveOptions.objectName():
            MoveOptions.setObjectName(u"MoveOptions")
        MoveOptions.resize(873, 38)
        MoveOptions.setMinimumSize(QSize(0, 38))
        MoveOptions.setMaximumSize(QSize(16777215, 38))
        self.gridLayout = QGridLayout(MoveOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MoveOptionsWidget = QWidget(MoveOptions)
        self.MoveOptionsWidget.setObjectName(u"MoveOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.MoveOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.MoveOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(MoveOptions)

        QMetaObject.connectSlotsByName(MoveOptions)
    # setupUi

    def retranslateUi(self, MoveOptions):
        MoveOptions.setWindowTitle(QCoreApplication.translate("MoveOptions", u"Form", None))
    # retranslateUi

