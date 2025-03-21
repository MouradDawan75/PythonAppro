import mysql.connector 

cnx = mysql.connector.connect(
   user='root', 
   password='',
   host='localhost',
   database='pythondb'
  
)

cursor = cnx.cursor()

params = (5,'n1', 'p1')
try: 
    cursor.execute("insert into empoyes(id,nom,prenom) values (?, ?, ?)", params)
    cnx.commit()
except Exception as e:
    print(e)

cursor.execute("select * from empoyes")
print(cursor.fetchall())

