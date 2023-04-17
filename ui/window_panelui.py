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
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(73, 57)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.windowsFrame = QFrame(Form)
        self.windowsFrame.setObjectName(u"windowsFrame")
        self.windowsFrame.setFrameShape(QFrame.StyledPanel)
        self.windowsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.windowsFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.windowsFrame)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 4, 10, 4)
        self.grabHandleWidget = QWidget(self.widget)
        self.grabHandleWidget.setObjectName(u"grabHandleWidget")
        self.grabHandleWidget.setMinimumSize(QSize(0, 14))
        self.grabHandleWidget.setMaximumSize(QSize(16777215, 20))
        self.grabHandleWidget.setStyleSheet(u"background: pink")

        self.gridLayout_2.addWidget(self.grabHandleWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.buttonLocationWidget = QWidget(self.windowsFrame)
        self.buttonLocationWidget.setObjectName(u"buttonLocationWidget")

        self.verticalLayout.addWidget(self.buttonLocationWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.windowsFrame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

