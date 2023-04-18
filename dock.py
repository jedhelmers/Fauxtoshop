import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class DockDemo(QMainWindow):
    def __init__(self,parent=None):
        super(DockDemo, self).__init__(parent)
        layout=QHBoxLayout()
        bar=self.menuBar()
        file=bar.addMenu('File')
        file.addAction('New')
        file.addAction('Save')
        file.addAction('quit')

        self.items=QDockWidget('Dockable',self)
        # self.items.setMaximumWidth(40)
        self.items.setFeatures(QDockWidget.DockWidgetMovable)

        self.listWidget=QListWidget()
        self.listWidget.addItem('Item1')
        self.listWidget.addItem('Item2')
        self.listWidget.addItem('Item3')
        self.listWidget.addItem('Item4')

        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)

        self.items2=QDockWidget('Dockable',self)
        # self.items2.setMaximumWidth(40)
        self.items2.setFeatures(QDockWidget.DockWidgetMovable)
        self.listWidget2=QListWidget()
        self.listWidget2.addItem('Item1')
        self.listWidget2.addItem('Item2')
        self.listWidget2.addItem('Item3')
        self.listWidget2.addItem('Item4')

        self.items2.setWidget(self.listWidget2)
        self.items2.setFloating(False)


        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea,self.items)
        self.addDockWidget(Qt.RightDockWidgetArea,self.items2)

        self.items3=QDockWidget('Dockable',self)
        self.b = QWidget()
        self.b.setMinimumSize(300, 300)
        self.b.setStyleSheet('background: pink')
        self.items3.setWidget(self.b)

        # Disable tabbing
        self.setDockOptions(QMainWindow.AllowNestedDocks)

        self.addDockWidget(Qt.RightDockWidgetArea,self.items3)

        layout.addWidget(self.b)

        self.setLayout(layout)
        self.setWindowTitle('Dock')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=DockDemo()
    demo.show()
    sys.exit(app.exec_())