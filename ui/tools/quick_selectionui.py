# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quick_selection.ui'
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

class Ui_QuickSelectionOptions(object):
    def setupUi(self, QuickSelectionOptions):
        if not QuickSelectionOptions.objectName():
            QuickSelectionOptions.setObjectName(u"QuickSelectionOptions")
        QuickSelectionOptions.resize(873, 38)
        QuickSelectionOptions.setMinimumSize(QSize(0, 38))
        QuickSelectionOptions.setMaximumSize(QSize(16777215, 38))
        self.gridLayout = QGridLayout(QuickSelectionOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.QuickSelectionOptionsWidget = QWidget(QuickSelectionOptions)
        self.QuickSelectionOptionsWidget.setObjectName(u"QuickSelectionOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.QuickSelectionOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.QuickSelectionOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(QuickSelectionOptions)

        QMetaObject.connectSlotsByName(QuickSelectionOptions)
    # setupUi

    def retranslateUi(self, QuickSelectionOptions):
        QuickSelectionOptions.setWindowTitle(QCoreApplication.translate("QuickSelectionOptions", u"Form", None))
    # retranslateUi

