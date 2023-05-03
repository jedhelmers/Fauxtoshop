# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layerswindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_LayersWindow(object):
    def setupUi(self, LayersWindow):
        if not LayersWindow.objectName():
            LayersWindow.setObjectName(u"LayersWindow")
        LayersWindow.resize(313, 273)
        LayersWindow.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(LayersWindow)
#ifndef Q_OS_MAC
        self.verticalLayout.setSpacing(-1)
#endif
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 0)
        self.layout = QWidget(LayersWindow)
        self.layout.setObjectName(u"layout")
        self.layout.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_2 = QHBoxLayout(self.layout)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 2, 0, 2)
        self.kindComboBox = QComboBox(self.layout)
        self.kindComboBox.setObjectName(u"kindComboBox")
        self.kindComboBox.setMaximumSize(QSize(100, 18))

        self.horizontalLayout_2.addWidget(self.kindComboBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pixelFilterLayersPushButton = QPushButton(self.layout)
        self.pixelFilterLayersPushButton.setObjectName(u"pixelFilterLayersPushButton")
        self.pixelFilterLayersPushButton.setMinimumSize(QSize(20, 20))
        self.pixelFilterLayersPushButton.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/images/images/window_filter_for_pixel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pixelFilterLayersPushButton.setIcon(icon)
        self.pixelFilterLayersPushButton.setIconSize(QSize(14, 14))

        self.horizontalLayout_2.addWidget(self.pixelFilterLayersPushButton)

        self.filterForAdjustmentLayersPushButton = QPushButton(self.layout)
        self.filterForAdjustmentLayersPushButton.setObjectName(u"filterForAdjustmentLayersPushButton")
        self.filterForAdjustmentLayersPushButton.setMinimumSize(QSize(20, 20))
        self.filterForAdjustmentLayersPushButton.setMaximumSize(QSize(20, 20))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/window_filter_for_adjustment.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.filterForAdjustmentLayersPushButton.setIcon(icon1)
        self.filterForAdjustmentLayersPushButton.setIconSize(QSize(14, 14))

        self.horizontalLayout_2.addWidget(self.filterForAdjustmentLayersPushButton)

        self.filterForTypeLayersPushButton = QPushButton(self.layout)
        self.filterForTypeLayersPushButton.setObjectName(u"filterForTypeLayersPushButton")
        self.filterForTypeLayersPushButton.setMinimumSize(QSize(20, 20))
        self.filterForTypeLayersPushButton.setMaximumSize(QSize(20, 20))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/window_filter_for_text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.filterForTypeLayersPushButton.setIcon(icon2)
        self.filterForTypeLayersPushButton.setIconSize(QSize(14, 14))

        self.horizontalLayout_2.addWidget(self.filterForTypeLayersPushButton)

        self.filterForShapesLayersPushButton = QPushButton(self.layout)
        self.filterForShapesLayersPushButton.setObjectName(u"filterForShapesLayersPushButton")
        self.filterForShapesLayersPushButton.setMinimumSize(QSize(20, 20))
        self.filterForShapesLayersPushButton.setMaximumSize(QSize(20, 20))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/window_filter_for_shape.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.filterForShapesLayersPushButton.setIcon(icon3)
        self.filterForShapesLayersPushButton.setIconSize(QSize(14, 14))

        self.horizontalLayout_2.addWidget(self.filterForShapesLayersPushButton)

        self.filterForSmartObjectsPushButton = QPushButton(self.layout)
        self.filterForSmartObjectsPushButton.setObjectName(u"filterForSmartObjectsPushButton")
        self.filterForSmartObjectsPushButton.setMinimumSize(QSize(20, 20))
        self.filterForSmartObjectsPushButton.setMaximumSize(QSize(20, 20))
        icon4 = QIcon()
        icon4.addFile(u":/images/images/window_filter_for_smart_object.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.filterForSmartObjectsPushButton.setIcon(icon4)
        self.filterForSmartObjectsPushButton.setIconSize(QSize(14, 14))

        self.horizontalLayout_2.addWidget(self.filterForSmartObjectsPushButton)


        self.verticalLayout.addWidget(self.layout)

        self.layout_2 = QWidget(LayersWindow)
        self.layout_2.setObjectName(u"layout_2")
        self.layout_2.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_4 = QHBoxLayout(self.layout_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 2, 0, 2)
        self.modeComboBox = QComboBox(self.layout_2)
        self.modeComboBox.setObjectName(u"modeComboBox")
        self.modeComboBox.setMinimumSize(QSize(110, 0))
        self.modeComboBox.setMaximumSize(QSize(16777215, 18))

        self.horizontalLayout_4.addWidget(self.modeComboBox)

        self.label_3 = QLabel(self.layout_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(40, 0))
        self.label_3.setMaximumSize(QSize(40, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.opacityComboBox = QComboBox(self.layout_2)
        self.opacityComboBox.setObjectName(u"opacityComboBox")
        self.opacityComboBox.setMinimumSize(QSize(50, 0))
        self.opacityComboBox.setMaximumSize(QSize(50, 18))
        self.opacityComboBox.setEditable(True)

        self.horizontalLayout_4.addWidget(self.opacityComboBox)


        self.verticalLayout.addWidget(self.layout_2)

        self.layout_4 = QWidget(LayersWindow)
        self.layout_4.setObjectName(u"layout_4")
        self.layout_4.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_3 = QHBoxLayout(self.layout_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 2, 0, 2)
        self.label = QLabel(self.layout_4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(27, 0))
        self.label.setMaximumSize(QSize(28, 16777215))
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.alphaLockPushButton = QPushButton(self.layout_4)
        self.alphaLockPushButton.setObjectName(u"alphaLockPushButton")
        self.alphaLockPushButton.setMinimumSize(QSize(20, 20))
        self.alphaLockPushButton.setMaximumSize(QSize(20, 20))
        icon5 = QIcon()
        icon5.addFile(u":/images/images/window_alpha_lock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.alphaLockPushButton.setIcon(icon5)
        self.alphaLockPushButton.setIconSize(QSize(14, 14))

        self.horizontalLayout_3.addWidget(self.alphaLockPushButton)

        self.pixelLockPushButton = QPushButton(self.layout_4)
        self.pixelLockPushButton.setObjectName(u"pixelLockPushButton")
        self.pixelLockPushButton.setMinimumSize(QSize(20, 20))
        self.pixelLockPushButton.setMaximumSize(QSize(20, 20))
        icon6 = QIcon()
        icon6.addFile(u":/images/images/window_pixel_lock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pixelLockPushButton.setIcon(icon6)
        self.pixelLockPushButton.setIconSize(QSize(14, 14))

        self.horizontalLayout_3.addWidget(self.pixelLockPushButton)

        self.moveLockPushButton = QPushButton(self.layout_4)
        self.moveLockPushButton.setObjectName(u"moveLockPushButton")
        self.moveLockPushButton.setMinimumSize(QSize(20, 20))
        self.moveLockPushButton.setMaximumSize(QSize(20, 20))
        icon7 = QIcon()
        icon7.addFile(u":/images/images/window_lock_position.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moveLockPushButton.setIcon(icon7)
        self.moveLockPushButton.setIconSize(QSize(14, 14))

        self.horizontalLayout_3.addWidget(self.moveLockPushButton)

        self.autoNestLockPushButton = QPushButton(self.layout_4)
        self.autoNestLockPushButton.setObjectName(u"autoNestLockPushButton")
        self.autoNestLockPushButton.setMinimumSize(QSize(20, 20))
        self.autoNestLockPushButton.setMaximumSize(QSize(20, 20))
        icon8 = QIcon()
        icon8.addFile(u":/images/images/window_prevent_auto_nesting.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.autoNestLockPushButton.setIcon(icon8)
        self.autoNestLockPushButton.setIconSize(QSize(14, 14))

        self.horizontalLayout_3.addWidget(self.autoNestLockPushButton)

        self.layerLockPushButton = QPushButton(self.layout_4)
        self.layerLockPushButton.setObjectName(u"layerLockPushButton")
        self.layerLockPushButton.setMinimumSize(QSize(20, 20))
        self.layerLockPushButton.setMaximumSize(QSize(20, 20))
        icon9 = QIcon()
        icon9.addFile(u":/images/images/window_lock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.layerLockPushButton.setIcon(icon9)
        self.layerLockPushButton.setIconSize(QSize(14, 14))

        self.horizontalLayout_3.addWidget(self.layerLockPushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.layout_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(17, 0))
        self.label_2.setMaximumSize(QSize(20, 16777215))
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.fillComboBox = QComboBox(self.layout_4)
        self.fillComboBox.setObjectName(u"fillComboBox")
        self.fillComboBox.setMinimumSize(QSize(50, 0))
        self.fillComboBox.setMaximumSize(QSize(50, 18))
        self.fillComboBox.setEditable(True)

        self.horizontalLayout_3.addWidget(self.fillComboBox)


        self.verticalLayout.addWidget(self.layout_4)

        self.layerScrollArea = QScrollArea(LayersWindow)
        self.layerScrollArea.setObjectName(u"layerScrollArea")
        self.layerScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 307, 145))
        self.layerScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.layerScrollArea)

        self.layout_3 = QWidget(LayersWindow)
        self.layout_3.setObjectName(u"layout_3")
        self.layout_3.setMinimumSize(QSize(0, 26))
        self.layout_3.setMaximumSize(QSize(16777215, 26))
        self.horizontalLayout = QHBoxLayout(self.layout_3)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 2, 10, 2)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.linkPushButton = QPushButton(self.layout_3)
        self.linkPushButton.setObjectName(u"linkPushButton")
        self.linkPushButton.setEnabled(False)
        self.linkPushButton.setMinimumSize(QSize(24, 24))
        self.linkPushButton.setMaximumSize(QSize(20, 20))
        icon10 = QIcon()
        icon10.addFile(u":/images/images/window_link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.linkPushButton.setIcon(icon10)
        self.linkPushButton.setIconSize(QSize(14, 14))
        self.linkPushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.linkPushButton)

        self.addLayerStylePushButton = QPushButton(self.layout_3)
        self.addLayerStylePushButton.setObjectName(u"addLayerStylePushButton")
        self.addLayerStylePushButton.setMinimumSize(QSize(24, 24))
        self.addLayerStylePushButton.setMaximumSize(QSize(20, 20))
        icon11 = QIcon()
        icon11.addFile(u":/images/images/window_layer_style.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addLayerStylePushButton.setIcon(icon11)
        self.addLayerStylePushButton.setIconSize(QSize(14, 14))
        self.addLayerStylePushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.addLayerStylePushButton)

        self.newLayerMaskPushButton = QPushButton(self.layout_3)
        self.newLayerMaskPushButton.setObjectName(u"newLayerMaskPushButton")
        self.newLayerMaskPushButton.setMinimumSize(QSize(24, 24))
        self.newLayerMaskPushButton.setMaximumSize(QSize(20, 20))
        icon12 = QIcon()
        icon12.addFile(u":/images/images/window_add_mask.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newLayerMaskPushButton.setIcon(icon12)
        self.newLayerMaskPushButton.setIconSize(QSize(14, 14))
        self.newLayerMaskPushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.newLayerMaskPushButton)

        self.newFillOrAdjustmentLayerPushButton = QPushButton(self.layout_3)
        self.newFillOrAdjustmentLayerPushButton.setObjectName(u"newFillOrAdjustmentLayerPushButton")
        self.newFillOrAdjustmentLayerPushButton.setMinimumSize(QSize(24, 24))
        self.newFillOrAdjustmentLayerPushButton.setMaximumSize(QSize(20, 20))
        icon13 = QIcon()
        icon13.addFile(u":/images/images/window_create_adjustment_layer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newFillOrAdjustmentLayerPushButton.setIcon(icon13)
        self.newFillOrAdjustmentLayerPushButton.setIconSize(QSize(14, 14))
        self.newFillOrAdjustmentLayerPushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.newFillOrAdjustmentLayerPushButton)

        self.newGroupPushButton = QPushButton(self.layout_3)
        self.newGroupPushButton.setObjectName(u"newGroupPushButton")
        self.newGroupPushButton.setMinimumSize(QSize(24, 24))
        self.newGroupPushButton.setMaximumSize(QSize(20, 20))
        icon14 = QIcon()
        icon14.addFile(u":/images/images/window_add_group.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newGroupPushButton.setIcon(icon14)
        self.newGroupPushButton.setIconSize(QSize(14, 14))
        self.newGroupPushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.newGroupPushButton)

        self.newLayerPushButton = QPushButton(self.layout_3)
        self.newLayerPushButton.setObjectName(u"newLayerPushButton")
        self.newLayerPushButton.setMinimumSize(QSize(24, 24))
        self.newLayerPushButton.setMaximumSize(QSize(20, 20))
        icon15 = QIcon()
        icon15.addFile(u":/images/images/window_add_layer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newLayerPushButton.setIcon(icon15)
        self.newLayerPushButton.setIconSize(QSize(14, 14))
        self.newLayerPushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.newLayerPushButton)

        self.deleteLayerPushButton = QPushButton(self.layout_3)
        self.deleteLayerPushButton.setObjectName(u"deleteLayerPushButton")
        self.deleteLayerPushButton.setMinimumSize(QSize(24, 24))
        self.deleteLayerPushButton.setMaximumSize(QSize(20, 20))
        icon16 = QIcon()
        icon16.addFile(u":/images/images/window_delete_layer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteLayerPushButton.setIcon(icon16)
        self.deleteLayerPushButton.setIconSize(QSize(14, 14))
        self.deleteLayerPushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.deleteLayerPushButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addWidget(self.layout_3)


        self.retranslateUi(LayersWindow)

        QMetaObject.connectSlotsByName(LayersWindow)
    # setupUi

    def retranslateUi(self, LayersWindow):
        LayersWindow.setWindowTitle(QCoreApplication.translate("LayersWindow", u"Form", None))
        self.pixelFilterLayersPushButton.setText("")
        self.filterForAdjustmentLayersPushButton.setText("")
        self.filterForTypeLayersPushButton.setText("")
        self.filterForShapesLayersPushButton.setText("")
        self.filterForSmartObjectsPushButton.setText("")
        self.label_3.setText(QCoreApplication.translate("LayersWindow", u"Opacity:", None))
        self.label.setText(QCoreApplication.translate("LayersWindow", u"Lock:", None))
        self.alphaLockPushButton.setText("")
        self.pixelLockPushButton.setText("")
        self.moveLockPushButton.setText("")
        self.autoNestLockPushButton.setText("")
        self.layerLockPushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("LayersWindow", u"Fill:", None))
        self.linkPushButton.setText("")
        self.addLayerStylePushButton.setText("")
        self.newLayerMaskPushButton.setText("")
        self.newFillOrAdjustmentLayerPushButton.setText("")
        self.newGroupPushButton.setText("")
        self.newLayerPushButton.setText("")
        self.deleteLayerPushButton.setText("")
    # retranslateUi

