# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template.ui'
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

class Ui_UI_NAMEOptions(object):
    def setupUi(self, UI_NAMEOptions):
        if not UI_NAMEOptions.objectName():
            UI_NAMEOptions.setObjectName(u"UI_NAMEOptions")
        UI_NAMEOptions.resize(873, 44)
        self.gridLayout = QGridLayout(UI_NAMEOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.UI_NAMEOptionsWidget = QWidget(UI_NAMEOptions)
        self.UI_NAMEOptionsWidget.setObjectName(u"UI_NAMEOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.UI_NAMEOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.UI_NAMEOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(UI_NAMEOptions)

        QMetaObject.connectSlotsByName(UI_NAMEOptions)
    # setupUi

    def retranslateUi(self, UI_NAMEOptions):
        UI_NAMEOptions.setWindowTitle(QCoreApplication.translate("UI_NAMEOptions", u"Form", None))
    # retranslateUi

