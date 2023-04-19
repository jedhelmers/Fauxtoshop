# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_flyout_panel.ui'
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
    QTabWidget, QVBoxLayout, QWidget)

class Ui_WindowPanel(object):
    def setupUi(self, WindowPanel):
        if not WindowPanel.objectName():
            WindowPanel.setObjectName(u"WindowPanel")
        WindowPanel.resize(296, 295)
        WindowPanel.setMaximumSize(QSize(296, 16777215))
        self.gridLayout = QGridLayout(WindowPanel)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(WindowPanel)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.windowPanelTitleBarWidget = QWidget(self.frame)
        self.windowPanelTitleBarWidget.setObjectName(u"windowPanelTitleBarWidget")
        self.windowPanelTitleBarWidget.setMinimumSize(QSize(0, 12))
        self.windowPanelTitleBarWidget.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout.addWidget(self.windowPanelTitleBarWidget)

        self.windowPanelTabWidget = QTabWidget(self.frame)
        self.windowPanelTabWidget.setObjectName(u"windowPanelTabWidget")
        self.windowPanelTabWidget.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.windowPanelTabWidget)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(WindowPanel)

        self.windowPanelTabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(WindowPanel)
    # setupUi

    def retranslateUi(self, WindowPanel):
        WindowPanel.setWindowTitle("")
    # retranslateUi

