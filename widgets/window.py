from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget, QFrame, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtGui import QIcon

from ui import windowsui

class WindowsWidget(QWidget):
    def __init__(self, signaler):
        super().__init__()
        self.ui = windowsui.Ui_Windows()
        self.ui.setupUi(self)

        self.add_toolbar_icons()

    def add_icon(self, icon_path):
        button = QPushButton(self.ui.windowsWidget)
        button.setObjectName(icon_path['name'])
        button.setMinimumSize(QSize(32, 32))
        button.setMaximumSize(QSize(32, 32))
        button.setToolTip(icon_path['tooltip'])
        icon = QIcon()
        icon.addFile(icon_path['path'], QSize(), QIcon.Normal, QIcon.Off)
        button.setIcon(icon)
        button.setFlat(False)
        self.ui.verticalLayout.addWidget(button)
        self.ui.verticalLayout.insertWidget(self.ui.verticalLayout.count() - 1, button)
        button.setText("")

        button.clicked.connect(
            lambda: self.on_toolbar_icon_click(icon_path['name']))

    def on_toolbar_icon_click(self, name):
        self.current_tool = name

    def add_toolbar_icons(self):
        toolbar_icons = [
            {'tooltip': 'actions', 'name': 'Actions', 'path': u':/images/images/window_actions.svg'},
            {'tooltip': 'adjustments', 'name': 'Adjustments', 'path': u':/images/images/window_adjustments.svg'},
            {'tooltip': 'brush settings', 'name': 'Brush Settings', 'path': u':/images/images/window_brush_settings.svg'},
            {'tooltip': 'brushes', 'name': 'Brushes', 'path': u':/images/images/window_brushes.svg'},
            {'tooltip': 'channels', 'name': 'Channels', 'path': u':/images/images/window_channels.svg'},
            {'tooltip': 'characters', 'name': 'Characters', 'path': u':/images/images/window_characters.svg'},
            {'tooltip': 'comments', 'name': 'Comments', 'path': u':/images/images/window_comments.svg'},
            {'tooltip': 'gradients', 'name': 'Gradients', 'path': u':/images/images/window_gradients.svg'},
            {'tooltip': 'history', 'name': 'History', 'path': u':/images/images/window_history.svg'},
            {'tooltip': 'layers', 'name': 'Layers', 'path': u':/images/images/window_layers.svg'},
            {'tooltip': 'libraries', 'name': 'Libraries', 'path': u':/images/images/window_libraries.svg'},
            {'tooltip': 'paragraph', 'name': 'Paragraph', 'path': u':/images/images/window_paragraph.svg'},
            {'tooltip': 'paths', 'name': 'Paths', 'path': u':/images/images/window_paths.svg'},
            {'tooltip': 'patterns', 'name': 'Patterns', 'path': u':/images/images/window_patterns.svg'},
            {'tooltip': 'properties', 'name': 'Properties', 'path': u':/images/images/window_properties.svg'},
            {'tooltip': 'swatches', 'name': 'Swatches', 'path': u':/images/images/window_swatches.svg'},
        ]

        try:
            for icon_path in toolbar_icons:
                self.add_icon(icon_path)

            verticalSpacer = QSpacerItem(20, 425, QSizePolicy.Minimum, QSizePolicy.Expanding)
            self.ui.windowsWidget.layout().addWidget(verticalSpacer)
        except Exception as e:
            print(e)
            pass
