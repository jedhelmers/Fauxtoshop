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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import resources_rc
import resources_rc

class Ui_LayerWidget(object):
    def setupUi(self, LayerWidget):
        if not LayerWidget.objectName():
            LayerWidget.setObjectName(u"LayerWidget")
        LayerWidget.resize(192, 32)
        LayerWidget.setMinimumSize(QSize(0, 32))
        self.gridLayout_2 = QGridLayout(LayerWidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.layerRowWidget = QWidget(LayerWidget)
        self.layerRowWidget.setObjectName(u"layerRowWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.layerRowWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 12, 0)
        self.frame_2 = QFrame(self.layerRowWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(30, 30))
        self.frame_2.setMaximumSize(QSize(30, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.hidePushButton = QPushButton(self.frame_2)
        self.hidePushButton.setObjectName(u"hidePushButton")
        self.hidePushButton.setMinimumSize(QSize(30, 30))
        self.hidePushButton.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/images/images/window_show.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.hidePushButton.setIcon(icon)
        self.hidePushButton.setFlat(True)

        self.gridLayout.addWidget(self.hidePushButton, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, -1, 4, -1)
        self.thumbnailWidget = QWidget(self.layerRowWidget)
        self.thumbnailWidget.setObjectName(u"thumbnailWidget")
        self.thumbnailWidget.setMinimumSize(QSize(32, 25))
        self.thumbnailWidget.setMaximumSize(QSize(32, 25))

        self.horizontalLayout.addWidget(self.thumbnailWidget)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.layerNameLabel = QLabel(self.layerRowWidget)
        self.layerNameLabel.setObjectName(u"layerNameLabel")

        self.horizontalLayout_2.addWidget(self.layerNameLabel)

        self.horizontalSpacer = QSpacerItem(19, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lockLabel = QLabel(self.layerRowWidget)
        self.lockLabel.setObjectName(u"lockLabel")
        self.lockLabel.setMinimumSize(QSize(15, 15))
        self.lockLabel.setMaximumSize(QSize(15, 15))
        self.lockLabel.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.lockLabel)

        self.layerOptionsWidget = QWidget(self.layerRowWidget)
        self.layerOptionsWidget.setObjectName(u"layerOptionsWidget")
        self.layerOptionsWidget.setMinimumSize(QSize(0, 32))
        self.layerOptionsWidget.setMaximumSize(QSize(32, 16777215))

        self.horizontalLayout_2.addWidget(self.layerOptionsWidget)


        self.gridLayout_2.addWidget(self.layerRowWidget, 0, 0, 1, 1)


        self.retranslateUi(LayerWidget)

        QMetaObject.connectSlotsByName(LayerWidget)
    # setupUi

    def retranslateUi(self, LayerWidget):
        LayerWidget.setWindowTitle(QCoreApplication.translate("LayerWidget", u"Form", None))
        self.hidePushButton.setText("")
        self.layerNameLabel.setText(QCoreApplication.translate("LayerWidget", u"Layer Name", None))
        self.lockLabel.setText("")
    # retranslateUi

