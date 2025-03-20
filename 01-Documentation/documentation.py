
"""
Ce modue contient des fonctions très utiles.
Le module documentation s'utilise dans plusieurs cas de figure.......

"""


# Documentation technique:
# En Python, on peut documenter les modules et les fonctions




import math

print(math.__doc__)

print(math.sqrt.__doc__)

print(help(math.sqrt))

# 3 syntaxes en Python

###### Syntaxe EpyText
"""
Doc EpyText

@param param1: décrire param1
@param param2: décrire param2
@return: décrire ce qui retourné


"""

###### Syntaxe reST
"""
Doc reST

:param param1: décrire param1
:param param2: décrire param2
:return: décrire ce qui retourné


"""

###### Syntaxe Google: la plus utilisée car plus lisible
"""
Doc Google

Args:
    param1: décrire param1
    param2: décrire param2

returns:
    Décrire le résultat renvoyé


"""

# Dans Vs code: installez l'extension docstring

def addition(x:int, y:int) -> int:
    """Fonction qui renvoie la somme de 2 entiers

    Args:
        x (int): est un entier
        y (int): est un entier

    Returns:
        int: somme de x et y
    """
    return x+y

# pdoc: module externe permettant de générer la documentation sous format html
# créer un env. virtuel: python -m venv myenv (nom_env)
# activation de l'env. virtuel: .\myenv\Scripts\activate

# pip: gestionnaire de modules externes
# pip list
# pip install nom_module
# pip uninstall nom_module

# commande a exécuter dnas terminal: pdoc chemin_module_python -o emplacement_doc
# pdoc 01-Documentation//documentation.py -o doc

