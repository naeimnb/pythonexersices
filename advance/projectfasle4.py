import requests
from bs4 import BeautifulSoup
import re
import mysql.connector


u = input('user: ')
p = input('pass: ')
h = input('host: ')
db = input('database: ')
table = input('table: ')
#con = mysql.connector.connect(user=u ,password=p,host=h,database=db)
#cursor = con.cursor()
#cursor.close()
#con.close()

r=requests.get('https://www.truecar.com/used-cars-for-sale/listings/bmw/x6/?sort=best_match')

mytext=r.text
my_lst=list()
my_dic=dict()

regex = r"vehicleCardPricingBlockPrice.*?(\$.*?)\<.*?<\/svg>(\d+.*?)\<"
matches = re.finditer(regex, mytext, re.MULTILINE)
for i in matches:
    print(i)