# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'brush.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QWidget)
import resources_rc

class Ui_BrushOptions(object):
    def setupUi(self, BrushOptions):
        if not BrushOptions.objectName():
            BrushOptions.setObjectName(u"BrushOptions")
        BrushOptions.resize(873, 38)
        BrushOptions.setMinimumSize(QSize(0, 38))
        BrushOptions.setMaximumSize(QSize(16777215, 38))
        self.horizontalLayout = QHBoxLayout(BrushOptions)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_4 = QLabel(BrushOptions)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.modeComboBox = QComboBox(BrushOptions)
        self.modeComboBox.setObjectName(u"modeComboBox")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.modeComboBox)


        self.horizontalLayout.addLayout(self.formLayout_4)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_5 = QLabel(BrushOptions)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.opacityComboBox = QComboBox(BrushOptions)
        self.opacityComboBox.setObjectName(u"opacityComboBox")
        self.opacityComboBox.setMinimumSize(QSize(80, 0))
        self.opacityComboBox.setEditable(True)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.opacityComboBox)


        self.horizontalLayout.addLayout(self.formLayout_5)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_6 = QLabel(BrushOptions)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.flowComboBox = QComboBox(BrushOptions)
        self.flowComboBox.setObjectName(u"flowComboBox")
        self.flowComboBox.setEditable(True)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.flowComboBox)


        self.horizontalLayout.addLayout(self.formLayout_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(BrushOptions)

        QMetaObject.connectSlotsByName(BrushOptions)
    # setupUi

    def retranslateUi(self, BrushOptions):
        BrushOptions.setWindowTitle(QCoreApplication.translate("BrushOptions", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("BrushOptions", u"Mode", None))
        self.label_5.setText(QCoreApplication.translate("BrushOptions", u"Opacity", None))
        self.label_6.setText(QCoreApplication.translate("BrushOptions", u"Flow", None))
    # retranslateUi

