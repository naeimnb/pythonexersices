import mysql.connector
from mysql.connector import errorcode


def my_function():
    query = "CREATE TABLE employee (Name nvarchar(20), Weight int, Height int)"
    cursor = con.cursor()
    cursor.execute(query)
    cursor.close()


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
    my_function()

    con.close()
