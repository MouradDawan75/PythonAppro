import mysql.connector 

cnx = mysql.connector.connect(
   user='root', 
   password='',
   host='localhost',
   database='pythondb'
  
)

cursor = cnx.cursor()

params = ('n1', 'p1')
try: 
    cursor.execute("insert into empoyes values (null, %s, %s)", params)
    cnx.commit()
except Exception as e:
    print(e)

cursor.execute("select * from empoyes")
print(cursor.fetchall())

