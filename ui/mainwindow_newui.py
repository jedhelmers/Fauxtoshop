# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_new.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(876, 611)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionMode = QAction(MainWindow)
        self.actionMode.setObjectName(u"actionMode")
        self.actionPlaceholder = QAction(MainWindow)
        self.actionPlaceholder.setObjectName(u"actionPlaceholder")
        self.actionPlaceholder_2 = QAction(MainWindow)
        self.actionPlaceholder_2.setObjectName(u"actionPlaceholder_2")
        self.actionPlaceholder_3 = QAction(MainWindow)
        self.actionPlaceholder_3.setObjectName(u"actionPlaceholder_3")
        self.actionPlaceholder_4 = QAction(MainWindow)
        self.actionPlaceholder_4.setObjectName(u"actionPlaceholder_4")
        self.actionPlaceholder_5 = QAction(MainWindow)
        self.actionPlaceholder_5.setObjectName(u"actionPlaceholder_5")
        self.actionPlaceholder_6 = QAction(MainWindow)
        self.actionPlaceholder_6.setObjectName(u"actionPlaceholder_6")
        self.actionPlaceholder_7 = QAction(MainWindow)
        self.actionPlaceholder_7.setObjectName(u"actionPlaceholder_7")
        self.actionPlaceholder_8 = QAction(MainWindow)
        self.actionPlaceholder_8.setObjectName(u"actionPlaceholder_8")
        self.actionPlaceholder_9 = QAction(MainWindow)
        self.actionPlaceholder_9.setObjectName(u"actionPlaceholder_9")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolOptionsGridWidget = QWidget(self.centralwidget)
        self.toolOptionsGridWidget.setObjectName(u"toolOptionsGridWidget")
        self.toolOptionsGridWidget.setMaximumSize(QSize(16777215, 50))
        self.gridLayout = QGridLayout(self.toolOptionsGridWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.toolOptionsWidget = QWidget(self.toolOptionsGridWidget)
        self.toolOptionsWidget.setObjectName(u"toolOptionsWidget")
        self.toolOptionsWidget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.toolOptionsWidget)
#ifndef Q_OS_MAC
        self.horizontalLayout_2.setSpacing(-1)
#endif
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.toolOptionsWidget, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.toolOptionsGridWidget, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolbarWidget = QWidget(self.centralwidget)
        self.toolbarWidget.setObjectName(u"toolbarWidget")
        self.toolbarWidget.setMinimumSize(QSize(0, 0))
        self.toolbarWidget.setMaximumSize(QSize(40, 16777215))
        self.verticalLayout = QVBoxLayout(self.toolbarWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 0, 0, 2)

        self.horizontalLayout.addWidget(self.toolbarWidget)

        self.workspaceTabWidget = QTabWidget(self.centralwidget)
        self.workspaceTabWidget.setObjectName(u"workspaceTabWidget")
        self.workspaceTabWidget.setTabsClosable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widget_2 = QWidget(self.tab)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(20, 0))
        self.widget_2.setMaximumSize(QSize(20, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLeftRulerCornerWidget = QWidget(self.widget_2)
        self.topLeftRulerCornerWidget.setObjectName(u"topLeftRulerCornerWidget")
        self.topLeftRulerCornerWidget.setMinimumSize(QSize(20, 20))
        self.topLeftRulerCornerWidget.setMaximumSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.topLeftRulerCornerWidget)

        self.verticalRulerWidget = QWidget(self.widget_2)
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


        self.verticalLayout_3.addWidget(self.verticalRulerWidget)


        self.horizontalLayout_7.addWidget(self.widget_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalRulerWidget = QWidget(self.tab)
        self.horizontalRulerWidget.setObjectName(u"horizontalRulerWidget")
        self.horizontalRulerWidget.setMinimumSize(QSize(0, 20))
        self.horizontalRulerWidget.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalRulerWidget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)


        self.verticalLayout_6.addWidget(self.horizontalRulerWidget)

        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.widget)


        self.horizontalLayout_7.addLayout(self.verticalLayout_6)


        self.gridLayout_5.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.workspaceTabWidget.addTab(self.tab, "")

        self.horizontalLayout.addWidget(self.workspaceTabWidget)

        self.windowsWidget = QWidget(self.centralwidget)
        self.windowsWidget.setObjectName(u"windowsWidget")
        self.windowsWidget.setMinimumSize(QSize(227, 0))
        self.verticalLayout_2 = QVBoxLayout(self.windowsWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.windowsWidget)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 876, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuImage = QMenu(self.menubar)
        self.menuImage.setObjectName(u"menuImage")
        self.menuLayer = QMenu(self.menubar)
        self.menuLayer.setObjectName(u"menuLayer")
        self.menuType = QMenu(self.menubar)
        self.menuType.setObjectName(u"menuType")
        self.menuSelect = QMenu(self.menubar)
        self.menuSelect.setObjectName(u"menuSelect")
        self.menuFilter = QMenu(self.menubar)
        self.menuFilter.setObjectName(u"menuFilter")
        self.menu3D = QMenu(self.menubar)
        self.menu3D.setObjectName(u"menu3D")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuPlugins = QMenu(self.menubar)
        self.menuPlugins.setObjectName(u"menuPlugins")
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuImage.menuAction())
        self.menubar.addAction(self.menuLayer.menuAction())
        self.menubar.addAction(self.menuType.menuAction())
        self.menubar.addAction(self.menuSelect.menuAction())
        self.menubar.addAction(self.menuFilter.menuAction())
        self.menubar.addAction(self.menu3D.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuPlugins.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuImage.addAction(self.actionMode)
        self.menuLayer.addAction(self.actionPlaceholder)
        self.menuType.addAction(self.actionPlaceholder_2)
        self.menuSelect.addAction(self.actionPlaceholder_3)
        self.menuFilter.addAction(self.actionPlaceholder_4)
        self.menu3D.addAction(self.actionPlaceholder_5)
        self.menuView.addAction(self.actionPlaceholder_6)
        self.menuPlugins.addAction(self.actionPlaceholder_7)
        self.menuWindow.addAction(self.actionPlaceholder_8)
        self.menuHelp.addAction(self.actionPlaceholder_9)

        self.retranslateUi(MainWindow)

        self.workspaceTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fauxtoshop 2023", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New...", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionMode.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.actionPlaceholder.setText(QCoreApplication.translate("MainWindow", u"Placeholder", None))
        self.actionPlaceholder_2.setText(QCoreApplication.translate("MainWindow", u"Placeholder", None))
        self.actionPlaceholder_3.setText(QCoreApplication.translate("MainWindow", u"Placeholder", None))
        self.actionPlaceholder_4.setText(QCoreApplication.translate("MainWindow", u"Placeholder", None))
        self.actionPlaceholder_5.setText(QCoreApplication.translate("MainWindow", u"Placeholder", None))
        self.actionPlaceholder_6.setText(QCoreApplication.translate("MainWindow", u"Placeholder", None))
        self.actionPlaceholder_7.setText(QCoreApplication.translate("MainWindow", u"Placeholder", None))
        self.actionPlaceholder_8.setText(QCoreApplication.translate("MainWindow", u"Placeholder", None))
        self.actionPlaceholder_9.setText(QCoreApplication.translate("MainWindow", u"Placeholder", None))
        self.workspaceTabWidget.setTabText(self.workspaceTabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Page", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuImage.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.menuLayer.setTitle(QCoreApplication.translate("MainWindow", u"Layer", None))
        self.menuType.setTitle(QCoreApplication.translate("MainWindow", u"Type", None))
        self.menuSelect.setTitle(QCoreApplication.translate("MainWindow", u"Select", None))
        self.menuFilter.setTitle(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.menu3D.setTitle(QCoreApplication.translate("MainWindow", u"3D", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuPlugins.setTitle(QCoreApplication.translate("MainWindow", u"Plugins", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

