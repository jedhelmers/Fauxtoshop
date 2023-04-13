import json
import sys
from pathlib import Path
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from styles.main import main_style
from ui import mainwindowui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainwindowui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(main_style())

def main():
    app = QApplication(sys.argv)
    settings_window = MainWindow()
    settings_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()