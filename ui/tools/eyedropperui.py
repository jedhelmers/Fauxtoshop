# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eyedropper.ui'
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

class Ui_EyedropperOptions(object):
    def setupUi(self, EyedropperOptions):
        if not EyedropperOptions.objectName():
            EyedropperOptions.setObjectName(u"EyedropperOptions")
        EyedropperOptions.resize(873, 38)
        EyedropperOptions.setMinimumSize(QSize(0, 38))
        EyedropperOptions.setMaximumSize(QSize(16777215, 38))
        self.gridLayout = QGridLayout(EyedropperOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.EyedropperOptionsWidget = QWidget(EyedropperOptions)
        self.EyedropperOptionsWidget.setObjectName(u"EyedropperOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.EyedropperOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.EyedropperOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(EyedropperOptions)

        QMetaObject.connectSlotsByName(EyedropperOptions)
    # setupUi

    def retranslateUi(self, EyedropperOptions):
        EyedropperOptions.setWindowTitle(QCoreApplication.translate("EyedropperOptions", u"Form", None))
    # retranslateUi

