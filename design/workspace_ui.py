# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'workspace.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Workspace(object):
    def setupUi(self, Workspace):
        if not Workspace.objectName():
            Workspace.setObjectName(u"Workspace")
        Workspace.resize(627, 459)
        self.gridLayout_2 = QGridLayout(Workspace)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(Workspace)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 623, 435))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(20, 0))
        self.widget.setMaximumSize(QSize(20, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topLeftRulerCornerWidget = QWidget(self.widget)
        self.topLeftRulerCornerWidget.setObjectName(u"topLeftRulerCornerWidget")
        self.topLeftRulerCornerWidget.setMinimumSize(QSize(20, 20))
        self.topLeftRulerCornerWidget.setMaximumSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.topLeftRulerCornerWidget)

        self.verticalRulerWidget = QWidget(self.widget)
        self.verticalRulerWidget.setObjectName(u"verticalRulerWidget")
        self.verticalRulerWidget.setMinimumSize(QSize(20, 0))
        self.verticalRulerWidget.setMaximumSize(QSize(20, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.verticalRulerWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addWidget(self.verticalRulerWidget)


        self.horizontalLayout.addWidget(self.widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalRulerWidget = QWidget(self.scrollAreaWidgetContents)
        self.horizontalRulerWidget.setObjectName(u"horizontalRulerWidget")
        self.horizontalRulerWidget.setMinimumSize(QSize(0, 20))
        self.horizontalRulerWidget.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalRulerWidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.horizontalRulerWidget)

        self.workspaceBackgroundWidget = QWidget(self.scrollAreaWidgetContents)
        self.workspaceBackgroundWidget.setObjectName(u"workspaceBackgroundWidget")

        self.verticalLayout.addWidget(self.workspaceBackgroundWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.informationBarWidget = QWidget(Workspace)
        self.informationBarWidget.setObjectName(u"informationBarWidget")
        self.informationBarWidget.setMinimumSize(QSize(0, 20))
        self.informationBarWidget.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.informationBarWidget)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(Workspace)

        QMetaObject.connectSlotsByName(Workspace)
    # setupUi

    def retranslateUi(self, Workspace):
        Workspace.setWindowTitle(QCoreApplication.translate("Workspace", u"Form", None))
    # retranslateUi

