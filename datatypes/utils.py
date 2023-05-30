from PySide6.QtWidgets import QMainWindow, QFrame


# RULER LINES
# Create a Ruler class to handle all this.
class QHLine(QFrame):
    def __init__(self, parent, width=20, thickness=1):
        super(QHLine, self).__init__(parent=parent)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setMaximumHeight(thickness)
        self.setMaximumWidth(width)
        self.setStyleSheet('border-color: rgba(255, 255, 255, 0.1)')


class QVLine(QFrame):
    def __init__(self, parent, height=20, thickness=1):
        super(QVLine, self).__init__(parent=parent)
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setMaximumWidth(thickness)
        self.setMaximumHeight(height)
        self.setStyleSheet('border-color: rgba(255, 255, 255, 0.1)')

