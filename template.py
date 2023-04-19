import re

toolbar_icons = []

def FixCase(st):
   return ''.join(''.join([w[0].upper(), w[1:].lower()]) for w in re.split('_', st))

for tool in toolbar_icons:
   f = open('./widgets/tools/template.py', 'r')
   f2 = open(f'./widgets/tools/{tool["name"]}.py', 'w')
   UI_NAME = FixCase(tool['name'])
   UI_NAME_LOWER = tool['name']
   f2.write(f.read().replace('UI_NAME_LOWER', UI_NAME_LOWER).replace('UI_NAME', UI_NAME))
   f.close()
   f2.close()

# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QWidget

# from ui import BrushArrowui


# class BrushArrowOptionsWidget(QWidget):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.ui = brush_arrowui.Ui_brush_arrowOptions()
#         self.ui.setupUi(self)
