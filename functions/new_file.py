from PySide6 import QtCore, QtGui
from PySide6.QtCore import QSize, Qt, QRect, QPoint, QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QScrollArea, QFrame

from widgets.artboard import ArtBoardWidget
from widgets.workspace import WorkspaceWidget


def new_file(self, new_file_info):
    tab = WorkspaceWidget(self, new_file_info)

    self.ui.workspaceTabWidget.addTab(tab, "")
    self.ui.workspaceTabWidget.setTabText(
        self.ui.workspaceTabWidget.indexOf(tab),
        QCoreApplication.translate(
            "MainWindow",
            new_file_info['name'], None))
