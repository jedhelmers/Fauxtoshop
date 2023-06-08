# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layer.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import resources_rc

class Ui_LayerWidget(object):
    def setupUi(self, LayerWidget):
        if not LayerWidget.objectName():
            LayerWidget.setObjectName(u"LayerWidget")
        LayerWidget.resize(179, 32)
        LayerWidget.setMinimumSize(QSize(0, 32))
        self.gridLayout_2 = QGridLayout(LayerWidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.layerWidget = QWidget(LayerWidget)
        self.layerWidget.setObjectName(u"layerWidget")
        self.layerWidget.setMinimumSize(QSize(0, 32))
        self.horizontalLayout_2 = QHBoxLayout(self.layerWidget)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.hideWidget = QWidget(self.layerWidget)
        self.hideWidget.setObjectName(u"hideWidget")
        self.hideWidget.setMinimumSize(QSize(30, 30))
        self.hideWidget.setMaximumSize(QSize(30, 16777215))
        self.gridLayout = QGridLayout(self.hideWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.hidePushButton = QPushButton(self.hideWidget)
        self.hidePushButton.setObjectName(u"hidePushButton")
        self.hidePushButton.setMinimumSize(QSize(13, 13))
        self.hidePushButton.setMaximumSize(QSize(13, 13))
        icon = QIcon()
        icon.addFile(u":/images/images/window_eye.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.hidePushButton.setIcon(icon)

        self.gridLayout.addWidget(self.hidePushButton, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.hideWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, -1, 4, -1)
        self.thumbnailWidget = QWidget(self.layerWidget)
        self.thumbnailWidget.setObjectName(u"thumbnailWidget")
        self.thumbnailWidget.setMinimumSize(QSize(32, 25))
        self.thumbnailWidget.setMaximumSize(QSize(32, 25))
        self.thumbnailWidget.setStyleSheet(u"background: white;")

        self.horizontalLayout.addWidget(self.thumbnailWidget)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.layerNameLabel = QLabel(self.layerWidget)
        self.layerNameLabel.setObjectName(u"layerNameLabel")

        self.horizontalLayout_2.addWidget(self.layerNameLabel)

        self.horizontalSpacer = QSpacerItem(19, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.layerOptionsWidget = QWidget(self.layerWidget)
        self.layerOptionsWidget.setObjectName(u"layerOptionsWidget")
        self.layerOptionsWidget.setMinimumSize(QSize(0, 32))
        self.layerOptionsWidget.setMaximumSize(QSize(32, 16777215))

        self.horizontalLayout_2.addWidget(self.layerOptionsWidget)


        self.gridLayout_2.addWidget(self.layerWidget, 0, 0, 1, 1)


        self.retranslateUi(LayerWidget)

        QMetaObject.connectSlotsByName(LayerWidget)
    # setupUi

    def retranslateUi(self, LayerWidget):
        LayerWidget.setWindowTitle(QCoreApplication.translate("LayerWidget", u"Form", None))
        self.hidePushButton.setText("")
        self.layerNameLabel.setText(QCoreApplication.translate("LayerWidget", u"Layer Name", None))
    # retranslateUi

