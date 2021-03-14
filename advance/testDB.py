import mysql.connector
from mysql.connector import errorcode
try:
    con = mysql.connector.connect(user='niminimda', password='123456', host='127.0.01', database='test')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("something is wrong with user or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("db doesn't exists")
    else:
        print(err)
else:
    name = "Ali"
    age = 34
    sex = 'M'
    cursor = con.cursor()
    cursor.execute('INSERT INTO people VALUES("%s","%i","%s")' % (name, age, sex))
    con.commit()
    cursor.close()
    con.close()
