
# 2 classes importantes dans PySide

from PySide6.QtWidgets import QApplication, QWidget

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




    #Définir une fonction pour chaque besoin fonctionnel
    def addition(self):
        nb1 = float(self.ed_nombre1.text())
        nb2 = float(self.ed_nombre2.text())
        somme = nb1 + nb2
        self.lblResultat.setText(str(somme))
        

app = QApplication()

# f = QWidget()

# f.show()

f = Main_Fenetre()
f.show()


app.exec()