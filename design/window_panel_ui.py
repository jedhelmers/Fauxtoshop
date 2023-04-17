# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_panel.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_PanelWidget(object):
    def setupUi(self, PanelWidget):
        if not PanelWidget.objectName():
            PanelWidget.setObjectName(u"PanelWidget")
        PanelWidget.resize(73, 26)
        self.verticalLayout_2 = QVBoxLayout(PanelWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 4)
        self.windowsFrame = QFrame(PanelWidget)
        self.windowsFrame.setObjectName(u"windowsFrame")
        self.windowsFrame.setFrameShape(QFrame.StyledPanel)
        self.windowsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.windowsFrame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.windowsFrame)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setStyleSheet(u"border-radius: 2px;")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.grabHandleWidget = QWidget(self.widget)
        self.grabHandleWidget.setObjectName(u"grabHandleWidget")
        self.grabHandleWidget.setMinimumSize(QSize(0, 10))
        self.grabHandleWidget.setMaximumSize(QSize(16777215, 10))
        self.grabHandleWidget.setStyleSheet(u"background: rgba(255, 255, 255, 0.25)")

        self.verticalLayout_3.addWidget(self.grabHandleWidget)


        self.verticalLayout.addWidget(self.widget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.windowsFrame)


        self.retranslateUi(PanelWidget)

        QMetaObject.connectSlotsByName(PanelWidget)
    # setupUi

    def retranslateUi(self, PanelWidget):
        PanelWidget.setWindowTitle(QCoreApplication.translate("PanelWidget", u"Form", None))
    # retranslateUi

