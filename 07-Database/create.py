# Quelque soit le type de base de données utiisée:
# 1 -Installer le connecteur via le pip
# 2- Se connecter en appelant la connect(paramètres de connexion)
# 3- Récupérer le flux en appelant la fonction cursor()
# 4- Exécuter les commandes sql via le flux en appelant la fonction execute(sql)

# Python propose un type de base données à utiliser: sqlite

import sqlite3

# Appelle de la fct connect:

cnx = sqlite3.connect('07-Database/db.sqlite3') # si base inexistante -> elle est générée par la fonction connect

# Récupérer le flux
cursor = cnx.cursor()

# Commandes sql:
# Commandes LMD: langage de manipulation de données: SELECT,INSERT,DELETE,UPDATE
# Commandes LDD: langage de définition de données (concerne la structure):CREATE, DROP, ALTER

cursor.execute("""

CREATE TABLE IF NOT EXISTS personne(
id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
nom varchar(30) NOT NULL,
prenom varchar(30) NOT NULL,
age int unsigned NOT NULL,
CONSTRAINT unique_names UNIQUE (nom,prenom)         
               
)

""")

# Insertion de données de test
# Les opérations d'écriture en base de données s'exécutent en mode transactionnel

try:

    # syntaxe déconseillée en pratique: injections sql
    cursor.execute("INSERT INTO personne(nom,prenom,age) values ('DUPONT', 'Jean', 50)")

    # protection: utilisez les commandes sql paramétrées:
    # les commandes sql paramètrées sont pré compilées, chargées en mémoire en attente de paramètres
    # possibilité de controller les paramètres fournis
    cursor.execute('insert into personne values (NULL,?,?,?)', ('BOUQUET','Caroline', 50))
    cursor.execute('insert into personne values (NULL,?,?,?)', ('CONNERY','Sean', 80))



    cnx.commit() # valide toutes les commandes

except Exception as e:
    print(e)
    cnx.rollback() # annule toutes les commandes sql

finally:
    cursor.close()
    cnx.close()

# def func(sql):
#     cursor.execute("INSERT INTO personne(nom,prenom,age) values ('DUPONT', 'Jean', 50)")


# def func2(nom,prenom,age):
#     # vérifier les params fournis
#     cursor.execute('insert into personne values (NULL,?,?,?)', (nom,prenom,age))

# Pour la base sql lite:
# 1 -installer un client externe sqlite browser
# 2- Dans vs code: extension sqlite viewer