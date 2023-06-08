# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eraser.ui'
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

class Ui_EraserOptions(object):
    def setupUi(self, EraserOptions):
        if not EraserOptions.objectName():
            EraserOptions.setObjectName(u"EraserOptions")
        EraserOptions.resize(873, 38)
        EraserOptions.setMinimumSize(QSize(0, 38))
        EraserOptions.setMaximumSize(QSize(16777215, 38))
        self.gridLayout = QGridLayout(EraserOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.EraserOptionsWidget = QWidget(EraserOptions)
        self.EraserOptionsWidget.setObjectName(u"EraserOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.EraserOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.EraserOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(EraserOptions)

        QMetaObject.connectSlotsByName(EraserOptions)
    # setupUi

    def retranslateUi(self, EraserOptions):
        EraserOptions.setWindowTitle(QCoreApplication.translate("EraserOptions", u"Form", None))
    # retranslateUi

