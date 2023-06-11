# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spot_headling.ui'
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

class Ui_SpotHeadlingOptions(object):
    def setupUi(self, SpotHeadlingOptions):
        if not SpotHeadlingOptions.objectName():
            SpotHeadlingOptions.setObjectName(u"SpotHeadlingOptions")
        SpotHeadlingOptions.resize(873, 38)
        SpotHeadlingOptions.setMinimumSize(QSize(0, 38))
        SpotHeadlingOptions.setMaximumSize(QSize(16777215, 38))
        self.gridLayout = QGridLayout(SpotHeadlingOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.SpotHeadlingOptionsWidget = QWidget(SpotHeadlingOptions)
        self.SpotHeadlingOptionsWidget.setObjectName(u"SpotHeadlingOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.SpotHeadlingOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.SpotHeadlingOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(SpotHeadlingOptions)

        QMetaObject.connectSlotsByName(SpotHeadlingOptions)
    # setupUi

    def retranslateUi(self, SpotHeadlingOptions):
        SpotHeadlingOptions.setWindowTitle(QCoreApplication.translate("SpotHeadlingOptions", u"Form", None))
    # retranslateUi

