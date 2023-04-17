# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windows.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Windows(object):
    def setupUi(self, Windows):
        if not Windows.objectName():
            Windows.setObjectName(u"Windows")
        Windows.resize(73, 344)
        self.gridLayout = QGridLayout(Windows)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.windowsWidget = QWidget(Windows)
        self.windowsWidget.setObjectName(u"windowsWidget")
        self.windowsWidget.setMinimumSize(QSize(40, 0))
        self.windowsWidget.setMaximumSize(QSize(40, 16777215))
        self.verticalLayout = QVBoxLayout(self.windowsWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 2)
        self.verticalSpacer = QSpacerItem(20, 425, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.windowsWidget, 0, 0, 1, 1)


        self.retranslateUi(Windows)

        QMetaObject.connectSlotsByName(Windows)
    # setupUi

    def retranslateUi(self, Windows):
        Windows.setWindowTitle(QCoreApplication.translate("Windows", u"Form", None))
    # retranslateUi

