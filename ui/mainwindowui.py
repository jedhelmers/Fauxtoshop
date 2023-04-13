# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.toolOptionsWidget = QWidget(self.widget)
        self.toolOptionsWidget.setObjectName(u"toolOptionsWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.toolOptionsWidget)
#ifndef Q_OS_MAC
        self.horizontalLayout_2.setSpacing(-1)
#endif
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.paintBrushButton_3 = QPushButton(self.toolOptionsWidget)
        self.paintBrushButton_3.setObjectName(u"paintBrushButton_3")
        self.paintBrushButton_3.setMinimumSize(QSize(32, 32))
        self.paintBrushButton_3.setMaximumSize(QSize(32, 32))
        icon = QIcon()
        icon.addFile(u":/images/images/paintbrush.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.paintBrushButton_3.setIcon(icon)
        self.paintBrushButton_3.setFlat(False)

        self.horizontalLayout_2.addWidget(self.paintBrushButton_3)

        self.paintBrushButton_2 = QPushButton(self.toolOptionsWidget)
        self.paintBrushButton_2.setObjectName(u"paintBrushButton_2")
        self.paintBrushButton_2.setMinimumSize(QSize(32, 32))
        self.paintBrushButton_2.setMaximumSize(QSize(32, 32))
        self.paintBrushButton_2.setIcon(icon)
        self.paintBrushButton_2.setFlat(False)

        self.horizontalLayout_2.addWidget(self.paintBrushButton_2)

        self.comboBox = QComboBox(self.toolOptionsWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.toolOptionsWidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboBox_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.toolOptionsWidget, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolbarWidget = QWidget(self.centralwidget)
        self.toolbarWidget.setObjectName(u"toolbarWidget")
        self.toolbarWidget.setMinimumSize(QSize(40, 0))
        self.toolbarWidget.setMaximumSize(QSize(40, 16777215))
        self.verticalLayout = QVBoxLayout(self.toolbarWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 2)
        self.paintBrushButton = QPushButton(self.toolbarWidget)
        self.paintBrushButton.setObjectName(u"paintBrushButton")
        self.paintBrushButton.setMinimumSize(QSize(32, 32))
        self.paintBrushButton.setMaximumSize(QSize(32, 32))
        self.paintBrushButton.setIcon(icon)
        self.paintBrushButton.setFlat(False)

        self.verticalLayout.addWidget(self.paintBrushButton)

        self.paletteButton = QPushButton(self.toolbarWidget)
        self.paletteButton.setObjectName(u"paletteButton")
        self.paletteButton.setMinimumSize(QSize(32, 32))
        self.paletteButton.setMaximumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/palette.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.paletteButton.setIcon(icon1)
        self.paletteButton.setFlat(False)

        self.verticalLayout.addWidget(self.paletteButton)

        self.verticalSpacer = QSpacerItem(20, 425, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.toolbarWidget)

        self.workspaceTabWidget = QTabWidget(self.centralwidget)
        self.workspaceTabWidget.setObjectName(u"workspaceTabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.workspaceTabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.workspaceTabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.workspaceTabWidget)

        self.collapsedPanelWidget = QWidget(self.centralwidget)
        self.collapsedPanelWidget.setObjectName(u"collapsedPanelWidget")
        self.collapsedPanelWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.collapsedPanelWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.paletteButton_2 = QPushButton(self.collapsedPanelWidget)
        self.paletteButton_2.setObjectName(u"paletteButton_2")
        self.paletteButton_2.setMinimumSize(QSize(32, 32))
        self.paletteButton_2.setMaximumSize(QSize(32, 32))
        self.paletteButton_2.setIcon(icon1)
        self.paletteButton_2.setFlat(False)

        self.verticalLayout_2.addWidget(self.paletteButton_2)

        self.verticalSpacer_2 = QSpacerItem(20, 439, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.collapsedPanelWidget)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.paintBrushButton_3.setText("")
        self.paintBrushButton_2.setText("")
        self.paintBrushButton.setText("")
        self.paletteButton.setText("")
        self.workspaceTabWidget.setTabText(self.workspaceTabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.workspaceTabWidget.setTabText(self.workspaceTabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.paletteButton_2.setText("")
    # retranslateUi

