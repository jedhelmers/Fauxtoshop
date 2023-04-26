# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_options.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import resources_rc

class Ui_TextOptions(object):
    def setupUi(self, TextOptions):
        if not TextOptions.objectName():
            TextOptions.setObjectName(u"TextOptions")
        TextOptions.resize(873, 44)
        TextOptions.setMinimumSize(QSize(0, 38))
        TextOptions.setMaximumSize(QSize(16777215, 44))
        self.gridLayout = QGridLayout(TextOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.toolOptionsWidget = QWidget(TextOptions)
        self.toolOptionsWidget.setObjectName(u"toolOptionsWidget")
        self.gridLayout_2 = QGridLayout(self.toolOptionsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolPresetPickerPushButton = QPushButton(self.toolOptionsWidget)
        self.toolPresetPickerPushButton.setObjectName(u"toolPresetPickerPushButton")
        self.toolPresetPickerPushButton.setMinimumSize(QSize(32, 32))
        self.toolPresetPickerPushButton.setMaximumSize(QSize(32, 32))
        icon = QIcon()
        icon.addFile(u":/images/images/toolbar_t.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolPresetPickerPushButton.setIcon(icon)
        self.toolPresetPickerPushButton.setFlat(False)

        self.gridLayout_2.addWidget(self.toolPresetPickerPushButton, 0, 0, 1, 1)

        self.line = QFrame(self.toolOptionsWidget)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(1, 20))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 0, 1, 1, 1)

        self.textOrientationPushButton = QPushButton(self.toolOptionsWidget)
        self.textOrientationPushButton.setObjectName(u"textOrientationPushButton")
        self.textOrientationPushButton.setMinimumSize(QSize(32, 32))
        self.textOrientationPushButton.setMaximumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/tool_options_toggle_text_orientation.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.textOrientationPushButton.setIcon(icon1)
        self.textOrientationPushButton.setFlat(False)

        self.gridLayout_2.addWidget(self.textOrientationPushButton, 0, 2, 1, 1)

        self.line_2 = QFrame(self.toolOptionsWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(1, 20))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 0, 3, 1, 1)

        self.fontComboBox = QComboBox(self.toolOptionsWidget)
        self.fontComboBox.setObjectName(u"fontComboBox")
        font = QFont()
        font.setPointSize(11)
        self.fontComboBox.setFont(font)
        self.fontComboBox.setEditable(True)

        self.gridLayout_2.addWidget(self.fontComboBox, 0, 4, 1, 1)

        self.fontStyleComboBox = QComboBox(self.toolOptionsWidget)
        self.fontStyleComboBox.setObjectName(u"fontStyleComboBox")
        self.fontStyleComboBox.setFont(font)
        self.fontStyleComboBox.setEditable(True)

        self.gridLayout_2.addWidget(self.fontStyleComboBox, 0, 5, 1, 1)

        self.line_3 = QFrame(self.toolOptionsWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(1, 20))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 0, 6, 1, 1)

        self.fontSizeIcon = QPushButton(self.toolOptionsWidget)
        self.fontSizeIcon.setObjectName(u"fontSizeIcon")
        self.fontSizeIcon.setEnabled(False)
        self.fontSizeIcon.setMinimumSize(QSize(32, 32))
        self.fontSizeIcon.setMaximumSize(QSize(32, 32))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/tool_options_set_font_size.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fontSizeIcon.setIcon(icon2)
        self.fontSizeIcon.setFlat(False)

        self.gridLayout_2.addWidget(self.fontSizeIcon, 0, 7, 1, 1)

        self.fontSizeComboBox = QComboBox(self.toolOptionsWidget)
        self.fontSizeComboBox.setObjectName(u"fontSizeComboBox")
        self.fontSizeComboBox.setFont(font)
        self.fontSizeComboBox.setEditable(True)

        self.gridLayout_2.addWidget(self.fontSizeComboBox, 0, 8, 1, 1)

        self.fontSharpenIcon = QPushButton(self.toolOptionsWidget)
        self.fontSharpenIcon.setObjectName(u"fontSharpenIcon")
        self.fontSharpenIcon.setEnabled(False)
        self.fontSharpenIcon.setMinimumSize(QSize(32, 32))
        self.fontSharpenIcon.setMaximumSize(QSize(32, 32))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/tool_options_font_sharpness.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fontSharpenIcon.setIcon(icon3)
        self.fontSharpenIcon.setFlat(False)

        self.gridLayout_2.addWidget(self.fontSharpenIcon, 0, 9, 1, 1)

        self.fontSharpnessComboBox = QComboBox(self.toolOptionsWidget)
        self.fontSharpnessComboBox.setObjectName(u"fontSharpnessComboBox")
        self.fontSharpnessComboBox.setFont(font)

        self.gridLayout_2.addWidget(self.fontSharpnessComboBox, 0, 10, 1, 1)

        self.line_4 = QFrame(self.toolOptionsWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMaximumSize(QSize(1, 20))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 0, 11, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textAlignLeftPushButton = QPushButton(self.toolOptionsWidget)
        self.textAlignLeftPushButton.setObjectName(u"textAlignLeftPushButton")
        self.textAlignLeftPushButton.setMinimumSize(QSize(32, 32))
        self.textAlignLeftPushButton.setMaximumSize(QSize(32, 32))
        icon4 = QIcon()
        icon4.addFile(u":/images/images/tool_options_left_align_text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.textAlignLeftPushButton.setIcon(icon4)
        self.textAlignLeftPushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.textAlignLeftPushButton)

        self.textAlignCenterPushButton = QPushButton(self.toolOptionsWidget)
        self.textAlignCenterPushButton.setObjectName(u"textAlignCenterPushButton")
        self.textAlignCenterPushButton.setMinimumSize(QSize(32, 32))
        self.textAlignCenterPushButton.setMaximumSize(QSize(32, 32))
        icon5 = QIcon()
        icon5.addFile(u":/images/images/tool_options_center_text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.textAlignCenterPushButton.setIcon(icon5)
        self.textAlignCenterPushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.textAlignCenterPushButton)

        self.textAlignRightPushButton = QPushButton(self.toolOptionsWidget)
        self.textAlignRightPushButton.setObjectName(u"textAlignRightPushButton")
        self.textAlignRightPushButton.setMinimumSize(QSize(32, 32))
        self.textAlignRightPushButton.setMaximumSize(QSize(32, 32))
        icon6 = QIcon()
        icon6.addFile(u":/images/images/tool_options_right_align_text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.textAlignRightPushButton.setIcon(icon6)
        self.textAlignRightPushButton.setFlat(False)

        self.horizontalLayout.addWidget(self.textAlignRightPushButton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 12, 1, 1)

        self.line_5 = QFrame(self.toolOptionsWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMaximumSize(QSize(1, 20))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 0, 13, 1, 1)

        self.widget_2 = QWidget(self.toolOptionsWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(20, 20))
        self.widget_2.setMaximumSize(QSize(20, 20))
        self.widget_2.setStyleSheet(u"background: white")

        self.gridLayout_2.addWidget(self.widget_2, 0, 14, 1, 1)

        self.line_6 = QFrame(self.toolOptionsWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMaximumSize(QSize(1, 20))
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_6, 0, 15, 1, 1)

        self.textWarpPushButton = QPushButton(self.toolOptionsWidget)
        self.textWarpPushButton.setObjectName(u"textWarpPushButton")
        self.textWarpPushButton.setMinimumSize(QSize(32, 32))
        self.textWarpPushButton.setMaximumSize(QSize(32, 32))
        icon7 = QIcon()
        icon7.addFile(u":/images/images/tool_options_create_warped_text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.textWarpPushButton.setIcon(icon7)
        self.textWarpPushButton.setFlat(False)

        self.gridLayout_2.addWidget(self.textWarpPushButton, 0, 16, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 17, 1, 1)


        self.gridLayout.addWidget(self.toolOptionsWidget, 0, 0, 1, 1)


        self.retranslateUi(TextOptions)

        QMetaObject.connectSlotsByName(TextOptions)
    # setupUi

    def retranslateUi(self, TextOptions):
        TextOptions.setWindowTitle(QCoreApplication.translate("TextOptions", u"Form", None))
        self.toolPresetPickerPushButton.setText("")
        self.textOrientationPushButton.setText("")
        self.fontSizeIcon.setText("")
        self.fontSharpenIcon.setText("")
        self.textAlignLeftPushButton.setText("")
        self.textAlignCenterPushButton.setText("")
        self.textAlignRightPushButton.setText("")
        self.textWarpPushButton.setText("")
    # retranslateUi

