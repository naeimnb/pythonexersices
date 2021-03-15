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
    query = "SELECT * FROM employee; "
    cursor = con.cursor()
    cursor.execute(query)
    myData = cursor.fetchall()
    myData.sort(key=lambda x: x[2])
    for item in range(0, len(myData) - 1):
        if myData[item][2] == myData[item + 1][2]:
            if myData[item][1] < myData[item + 1][1]:
                x = myData[item]
                myData[item] = myData[item + 1]
                myData[item + 1] = x
    for y in range(len(myData) - 1, -1, -1):
        q = myData[y]
        print(q[0], q[1], q[2])
    cursor.close()
    con.close()
