from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QDialog, QColorDialog

from datas.new_file import (
    setup_values,
    units,
    units_resolution,
    color_mode_res,
    color_profiles,
    pixel_aspect_ratio)
from styles.dialog import dialog_styles
from ui import new_fileui


class NewFileWidget(QDialog):
    def __init__(self, parent, save):
        super().__init__(parent)
        self.ui = new_fileui.Ui_NewFile()
        self.ui.setupUi(self)
        self.save = save
        self.parent = parent
        self.setStyleSheet(dialog_styles())

        row_index = 0
        setup_options = setup_values()
        doc_type_len = len(setup_options)
        q_color = QColor()
        q_color.setRedF(1.0)
        q_color.setGreenF(1.0)
        q_color.setBlueF(1.0)
        q_color.setAlphaF(1.0)
        self.bg_color = q_color

        self.selected_option = None

        self.ui.unitsHComboBox.addItems(units())
        self.ui.unitsWComboBox.addItems(units())
        self.ui.unitsResolutionComboBox.addItems(units_resolution())
        self.ui.colorModeResComboBox.addItems(color_mode_res())
        self.ui.colorProfileComboBox.addItems(color_profiles())
        self.ui.pixelAspectRatioComboBox.addItems(pixel_aspect_ratio())

        self.ui.colorPickerPushButton.clicked.connect(self.show_color_picker)

        self.ui.unitsHComboBox.setCurrentText('Inches')
        self.ui.unitsWComboBox.setCurrentText('Inches')

        for index, item in enumerate(setup_options):
            row_index += 1

            if item['items']:
                row_index += 1

                for size_obj in item['items']:
                    row_index += 1
                    self.ui.documentTypeComboBox.addItem(
                        size_obj['label']
                    )

            if index < doc_type_len - 1:
                self.ui.documentTypeComboBox.insertSeparator(row_index)

        self.ui.okPushButton.clicked.connect(self.create_new_file)

    @property
    def selected_option(self):
        return self._selected_option
    
    @selected_option.setter
    def selected_option(self, option):

        obj = {
            'width': '7',
            'units_w': 'Inches',
            'height': '5',
            'units_h': 'Inches',
            'color_mode': 'RGB Color',
            'units_c': '8 bit',
            'resolution': '300',
            'units_r': 'Pixels/Inch',
            'background_contents': 'White',
            'color_profile': 'Working RGB: sRGB IEC61966-2.1',
            'pixel_aspect_ratio': 'Square Pixels',
        }

        self._selected_option = obj

        # if self._selected_option is not None:
        self.ui.widthLineEdit.setText(obj['width'])
        self.ui.unitsWComboBox.setCurrentText(obj['units_w'])
        self.ui.heightLineEdit.setText(obj['height'])
        self.ui.unitsHComboBox.setCurrentText(obj['units_h'])
        self.ui.colorModeLineEdit.setText(obj['color_mode'])
        self.ui.colorModeResComboBox.setCurrentText(obj['units_c'])
        self.ui.resolutionLineEdit.setText(obj['resolution'])
        self.ui.unitsResolutionComboBox.setCurrentText(obj['units_r'])
        self.ui.backgroundContentsLineEdit.setText(obj['background_contents'])
        self.ui.colorProfileComboBox.setCurrentText(obj['color_profile'])
        self.ui.pixelAspectRatioComboBox.setCurrentText(obj['pixel_aspect_ratio'])

    def show_color_picker(self):
        bg_color = QColorDialog.getColor()

        if bg_color.isValid():
            self.bg_color = bg_color
            print('COLOR:', self.bg_color)
            self.ui.colorPickerPushButton.setStyleSheet(f'background-color: {self.bg_color.name()}')

    def create_new_file(self):
        self.save(self.parent, {
            'width': self.ui.widthLineEdit.text(),
            'units_w': self.ui.unitsWComboBox.currentText(),
            'height': self.ui.heightLineEdit.text(),
            'units_h': self.ui.unitsHComboBox.currentText(),
            'color_mode': self.ui.colorModeLineEdit.text(),
            'units_c': self.ui.colorModeResComboBox.currentText(),
            'resolution': self.ui.resolutionLineEdit.text(),
            'units_r': self.ui.unitsResolutionComboBox.currentText(),
            'background_contents': self.ui.backgroundContentsLineEdit.text(),
            'color_profile': self.ui.colorProfileComboBox.currentText(),
            'pixel_aspect_ratio': self.ui.pixelAspectRatioComboBox.currentText(),
            'bg_color': self.bg_color,
            'name': self.ui.nameLineEdit.text()})
        self.close()