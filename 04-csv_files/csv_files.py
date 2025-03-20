import os
import csv

chemin_dossier = os.path.dirname(__file__)
chemin_csv = os.path.join(chemin_dossier, 'demo_file.csv')

# Lecture d'un csv

contenu = []

with open(chemin_csv, 'r', encoding='utf-8') as flux:
    curseur = csv.reader(flux, delimiter=",")
    #cursuer: pointeur en mémoire vers toutes les du csv

    for ligne in curseur:
        contenu.append(ligne) # une ligne est une liste

        # possibilité de traiter la ligne en cours selon les besoins
        for e in ligne:
            if e == 'mot recherché':
                pass

print(contenu) # contenu est une liste de listes

# Ecriture dans un csv

chemin_copie = os.path.join(chemin_dossier, 'copie.csv')

# 1- Construction du contenu:
# Pour insérer 1 ligne: on doit fournir une liste
# Pour insérer plusieurs lignes: on fournir une liste de listes

with open(chemin_copie, 'w', encoding='utf-8') as flux:

    curseur = csv.writer(flux, delimiter=';', lineterminator='\n')

    # Insertion ligne/ligne
    # for ligne in contenu:
    #     curseur.writerow(ligne)

    # Inserer toutes lignes d'un coup
    curseur.writerows(contenu)


lst = [1,2,3,4]

l1 = lst[:3]

print(">>>>>>>>>>>>>>>>>>>>>>>>Exploration d'un csv") 

chemin = os.path.join(chemin_dossier, 'deces_usa.csv')

with open(chemin, 'r', encoding='utf-8') as flux:
    reader = csv.reader(flux)
    data = list(reader)

print(">>>> Afficher les 5 premières lignes:")

print(data[:5])

# sauvegarde de l'entête
header = data[:1]

# suppression du header
data = data[1:]

print(">>> nombre de décès par année:")

# construire un dictionnaire contenant le nombre de décès par année

years = [e[1] for e in data] # Comprehension List

annees = []

for e in data:

    # e est une liste (1 ligne du csv)
    annees.append(e[1])


#print(annees)

annees_dict = {}

for annee in annees:

    # créer la clé 1 seule fois:
    if annee not in annees_dict:
        annees_dict[annee] = 0

    # a chaque passage on incrémente de 1
    annees_dict[annee] += 1

print(annees_dict)