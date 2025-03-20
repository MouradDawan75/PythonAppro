# 1- Construire le chemin du fichier

#chemin = 'c:\\......\\demo.txt'

# module nécessaire pour la gestion des paths
import os 


print(__file__) # __file__: contient le chemin du fichier en cours: c:\...........\txt_file.py

chemin_dossier = os.path.dirname(__file__) # c:\....\02-txt_files

#chemin_fichier = chemin_dossier +'\demo.txt'

chemin_fichier = os.path.join(chemin_dossier, 'demo.txt') # join: génère un chemin selon l'os utilisé


# 2- Appelle de la fonction open
# Elle prend plusieurs paramètres
# - le chemin du fichier
# - mode d'accès: r: read, w:write, a: append -> pour un accès en écriture si le fichier n'existe pas, il sera crée par la fct open
# - encodage: 'utf-8'

#stream (flux) zone mémoire: sorte de canal intermédiaire entre une source et une destination^étre libérer
# Obligation: une doit êttre libérer à la fin de son utilisation


# Ecriture fichier

flux = open(chemin_fichier, 'a', encoding='utf-8')
flux.write('\nceci est le contenu du fichier')
flux.close()

# Context Manager (with resource): libère la ressource à la fin du bloc d'instructions

# Lecture fichier:

with open(chemin_fichier, 'r', encoding="utf-8") as flux:
    print(flux.read()) # Vous arrivez à la fin du fichier. La prochaine lecture n'aura aucune ligne à lire

    # Remettre le cusrseur au début du fichier
    flux.seek(0)
    # flux.seek(5): pointe vers le 6ème caractère dans le fichier
    # whence = 0: partir du début du fichier
    # whence = 1 : partir de la position du curseur
    # whence = 2 : partir de la fin du fichier

    print("*****************************")
    print(flux.read())
    print("*****************************")

    #flux.close() -> cose est appelée par le with

#print(flux.read())

# Pour connaitre l'encodage des caractères d'un fichier: utilisez le module externe chardet: 
# https://www.geeksforgeeks.org/character-encoding-detection-with-chardet-in-python/

# Test des fonctions de lecture et écriture fichier: 

# La liste des modules et packages visibles par Python est définie dans sys.path

import sys

print(sys.path) # Python ne vois que le dosier en cours 02-txt_files -> package se trouve en dehors de ce dossier

# Solution: ajouter le chemin du dossier principal dans sys.path

print(os.getcwd()) # renvoie le chemin du dossier principal

sys.path.append(os.getcwd())

#from tools import filehelper
from tools.filehelper import ecriture_fichier_texte,lecture_fichier_texte

chemin_fichier_test = os.path.join(chemin_dossier, 'test.txt')

ecriture_fichier_texte(chemin_fichier_test, 'contenu du fichier')
ecriture_fichier_texte(chemin_fichier_test, 'contenu du fichier', mode_ajout=True)

contenu = lecture_fichier_texte(chemin_fichier_test)
print(contenu)

print(">>>>>>>>Module os:")

# Get current working directory
print(os.getcwd())

# Création de répertoires:

chemin_dossier_en_cours = os.path.dirname(__file__)
chemin_nouveau_rep = os.path.join(chemin_dossier_en_cours, 'rep')

if os.path.exists(chemin_nouveau_rep):
    print('Dossier existant')
else:
    os.mkdir(chemin_nouveau_rep)
    print('Dossier crée')


print(">>>>>> Parcourir un répertoire:")

lst = os.listdir(chemin_dossier_en_cours)

for f in lst:
    print(f)

# Exo: lire tous les fichier .txt et sauvegarder le contenu dans un nouveau fichier new.txt
# contenu de new.txt
# >>>>>>>>>>>>>>> nom fichier lu
# contenu

contenu_final = ''

for fichier in lst:

    if fichier.endswith('.txt'):
        chemin = os.path.join(chemin_dossier_en_cours, fichier)
        contenu_final += '>>>>>>>>>>>>> Nom du fichier: '+fichier+'\n'+lecture_fichier_texte(chemin)+'\n'


if contenu_final:
    chemin_fichier_resultat = os.path.join(chemin_dossier_en_cours, 'new.txt')
    ecriture_fichier_texte(chemin_fichier_resultat, contenu_final)

else:
    print('Aucun fichier .txt trouvé.')

def check_permission(path):
    if os.access(path, os.R_OK):
        #appelle de la fct de lecture
        print('lecture ok')

    if os.access(path, os.W_OK):
        #appelle de la fct d'écriture
        print('écriture ok')


print(os.stat(chemin_fichier_resultat))

import subprocess

subprocess.Popen(['powershell', 'script shell'])