# Fonction d'écriture dans un fichier
import os
import threading

def ecriture_fichier_texte(chemin_fichier: str, contenu: str, mode_ajout: bool = False):
    """Fonction d'écriture dans un fichier texte.

    Args:
        chemin_fichier (str): chemin absolut du fichier. Ex: c:\\rep\\demo.txt
        contenu (str): texte à insérer dans le fichier
        mode_ajout (bool, optional): mettre à True pour un accès en mode append
    """
    mode = 'w'
    if mode_ajout:
        mode = 'a'
        contenu = '\n'+contenu

    with open(chemin_fichier, mode, encoding='utf-8') as flux:
        flux.write(contenu)




# Fonction de lecture d'un fichier texte

def lecture_fichier_texte(chemin_fichier: str) -> str:
    """Fonction de lecture d'un fichier texte.

    Args:
        chemin_fichier (str): chemin absolut du fichier à lire.

    Returns:
        str: le contenu du fichier
    """

    if os.path.exists(chemin_fichier):
        with open(chemin_fichier,'r', encoding='utf-8') as flux:
             contenu = flux.read()

        return contenu
    else:
        print('Chemin invalide.............')


# t1 = threading.Thread(target=ecriture_fichier_texte)
# t2 = threading.Thread(target=ecriture_fichier_texte)

# t1.start()
# t2.start()