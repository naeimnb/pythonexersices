import mysql.connector

Host = input('host: ')
UserName = input('User Name: ')
PassWord = input('PassWord: ')
DataBase = input('DataBase: ')
Table = input('Table: ')
con = mysql.connector.connect(user=UserName, password=PassWord, host=Host, database=DataBase)
cursor = con.cursor()

uSr = 'myProjectIsBest'
c=0

def entry_mail(en_mail):
    insertMail = en_mail.split('@')
    if len(insertMail) == 2 and len(insertMail[1].split('.')) == 2:
        print('your email is correct.')
        return True
    else:
        if c !=0:
            print('the correct email is like naeim@yahoo.com')
            return False
        else:
            return False

while (not entry_mail(uSr)):
    c+=1
    uSr = input('email:')
    b = input('Password: ')

cursor.execute('INSERT INTO %s (username  ,password) VALUES ("%s" ,"%s")' % (Table, uSr, b))
con.commit()
cursor.close()
con.close()
