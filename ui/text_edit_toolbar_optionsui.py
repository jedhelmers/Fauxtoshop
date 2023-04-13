# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_edit_toolbar_options.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTabWidget, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(695, 300)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(40, 30, 571, 191))
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setMinimumSize(QSize(32, 32))
        self.tab.setMaximumSize(QSize(32, 32))
        icon = QIcon()
        icon.addFile(u":/images/images/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setMinimumSize(QSize(32, 32))
        self.tab_2.setMaximumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/paintbrush.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon1, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "")
    # retranslateUi

