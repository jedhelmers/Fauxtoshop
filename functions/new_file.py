from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, Qt, QRect, QPoint, QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QScrollArea

from widgets.artboard import ArtBoardWidget

def new_file(self, new_file_info):
    """NEW TAB"""
    tab = QWidget()
    tab.setObjectName(u"tab")
    gridLayout_4 = QGridLayout(tab)
    gridLayout_4.setSpacing(0)
    gridLayout_4.setObjectName(u"gridLayout_4")
    gridLayout_4.setContentsMargins(0, 0, 0, 0)

    gridLayout_3 = QGridLayout()
    gridLayout_3.setSpacing(0)
    gridLayout_3.setObjectName(u"gridLayout_3")
    verticalRulerWidget = QWidget(tab)
    verticalRulerWidget.setObjectName(u"verticalRulerWidget")
    verticalRulerWidget.setMinimumSize(QSize(20, 0))
    verticalRulerWidget.setMaximumSize(QSize(20, 16777215))

    gridLayout_3.addWidget(verticalRulerWidget, 0, 0, 1, 1)

    verticalLayout_3 = QVBoxLayout()
    verticalLayout_3.setSpacing(0)
    verticalLayout_3.setObjectName(u"verticalLayout_3")
    horizontalRulerWidget = QWidget(tab)
    horizontalRulerWidget.setObjectName(u"horizontalRulerWidget")
    horizontalRulerWidget.setMinimumSize(QSize(0, 20))
    horizontalRulerWidget.setMaximumSize(QSize(16777215, 20))

    verticalLayout_3.addWidget(horizontalRulerWidget)

    workScrollArea = QScrollArea(tab)
    workScrollArea.setObjectName(u"workScrollArea")
    workScrollArea.setWidgetResizable(True)
    scrollAreaWidgetContents = QWidget()
    scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
    scrollAreaWidgetContents.setGeometry(QRect(0, 0, 670, 420))
    openGLWidget = ArtBoardWidget(scrollAreaWidgetContents, new_file_info)

    workScrollArea.setWidget(scrollAreaWidgetContents)

    verticalLayout_3.addWidget(workScrollArea)

    gridLayout_3.addLayout(verticalLayout_3, 0, 1, 1, 1)

    gridLayout_4.addLayout(gridLayout_3, 0, 0, 1, 1)

    self.ui.workspaceTabWidget.addTab(tab, "")
    self.ui.workspaceTabWidget.setTabText(self.ui.workspaceTabWidget.indexOf(tab), QCoreApplication.translate("MainWindow", new_file_info['name'], None))
    print('BUTTS')
    """END NEW TAB"""