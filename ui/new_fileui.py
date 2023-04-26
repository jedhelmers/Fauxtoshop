# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_file.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_NewFile(object):
    def setupUi(self, NewFile):
        if not NewFile.objectName():
            NewFile.setObjectName(u"NewFile")
        NewFile.resize(550, 350)
        NewFile.setMinimumSize(QSize(550, 350))
        NewFile.setMaximumSize(QSize(550, 350))
        self.frame = QFrame(NewFile)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 44, 390, 287))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 210, 371, 71))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout_2.setSpacing(-1)
#endif
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout_2 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayout_2.setSpacing(-1)
#endif
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.colorProfileComboBox = QComboBox(self.frame_2)
        self.colorProfileComboBox.setObjectName(u"colorProfileComboBox")
        self.colorProfileComboBox.setMinimumSize(QSize(220, 20))
        self.colorProfileComboBox.setMaximumSize(QSize(16777215, 20))
        self.colorProfileComboBox.setFont(font)

        self.horizontalLayout_2.addWidget(self.colorProfileComboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayout.setSpacing(-1)
#endif
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_9)

        self.pixelAspectRatioComboBox = QComboBox(self.frame_2)
        self.pixelAspectRatioComboBox.setObjectName(u"pixelAspectRatioComboBox")
        self.pixelAspectRatioComboBox.setMinimumSize(QSize(220, 20))
        self.pixelAspectRatioComboBox.setMaximumSize(QSize(16777215, 20))
        self.pixelAspectRatioComboBox.setFont(font)

        self.horizontalLayout.addWidget(self.pixelAspectRatioComboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 202, 100, 16))
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(7, 20, 381, 171))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 0))
        self.label_7.setMaximumSize(QSize(120, 16777215))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.sizeLineEdit = QLineEdit(self.layoutWidget)
        self.sizeLineEdit.setObjectName(u"sizeLineEdit")
        self.sizeLineEdit.setMinimumSize(QSize(155, 20))
        self.sizeLineEdit.setMaximumSize(QSize(230, 20))
        self.sizeLineEdit.setFont(font)

        self.horizontalLayout_5.addWidget(self.sizeLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(132, 0))
        self.label_4.setMaximumSize(QSize(132, 16777215))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.widthLineEdit = QLineEdit(self.layoutWidget)
        self.widthLineEdit.setObjectName(u"widthLineEdit")
        self.widthLineEdit.setMinimumSize(QSize(105, 20))
        self.widthLineEdit.setMaximumSize(QSize(105, 20))
        self.widthLineEdit.setFont(font)

        self.horizontalLayout_6.addWidget(self.widthLineEdit)

        self.unitsWComboBox = QComboBox(self.layoutWidget)
        self.unitsWComboBox.setObjectName(u"unitsWComboBox")
        self.unitsWComboBox.setMinimumSize(QSize(105, 20))
        self.unitsWComboBox.setMaximumSize(QSize(105, 20))
        self.unitsWComboBox.setFont(font)

        self.horizontalLayout_6.addWidget(self.unitsWComboBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(132, 0))
        self.label_5.setMaximumSize(QSize(132, 16777215))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.heightLineEdit = QLineEdit(self.layoutWidget)
        self.heightLineEdit.setObjectName(u"heightLineEdit")
        self.heightLineEdit.setMinimumSize(QSize(105, 20))
        self.heightLineEdit.setMaximumSize(QSize(105, 20))
        self.heightLineEdit.setFont(font)

        self.horizontalLayout_7.addWidget(self.heightLineEdit)

        self.unitsHComboBox = QComboBox(self.layoutWidget)
        self.unitsHComboBox.setObjectName(u"unitsHComboBox")
        self.unitsHComboBox.setMinimumSize(QSize(105, 20))
        self.unitsHComboBox.setMaximumSize(QSize(105, 20))
        self.unitsHComboBox.setFont(font)

        self.horizontalLayout_7.addWidget(self.unitsHComboBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(132, 0))
        self.label_6.setMaximumSize(QSize(132, 16777215))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.resolutionLineEdit = QLineEdit(self.layoutWidget)
        self.resolutionLineEdit.setObjectName(u"resolutionLineEdit")
        self.resolutionLineEdit.setMinimumSize(QSize(105, 20))
        self.resolutionLineEdit.setMaximumSize(QSize(105, 20))
        self.resolutionLineEdit.setFont(font)

        self.horizontalLayout_8.addWidget(self.resolutionLineEdit)

        self.unitsResolutionComboBox = QComboBox(self.layoutWidget)
        self.unitsResolutionComboBox.setObjectName(u"unitsResolutionComboBox")
        self.unitsResolutionComboBox.setMinimumSize(QSize(105, 20))
        self.unitsResolutionComboBox.setMaximumSize(QSize(105, 20))
        self.unitsResolutionComboBox.setFont(font)

        self.horizontalLayout_8.addWidget(self.unitsResolutionComboBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(132, 0))
        self.label_8.setMaximumSize(QSize(132, 16777215))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.colorModeLineEdit = QLineEdit(self.layoutWidget)
        self.colorModeLineEdit.setObjectName(u"colorModeLineEdit")
        self.colorModeLineEdit.setMinimumSize(QSize(105, 20))
        self.colorModeLineEdit.setMaximumSize(QSize(105, 20))
        self.colorModeLineEdit.setFont(font)

        self.horizontalLayout_9.addWidget(self.colorModeLineEdit)

        self.colorModeResComboBox = QComboBox(self.layoutWidget)
        self.colorModeResComboBox.setObjectName(u"colorModeResComboBox")
        self.colorModeResComboBox.setMinimumSize(QSize(105, 20))
        self.colorModeResComboBox.setMaximumSize(QSize(105, 20))
        self.colorModeResComboBox.setFont(font)

        self.horizontalLayout_9.addWidget(self.colorModeResComboBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(120, 0))
        self.label_10.setMaximumSize(QSize(120, 16777215))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.backgroundContentsLineEdit = QLineEdit(self.layoutWidget)
        self.backgroundContentsLineEdit.setObjectName(u"backgroundContentsLineEdit")
        self.backgroundContentsLineEdit.setMinimumSize(QSize(0, 20))
        self.backgroundContentsLineEdit.setMaximumSize(QSize(180, 20))
        self.backgroundContentsLineEdit.setFont(font)

        self.horizontalLayout_10.addWidget(self.backgroundContentsLineEdit)

        self.colorPickerPushButton = QPushButton(self.layoutWidget)
        self.colorPickerPushButton.setObjectName(u"colorPickerPushButton")
        self.colorPickerPushButton.setMinimumSize(QSize(15, 15))
        self.colorPickerPushButton.setMaximumSize(QSize(15, 15))
        self.colorPickerPushButton.setStyleSheet(u"background: white; border: none")
        self.colorPickerPushButton.setFlat(False)

        self.horizontalLayout_10.addWidget(self.colorPickerPushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.layoutWidget_2 = QWidget(NewFile)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(80, 10, 311, 22))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.nameLineEdit = QLineEdit(self.layoutWidget_2)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setMinimumSize(QSize(0, 20))
        self.nameLineEdit.setMaximumSize(QSize(16777215, 20))
        self.nameLineEdit.setFont(font)

        self.horizontalLayout_4.addWidget(self.nameLineEdit)

        self.layoutWidget_3 = QWidget(NewFile)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(410, 10, 123, 321))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.okPushButton = QPushButton(self.layoutWidget_3)
        self.okPushButton.setObjectName(u"okPushButton")
        self.okPushButton.setMinimumSize(QSize(0, 25))
        self.okPushButton.setMaximumSize(QSize(16777215, 25))
        self.okPushButton.setFont(font)

        self.verticalLayout.addWidget(self.okPushButton)

        self.cancelPushButton = QPushButton(self.layoutWidget_3)
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setMinimumSize(QSize(0, 25))
        self.cancelPushButton.setMaximumSize(QSize(16777215, 25))
        self.cancelPushButton.setFont(font)

        self.verticalLayout.addWidget(self.cancelPushButton)

        self.savePresetPushButton = QPushButton(self.layoutWidget_3)
        self.savePresetPushButton.setObjectName(u"savePresetPushButton")
        self.savePresetPushButton.setMinimumSize(QSize(0, 25))
        self.savePresetPushButton.setMaximumSize(QSize(16777215, 25))
        self.savePresetPushButton.setFont(font)

        self.verticalLayout.addWidget(self.savePresetPushButton)

        self.deletePresetPushButton = QPushButton(self.layoutWidget_3)
        self.deletePresetPushButton.setObjectName(u"deletePresetPushButton")
        self.deletePresetPushButton.setMinimumSize(QSize(0, 25))
        self.deletePresetPushButton.setMaximumSize(QSize(16777215, 25))
        self.deletePresetPushButton.setFont(font)

        self.verticalLayout.addWidget(self.deletePresetPushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_12 = QLabel(self.layoutWidget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_12)

        self.label_13 = QLabel(self.layoutWidget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_13)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.widget = QWidget(NewFile)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 36, 371, 21))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(12345678, 16777215))
        font1 = QFont()
        font1.setPointSize(13)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.documentTypeComboBox = QComboBox(self.widget)
        self.documentTypeComboBox.setObjectName(u"documentTypeComboBox")
        self.documentTypeComboBox.setMinimumSize(QSize(258, 20))
        self.documentTypeComboBox.setMaximumSize(QSize(16777215, 20))
        self.documentTypeComboBox.setFont(font)

        self.horizontalLayout_3.addWidget(self.documentTypeComboBox)


        self.retranslateUi(NewFile)

        QMetaObject.connectSlotsByName(NewFile)
    # setupUi

    def retranslateUi(self, NewFile):
        NewFile.setWindowTitle(QCoreApplication.translate("NewFile", u"New File", None))
        self.label_3.setText(QCoreApplication.translate("NewFile", u"Color Profile:", None))
        self.label_9.setText(QCoreApplication.translate("NewFile", u"Pixel Aspect Ratio:", None))
        self.label_11.setText(QCoreApplication.translate("NewFile", u"Advanced", None))
        self.label_7.setText(QCoreApplication.translate("NewFile", u"Size:", None))
        self.label_4.setText(QCoreApplication.translate("NewFile", u"Width:", None))
        self.label_5.setText(QCoreApplication.translate("NewFile", u"Height:", None))
        self.label_6.setText(QCoreApplication.translate("NewFile", u"Resolution:", None))
        self.label_8.setText(QCoreApplication.translate("NewFile", u"Color Mode:", None))
        self.label_10.setText(QCoreApplication.translate("NewFile", u"Background Contents:", None))
        self.colorPickerPushButton.setText("")
        self.label.setText(QCoreApplication.translate("NewFile", u"Name:", None))
        self.okPushButton.setText(QCoreApplication.translate("NewFile", u"OK", None))
        self.cancelPushButton.setText(QCoreApplication.translate("NewFile", u"Cancel", None))
        self.savePresetPushButton.setText(QCoreApplication.translate("NewFile", u"Save Preset...", None))
        self.deletePresetPushButton.setText(QCoreApplication.translate("NewFile", u"Delete Preset...", None))
        self.label_12.setText(QCoreApplication.translate("NewFile", u"Image Size:", None))
        self.label_13.setText(QCoreApplication.translate("NewFile", u"1.05M", None))
        self.label_2.setText(QCoreApplication.translate("NewFile", u"Document Type:", None))
    # retranslateUi

