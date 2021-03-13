import mysql.connector

con=mysql.connector.connect(user='niminimda', password='******', host='127.0.0.1', database='test')
cursor=con.cursor()
cursor.execute('INSERT INTO people VALUES (\'yasaman\',23,\'f\')')
con.commit()
cursor.close()
con.close()