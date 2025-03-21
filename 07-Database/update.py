import sqlite3

cnx = sqlite3.connect('07-Database/db.sqlite3')
cursor = cnx.cursor()

sql = "update personne set nom=:last_name,prenom=:first_name,age=:age where id=:id" # paramètres nommés -> a fournir via un dict

# paramètres anonymes -> a fournir via un tuple (nom,prenom,age,id) -> tenir compte de leur position dans la commande sql
#sql = "update personne set nom=?prenom=?,age=? where id=?" 


params = {
    'id' : 3,
    'last_name' : 'new nom',
    'first_name' : 'new prenom',
    'age' : 99
    
}

cursor.execute(sql,params)
cnx.commit()

cursor.close()
cnx.close()