#
#   az site truecar    --> BMW   -->X6
#

import requests
from bs4 import BeautifulSoup
import re
import mysql.connector
from sklearn import tree


def add_data_to_db(val1, val2):
    con = mysql.connector.connect(user='niminimda', password='123456', host='127.0.01', database='test')
    query = 'INSERT INTO all_car (price, kar) VALUES ("%s", "%s")' % (str(val1), str(val2))
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

x=[]
y=[]
def data_reader():
    con = mysql.connector.connect(user='niminimda', password='123456', host='127.0.01', database='test')
    query = "SELECT * FROM all_car; "
    cursor = con.cursor()
    cursor.execute(query)
    for (price,kar) in cursor:
        #print(price,kar)
        price = price.strip()
        price = (lambda x: x.replace(',',''))(price)
        kar = kar.strip()
        kar = (lambda x: x.replace(',',''))(kar)
        #print(price,kar)
        x.append([int(kar)])
        y.append([int(price)])
    con.close()
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x, y)
    return clf


def update_db(page_num):
    for i in range(1, page_num):
        url = "https://www.truecar.com/used-cars-for-sale/listings/bmw/x6/?page=%i" % i
        res = requests.get(url)
        res = res.text
        soup = BeautifulSoup(res, "html.parser")
        vals1 = soup.find_all(attrs={'data-test': 'vehicleCardPricingBlockPrice'})
        vals2 = soup.find_all(attrs={'data-test': 'vehicleMileage'})
        allvals = zip(vals1, vals2)
        for val1, val2 in allvals:
            text_val1 = val1.text
            text_val2 = val2.text
            text_val1 = text_val1[1:]
            text_val2 = re.search('\d.*\s', text_val2)
            text_val2 = text_val2.group()
            # print(text_val1,text_val2)
            add_data_to_db(text_val1, text_val2)
def run_func():
    new_data = int(input('Lotfan mizane Karkarde BMW X6 khod ra vared nemiaeid: '))
    gheymat_dollar = int(input('gheymate dollar be toman: '))
    clf = data_reader()
    answers = clf.predict([[new_data]])
    gheymat_BMW = int(answers[0])
    gheymat_BMW_toman = gheymat_BMW * gheymat_dollar
    print('gheymate BMW X6 shoma $%i va %i toman mibashad' % (gheymat_BMW, gheymat_BMW_toman))


tamayol = input("aya mayel be beroz avarie database mibashid yes=1 no=0: ")
if tamayol == "1":
    meghdare_page = int(input('mizane safehate baraye update ra moshakhas nemiaeid: '))
    update_db(meghdare_page)
    run_func()
else:
    run_func()


