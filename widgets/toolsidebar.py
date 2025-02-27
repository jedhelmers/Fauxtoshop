from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QSize, QRect
from PySide6.QtWidgets import QWidget, QDialog, QGraphicsSceneMouseEvent, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QFrame, QLabel, QPushButton
from PySide6.QtGui import QIcon, QColor

from functions import new_file
from ui import toolbarui
from widgets.color_picker import ColorPickerWidget
from widgets.new_file import NewFileWidget
from widgets.tools.text_options import TextOptionsWidget


class ColorSwatch(QGraphicsRectItem):
    def __init__(self, callback, index, set_active):
        super().__init__()
        self.callback = callback
        self.index = index
        self.set_active = set_active

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        # Call callback function
        # TODO: maybe turn this into a signal
        if self.callback:
            self.callback(self.brush().color(), self)

        # Set z value so swatch is on top
        # self.setZValue(1)
        # self.set_active(self.index)
        
        return super().mousePressEvent(event)

    def set_color(self, color):
        self.setBrush(color)


class ColorSwatches(QGraphicsScene):
    def __init__(self, parent, set_color):
        super().__init__(parent=parent)
        self.set_color = set_color
        self.active_swatch = None

        self.setBackgroundBrush(Qt.transparent)
        self.background_color = QColor(255, 255, 255)
        self.foreground_color = QColor(0, 0, 0)

        # view.setScene(scene)
        self.front = ColorSwatch(self.set_color, 0, self.set_active)
        self.front.setBrush(self.background_color)
        self.front.setRect(QRect(0, 0, 19, 19))

        self.back = ColorSwatch(self.set_color, 1, self.set_active)
        self.back.setRect(QRect(10, 10, 19, 19))
        self.back.setBrush(self.foreground_color)

        self.addItem(self.back)
        self.addItem(self.front)

        self.active_swatch = self.front

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        # self.reset_z_index()

        if self.set_color:
            self.set_color(self.active_swatch.brush().color(), self)

        return super().mousePressEvent(event)

    def reset_z_index(self):
        # Reset ALL z values to 0
        for child in self.items():
            child.setZValue(0)

    def flip_active(self):
        current_index = self.active_swatch.index
        self.reset_z_index()
        self.set_active(abs(current_index - 1))
        self.active_swatch.setZValue(1)
        self.parent().tool.brush_color =  self.active_swatch.brush().color()
        print('SWATCH COLOR', self.active_swatch.brush().color())

    def set_active(self, index):
        self.reset_z_index()

        if index == 0:
            self.active_swatch = self.front
        else:
            self.active_swatch = self.back


class ToolSidebarWidget(QWidget):
    def __init__(self, main_signaler, tool):
        # TODO: Clean this thing up
        super().__init__()
        self.ui = toolbarui.Ui_Toolbar()
        self.ui.setupUi(self)
        self.main_signaler = main_signaler
        self.tool = tool

        self._current_tool = 'text'
        self.current_tool = 'text'

        # UI
        self.ui.toolbarWidget.layout().setAlignment(Qt.AlignTop)

        # Render icons
        self.render()

        # Color Front/Back
        view = QGraphicsView()
        view.setMaximumHeight(40)
        view.setMaximumWidth(40)
        view.setStyleSheet('background: transparent;')
        self.color_swatches = ColorSwatches(self, self.set_color)
        view.setScene(self.color_swatches)

        self.ui.verticalLayout.insertWidget(self.ui.verticalLayout.count(), view)


    @property
    def current_tool(self):
        return self._current_tool

    @current_tool.setter
    def current_tool(self, tool):
        """
        Set tool and remove button style from previously selected tool.
        """
        old_button = self.findChild(QPushButton, self.current_tool)
        button = self.findChild(QPushButton, tool)

        if old_button is not None:
            old_button.setStyleSheet('QPushButton {background-color: transparent;}')

        if button is not None:
            button.setStyleSheet('QPushButton {background-color: rgba(255, 255, 255, .25);}')

        self._current_tool = tool
        self.select_tool()

    def set_color(self, color, swatch):
        current_color = color
        color_picker = ColorPickerWidget(self, current_color)
        color_picker.setWindowFlags(Qt.Tool)
        color_picker.setModal(True)

        if color_picker.exec() == QDialog.Accepted:
            self.main_signaler.update_tool_property.emit({'key': 'brush_color', 'value': color_picker.new_color})
            self.color_swatches.active_swatch.set_color(color_picker.new_color)
            # self.main_signaler.update_tool_property.emit({'key': 'opacity', 'value': 0.10})
            pass
        else:
            print('WOO')

    def on_toolbar_icon_click(self, name):
        self.current_tool = name
        self.main_signaler.set_active_tool.emit(name)

    def select_tool(self):
        # self.main_signaler.select_tool.emit(self.current_tool)
        # self.tool.active_tool = 'move'
        pass

    def add_icon(self, icon_path):
        button = QPushButton(self.ui.toolbarWidget)
        button.setObjectName(icon_path['name'])
        button.setMinimumSize(QSize(32, 32))
        button.setMaximumSize(QSize(32, 32))
        button.setToolTip(icon_path['tooltip'])
        icon = QIcon()
        icon.addFile(icon_path['path'], QSize(), QIcon.Normal, QIcon.Off)
        button.setIcon(icon)
        button.setFlat(False)
        # self.ui.verticalLayout.addWidget(button)
        self.ui.verticalLayout.insertWidget(self.ui.verticalLayout.count(), button)
        button.setText("")

        button.clicked.connect(
            lambda: self.on_toolbar_icon_click(icon_path['name']))

    def add_toolbar_icons(self):
        toolbar_icons = [
            {'path': u':/images/images/toolbar_move.svg', 'tooltip': 'Move (space)', 'name': 'move'},
            {'path': u':/images/images/toolbar_dashed_box.svg', 'tooltip': 'Selection', 'name': 'dashed_box'},
            {'path': u':/images/images/toolbar_polygon_lasso.svg', 'tooltip': 'Polygon Lasso (w)', 'name': 'polygon_lasso'},
            {'path': u':/images/images/toolbar_a_pointer.svg', 'tooltip': 'Pointer', 'name': 'a_pointer'},
            {'path': u':/images/images/toolbar_rectangle.svg', 'tooltip': 'Rectangle', 'name': 'rectangle'},
            {'path': u':/images/images/toolbar_brush.svg', 'tooltip': 'Brush (b)', 'name': 'brush'},
            {'path': u':/images/images/toolbar_brush_arrow.svg', 'tooltip': 'Brush Arrow', 'name': 'brush_arrow'},
            {'path': u':/images/images/toolbar_crop.svg', 'tooltip': 'Crop (c)', 'name': 'crop'},
            {'path': u':/images/images/toolbar_eraser.svg', 'tooltip': 'Eraser (e)', 'name': 'eraser'},
            {'path': u':/images/images/toolbar_eyedropper.svg', 'tooltip': 'Eyedropper (i)', 'name': 'eyedropper'},
            {'path': u':/images/images/toolbar_frame.svg', 'tooltip': 'Frame', 'name': 'frame'},
            {'path': u':/images/images/toolbar_gradient.svg', 'tooltip': 'Gradient', 'name': 'gradient'},
            {'path': u':/images/images/toolbar_pointer_finger.svg', 'tooltip': 'pointer_finger', 'name': 'pointer_finger'},
            {'path': u':/images/images/toolbar_pin.svg', 'tooltip': 'Pin', 'name': 'pin'},
            {'path': u':/images/images/toolbar_pen.svg', 'tooltip': 'Pen (p)', 'name': 'pen'},
            {'path': u':/images/images/toolbar_quick_selection.svg', 'tooltip': 'quick_selection', 'name': 'quick_selection'},
            {'path': u':/images/images/toolbar_spot_headling.svg', 'tooltip': 'spot_headling', 'name': 'spot_headling'},
            {'path': u':/images/images/toolbar_stamp.svg', 'tooltip': 'Stamp (s)', 'name': 'stamp'},
            {'path': u':/images/images/toolbar_t.svg', 'tooltip': 'Text', 'name': 'text'},
            {'path': u':/images/images/toolbar_rotate_view.svg', 'tooltip': 'rotate_view', 'name': 'rotate_view'},
            {'path': u':/images/images/toolbar_zoom.svg', 'tooltip': 'Zoom (⌘ +/-)', 'name': 'zoom'},
        ]

        try:
            for icon_path in toolbar_icons:
                self.add_icon(icon_path)
        except Exception as e:
            print(e)
            pass

    def render(self):
        self.add_toolbar_icons()