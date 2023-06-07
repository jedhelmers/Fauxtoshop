# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base.ui'
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

class Ui_BaseOptions(object):
    def setupUi(self, BaseOptions):
        if not BaseOptions.objectName():
            BaseOptions.setObjectName(u"BaseOptions")
        BaseOptions.resize(873, 38)
        BaseOptions.setMinimumSize(QSize(0, 38))
        BaseOptions.setMaximumSize(QSize(16777215, 38))
        self.gridLayout = QGridLayout(BaseOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.retranslateUi(BaseOptions)

        QMetaObject.connectSlotsByName(BaseOptions)
    # setupUi

    def retranslateUi(self, BaseOptions):
        BaseOptions.setWindowTitle(QCoreApplication.translate("BaseOptions", u"Form", None))
    # retranslateUi

