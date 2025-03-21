
# Seul le dossier en cours est visible par python: 09-Demo_Pyside

import sys
import os

chemin_dossier_principal = os.getcwd()
sys.path.append(chemin_dossier_principal)

from tools.filehelper import lecture_fichier_texte, ecriture_fichier_texte

# 2 classes importantes dans PySide

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox

# classe pour appliquer des templates
from PySide6 import QtCore

# importer la classe du design

from fenetre_ui import Ui_Form

# QApplication: permet de créer 1 seule application -> utiiser qu'1 seule fois
# QWidget: est la classe mère de tous les widgets


class Main_Fenetre(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # connecter btnValider à cette fonction
        self.btnValider.clicked.connect(self.addition)

        # gestion du btnLecture
        self.btnLecture.clicked.connect(self.lecture)

        # gestion du btnEcriture
        self.btnEcriture.clicked.connect(self.ecriture)




    #Définir une fonction pour chaque besoin fonctionnel
    def addition(self):
        nb1 = float(self.ed_nombre1.text())
        nb2 = float(self.ed_nombre2.text())
        somme = nb1 + nb2
        self.lblResultat.setText(str(somme))

    def lecture(self):
        # affichier une boite de dialogue pour selectionner le fichier à lire
        dialog = QFileDialog()
        resultat = dialog.exec() # renvoie 1 si un fichier est sélectionné sinon renvoie 0

        if resultat:
            chemin = dialog.selectedFiles()[0]
            contenu = lecture_fichier_texte(chemin)
            self.champsSaisie.setPlainText(contenu)

        else:
            boite_dialogue = QMessageBox()
            boite_dialogue.setText('Aucun fichier sélectionné...')
            boite_dialogue.setIcon(QMessageBox.Icon.Information)
            boite_dialogue.setWindowTitle("Lecture d'un fichier")
            boite_dialogue.exec()


    def ecriture(self):

        dialog = QFileDialog()
        resultat = dialog.exec() # renvoie 1 si un fichier est sélectionné sinon renvoie 0

        boite_dialogue = QMessageBox()
        boite_dialogue.setWindowTitle("Ecriture dans un fichier")

        if resultat:
            chemin = dialog.selectedFiles()[0]
            contenu = self.champsSaisie.toPlainText()
            ecriture_fichier_texte(chemin, contenu)
            boite_dialogue.setIcon(QMessageBox.Icon.Information)
            boite_dialogue.setText('Fichier sauvegardé dans: '+chemin)
            boite_dialogue.exec()

        else:
            
            boite_dialogue.setText('Aucune sauvegarde...')
            boite_dialogue.setIcon(QMessageBox.Icon.Information)
            boite_dialogue.exec()

        
        
# site pour templates qss: https://qss-stock.devsecstudio.com/



app = QApplication()

# f = QWidget()

# f.show()
dossier = os.path.dirname(__file__)
#theme = os.path.join(dossier, b'C:\\Users\\oem\\Desktop\\PythonAppro\\09-Demo_Pyside\\Adaptic.qss')

chemin_qss = b'C:\\Users\\oem\\Desktop\\PythonAppro\\09-Demo_Pyside\\Adaptic.qss'

style = QtCore.QFile(chemin_qss)
style.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)

my_style = style.readAll()

app.setStyleSheet(str(my_style, encoding='utf-8'))


f = Main_Fenetre()

f.show()


app.exec()

# Pour générer le .exe: pip install cx_Freeze
# Doc: https://python.doctor/page-cx_freeze-creer-executables-python-cours-apprendre