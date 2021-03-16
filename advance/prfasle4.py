import requests
import re
from bs4 import BeautifulSoup
import mysql.connector


def add_data_to_db(val1, val2):
    con = mysql.connector.connect(user='niminimda', password='123456', host='127.0.01', database='test')
    query = 'INSERT INTO all_car (price, kar) VALUES ("%s", "%s")' % (str(val1), str(val2))
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
my_url = "https://www.truecar.com/used-cars-for-sale/listings/bmw/"

my_string = requests.get(my_url)
my_text = my_string.text
# print(my_text)

soup = BeautifulSoup(my_text, 'html.parser')

# print(soup)

vals1 = soup.find_all(attrs={'data-test': 'vehicleCardPricingBlockPrice'})
vals2 = soup.find_all(attrs={'data-test': 'vehicleMileage'})
allvals = zip(vals1, vals2)

count = 0
for val1, val2 in allvals:
    text_val1 = val1.text
    text_val2 = val2.text
    text_val1 = text_val1[1:]
    text_val2 = re.search('\d.*\s', text_val2)
    text_val2= text_val2.group()
    print(text_val1,text_val2)
    add_data_to_db(text_val1, text_val2)
    count += 1
    if count == 20:
        break
