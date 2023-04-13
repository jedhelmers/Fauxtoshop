"""
(Re)compile all UI widgets.
"""

import os

source_directory = 'design'
target_directory = 'ui'
command_pattern = "pyside6-uic {}/{}.ui -o {}/{}ui.py".format(
    source_directory, "{}", target_directory, "{}")

for direntry in os.scandir(source_directory):
    if not direntry.is_file():
        continue

    base_name, extension = os.path.splitext(direntry.name)

    if extension != '.ui':
        continue

    command = command_pattern.format(base_name, base_name)
    os.system(command)

os.system("pyside6-rcc resources.qrc -o resources_rc.py")
print("compile_ui_widgets.py has been run successfully")
