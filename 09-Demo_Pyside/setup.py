from cx_Freeze import setup, Executable
import sys
import os


chemin_dossier = os.path.dirname(__file__)
chemin_dossier_principal = os.path.dirname(chemin_dossier)
sys.path.append(chemin_dossier_principal)

from tools import filehelper


options = {
    "packages": ['tools'],
    "includes": ["sys","os","fenetre_ui",'application'],
    "include_files": ["Adaptic.qss", 'icon.ico', 'fenetre_ui.py','application.py','C:\\Users\\oem\\Desktop\\PythonAppro\\tools\\filehelper.py'],
    "excludes": ['']
}

target = Executable(
script='application.py',
base='Win32Gui',
icon='icon.ico'

)

setup(
    name = "demo_exe",
    version = "1",
    description = "Votre programme",
    options= {'build_exe': options},
    executables = [target]
)