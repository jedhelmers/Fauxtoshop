"""
(Re)compile all UI widgets.
"""
from os import scandir
import os

source_directory = './design'
target_directory = './ui'

def scantree(path):
    """Recursively yield DirEntry objects for given directory."""
    for entry in scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from scantree(entry)  # see below for Python 2.x
        else:
            yield entry

for direntry in scantree(source_directory):
    base_name, extension = os.path.splitext(direntry.path)

    if extension != '.ui':
        continue

    command = f'pyside6-uic {base_name}.ui -o {base_name.replace(source_directory, target_directory)}ui.py'
    os.system(command)

os.system("pyside6-rcc resources.qrc -o resources_rc.py")
print("compile_ui_widgets.py has been run successfully")
