import sqlite3

cnx = sqlite3.connect('07-Database/db.sqlite3')
cursor = cnx.cursor()

sql = "delete from personne where id=?"

param = (2,)

cursor.execute(sql,param)
cnx.commit()

cursor.close()
cnx.close()