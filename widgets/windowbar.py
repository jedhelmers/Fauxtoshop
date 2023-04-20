from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QSize, QPoint
from PySide6.QtWidgets import QWidget, QMainWindow, QDockWidget, QFrame, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtGui import QIcon

from styles.window_panel import window_panel_style
from ui import windowsui
from ui import window_panelui


class WindowPanelWidget(QWidget):
    def __init__(self, window_data, index, window_icons, signaler=None):
        super().__init__()
        self.ui = window_panelui.Ui_PanelWidget()
        self.ui.setupUi(self)
        self.window_data = window_data
        self.signaler = signaler
        self.window_icons = []
        # self.setFloating(False)

        for item in self.window_data['items']:
            self.add_icon(item, index)

    def add_icon(self, icon_data, index):
        print(icon_data)
        button = QPushButton()
        button.setObjectName(icon_data['name'])
        button.setMinimumSize(QSize(32, 32))
        button.setMaximumSize(QSize(32, 32))
        button.setToolTip(icon_data['tooltip'])
        icon = QIcon()
        icon.addFile(icon_data['path'], QSize(), QIcon.Normal, QIcon.Off)
        button.setIcon(icon)
        button.setFlat(False)
        self.ui.widget.layout().addWidget(button)
        button.setText("")

        button.clicked.connect(
            lambda: self.on_window_select(button, icon_data['name'], index))
        
    def on_window_select(self, button, name, window_index):
        p = QPoint()
        self.current_window = name
        x = self.y()
        y = self.y()
        pos = button.mapToGlobal(p)

        window = {
            'name': self.current_window,
            'pos': pos,
        }

        self.signaler.show_window_panel.emit(window)

class WindowSignaler(QtCore.QObject):
    select_window = QtCore.Signal(str)


class WindowsWidget(QWidget):
    def __init__(self, signaler):
        super().__init__()
        self.ui = windowsui.Ui_Windows()
        self.ui.setupUi(self)
        self.signaler = signaler
        self.window_signaler = WindowSignaler()
        self.window_icons = []

        self.current_window = None

        # Disable tabbing
        # self.setDockOptions(QMainWindow.AllowNestedDocks)
        self.window_signaler.select_window.connect(self.select_window)

        self.add_window_icons()

    def select_window(self, str):
        pass

    def add_icon(self, icon_data, window_panel, window_index):
        button = QPushButton()
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
            lambda: self.on_window_select(button, icon_data['name'], window_index))

    def on_window_select(self, button, name, window_index):
        p = QPoint()
        self.current_window = name
        x = self.y()
        y = self.y()
        # print(self.width())
        # pos = self.mapFrom(self.parent(), p)
        pos = button.mapToGlobal(p)

        window = {
            'name': self.current_window,
            'pos': pos,
            'panel_contents': self.window_icons[window_index]
        }

        # print('window', window['panel_contents'])

        self.signaler.show_window_panel.emit(window)

    def add_window_icons(self):
        self.window_icons = [
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
            for window_index, window_data in enumerate(self.window_icons):
                window_panel = WindowPanelWidget(
                    window_data,
                    window_index,
                    self.window_icons,
                    self.signaler
                )
                window_panel.setStyleSheet(window_panel_style())

                self.ui.windowsWidget.layout().addWidget(window_panel)
            verticalSpacer = QSpacerItem(20, 425, QSizePolicy.Minimum, QSizePolicy.Expanding)
            self.ui.windowsWidget.layout().addItem(verticalSpacer)
            # self.addDockWidget(Qt.RightDockWidgetArea, self.ui.windowsWidget)

        except Exception as e:
            print(e)
            pass
