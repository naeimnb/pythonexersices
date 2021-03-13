import mysql.connector

con=mysql.connector.connect(user='niminimda', password='******', host='127.0.0.1', database='test')
cursor=con.cursor()
cursor.execute('INSERT INTO people VALUES (\'jasmine\',23,\'f\')')
con.commit()
cursor.close()
con.close()