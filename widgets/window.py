from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget, QFrame, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtGui import QIcon

from styles.window_panel import window_panel_style
from ui import windowsui
from ui import window_panelui


class WindowPanelWidget(QWidget):
    def __init__(self, name, signaler=None):
        super().__init__()
        self.ui = window_panelui.Ui_PanelWidget()
        self.ui.setupUi(self)

class WindowsWidget(QWidget):
    def __init__(self, signaler):
        super().__init__()
        self.ui = windowsui.Ui_Windows()
        self.ui.setupUi(self)
        self.signaler = signaler

        self.current_window = None

        self.add_window_icons()

    def add_icon(self, icon_data, window_panel):
        button = QPushButton(self.ui.windowsWidget)
        button.setObjectName(icon_data['name'])
        button.setMinimumSize(QSize(32, 32))
        button.setMaximumSize(QSize(32, 32))
        button.setToolTip(icon_data['tooltip'])
        icon = QIcon()
        icon.addFile(icon_data['path'], QSize(), QIcon.Normal, QIcon.Off)
        button.setIcon(icon)
        button.setFlat(False)
        window_panel.ui.widget.layout().addWidget(button)
        button.setText("")

        button.clicked.connect(
            lambda: self.on_window_select(button, icon_data['name']))

    def on_window_select(self, button, name):
        self.current_window = name
        x = self.y()
        y = self.y()
        print(x, y, button.x(), button.y())
        window = {
            'name': self.current_window,
            'x': 100,
            'y': 200
        }
        self.signaler.show_window_flyout_panel.emit(window)

    def add_window_icons(self):
        window_icons = [
            {
                'chunk': '',
                'items': [
                    {'tooltip': 'actions', 'name': 'Actions', 'path': u':/images/images/window_actions.svg'},
                    {'tooltip': 'adjustments', 'name': 'Adjustments', 'path': u':/images/images/window_adjustments.svg'},
                    {'tooltip': 'brush settings', 'name': 'Brush Settings', 'path': u':/images/images/window_brush_settings.svg'},
                    {'tooltip': 'brushes', 'name': 'Brushes', 'path': u':/images/images/window_brushes.svg'},
                ]
            },
            {
                'chunk': '',
                'items': [
                    {'tooltip': 'channels', 'name': 'Channels', 'path': u':/images/images/window_channels.svg'},
                    {'tooltip': 'characters', 'name': 'Characters', 'path': u':/images/images/window_characters.svg'},
                    {'tooltip': 'comments', 'name': 'Comments', 'path': u':/images/images/window_comments.svg'},
                    {'tooltip': 'gradients', 'name': 'Gradients', 'path': u':/images/images/window_gradients.svg'},
                ]
            },
            {
                'chunk': '',
                'items': [
                    {'tooltip': 'history', 'name': 'History', 'path': u':/images/images/window_history.svg'},
                    {'tooltip': 'layers', 'name': 'Layers', 'path': u':/images/images/window_layers.svg'},
                    {'tooltip': 'libraries', 'name': 'Libraries', 'path': u':/images/images/window_libraries.svg'},
                    {'tooltip': 'paragraph', 'name': 'Paragraph', 'path': u':/images/images/window_paragraph.svg'},
                    {'tooltip': 'paths', 'name': 'Paths', 'path': u':/images/images/window_paths.svg'},
                ]
            },
            {
                'chunk': '',
                'items': [
                    {'tooltip': 'swatches', 'name': 'Swatches', 'path': u':/images/images/window_swatches.svg'},
                ]
            },
            {
                'chunk': '',
                'items': [
                    {'tooltip': 'patterns', 'name': 'Patterns', 'path': u':/images/images/window_patterns.svg'},
                    {'tooltip': 'properties', 'name': 'Properties', 'path': u':/images/images/window_properties.svg'},
                ]
            }

        ]

        try:
            for window_data in window_icons:
                window_panel = WindowPanelWidget(name=window_data['chunk'])
                window_panel.setStyleSheet(window_panel_style())

                for item in window_data['items']:
                    self.add_icon(item, window_panel)

                self.ui.windowsWidget.layout().addWidget(window_panel)

            verticalSpacer = QSpacerItem(20, 425, QSizePolicy.Minimum, QSizePolicy.Expanding)
            self.ui.windowsWidget.layout().addItem(verticalSpacer)

        except Exception as e:
            print(e)
            pass
