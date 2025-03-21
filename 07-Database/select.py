import sqlite3

cnx = sqlite3.connect('07-Database/db.sqlite3')
cursor = cnx.cursor()

print(">>>>> select * :")

sql = "select * from personne" # select nom,prenom from personne

cursor.execute(sql)

personnes  = cursor.fetchall() # renvoie une liste de tuples

print(personnes)

# unpacking: deballage d'un tuple -> extraire les éléments d'un tuple
for id,nom,prenom,age in personnes:
    print(f'Id: {id} - Nom: {nom} - Prénom: {prenom} - Age: {age}' )
    
print(cursor.fetchall()) # une fois le contenu du cursor consommé (ligne 12), ce dernier est réinitialisé en mémoire

print(">>>> select avec conditions")

sql = "select * from personne where id=?"

param = (1,)
print(type(param))
cursor.execute(sql,param)

print(cursor.fetchone())
print(cursor.fetchone()) # curseur vidé en mémoire

print(">>>>> select like")

sql = "select * from personne where nom like ?"

# n%: nom commençant par n
# %n: nom se terminant par n
# %n%: nom contenant n queque soit sa position

param = ['%y%']

cursor.execute(sql, param)
print(cursor.fetchall())

cursor.close()
cnx.close()