# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'toolbar.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Toolbar(object):
    def setupUi(self, Toolbar):
        if not Toolbar.objectName():
            Toolbar.setObjectName(u"Toolbar")
        Toolbar.resize(73, 344)
        self.gridLayout = QGridLayout(Toolbar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.toolbarWidget = QWidget(Toolbar)
        self.toolbarWidget.setObjectName(u"toolbarWidget")
        self.toolbarWidget.setMinimumSize(QSize(40, 0))
        self.toolbarWidget.setMaximumSize(QSize(40, 16777215))
        self.verticalLayout = QVBoxLayout(self.toolbarWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 2)

        self.gridLayout.addWidget(self.toolbarWidget, 0, 0, 1, 1)


        self.retranslateUi(Toolbar)

        QMetaObject.connectSlotsByName(Toolbar)
    # setupUi

    def retranslateUi(self, Toolbar):
        Toolbar.setWindowTitle(QCoreApplication.translate("Toolbar", u"Form", None))
    # retranslateUi

