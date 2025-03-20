# Contrairement à un fichier texte, un fichier json en plus du texte contient des données (listes,types numériques......)

import os
import json

chemin_dossier = os.path.dirname(__file__)
chemin_json = os.path.join(chemin_dossier, 'users.json')

# Lecture d'un json:

with open(chemin_json, 'r', encoding='utf-8') as flux:

    contenu = json.load(flux)

#print(contenu) -> est une liste de dict

for user in contenu:
    print(f"Name: {user.get('name')} - Email: {user.get('email')} - Ville: {user.get('address').get('city')}")


# Ecriture JSON:

chemin_sortie = os.path.join(chemin_dossier, 'sortie.json')
with open(chemin_sortie, 'w', encoding='utf-8') as flux:

    # Construction du contenu: doit être un dict ou une liste de dict
    donnee = {
        'python': 'Langage de programmation',
        'version': 3.13
    }
    json.dump(donnee, flux, indent=4, ensure_ascii=False) # ensure_ascii=True: tous les caractères non ascii seront ignorés

# Exo: a partir de users.json, construire un nouveau fichier ne contenant que les clés: email et username

# 1- Construire le contenu à insérer: une liste de dict

lst = []

for user in contenu:
    d = {
        'email': user.get('email'),
        'username': user.get('username')
    }

    lst.append(d)

# 2- Ecriture dans un fichier json

chemin_resultat = os.path.join(chemin_dossier, 'resultat.json')
with open(chemin_resultat, 'w', encoding='utf-8') as flux:

    json.dump(lst, flux, indent=4, ensure_ascii=False)

print(">>>>>>>>>>>>> Gestion des chaines sous format JSON: loads() et dumps()")

player = '{"first_name" : "FEDERER", "last_name": "Roger", "sport": "football"}'

# json.loads(): permet de convertir une chaine en objet (dict)

player_dict = json.loads(player)

print(player_dict.get('first_name'))
print(type(player_dict))


### update player_dict
player_dict['sport'] = 'tennis'

print(player_dict)

### ajouter des clés
player_dict['age'] = 39

print(player_dict)

### supprimer des clés
player_dict.pop("age")

print(player_dict)

player_nadal = '{"first_name" : "NADAL", "last_name": "Rafael", "sport": "Tennis", "Pays": "Espagne"}'

nadal_dict = json.loads(player_nadal)

### mise à jours d'un dictionnaire
player_dict = dict(player_dict) #-> nécessaire uniquement pour l'auto complétion
player_dict.update(nadal_dict)

print(player_dict)

# json.dumps(): permet de convertir un dictionnaire en chaine formattée en json

player_string = json.dumps(player_dict)

print(player_string)

#### load() et dump(): pour les fichiers json
#### loads() et dumps(): pour les chaines formattées en json

