# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rotate_view.ui'
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

class Ui_RotateViewOptions(object):
    def setupUi(self, RotateViewOptions):
        if not RotateViewOptions.objectName():
            RotateViewOptions.setObjectName(u"RotateViewOptions")
        RotateViewOptions.resize(873, 38)
        RotateViewOptions.setMinimumSize(QSize(0, 38))
        RotateViewOptions.setMaximumSize(QSize(16777215, 38))
        self.gridLayout = QGridLayout(RotateViewOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.RotateViewOptionsWidget = QWidget(RotateViewOptions)
        self.RotateViewOptionsWidget.setObjectName(u"RotateViewOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.RotateViewOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.RotateViewOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(RotateViewOptions)

        QMetaObject.connectSlotsByName(RotateViewOptions)
    # setupUi

    def retranslateUi(self, RotateViewOptions):
        RotateViewOptions.setWindowTitle(QCoreApplication.translate("RotateViewOptions", u"Form", None))
    # retranslateUi

