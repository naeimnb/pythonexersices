import bs4
import requests

myurl= requests.get('https://divar.ir/s/bijar')
soup = bs4.BeautifulSoup(myurl.text, 'html.parser')
mydata = soup.findAll('a')


c = 0
for item in mydata[36:]:
    mored = item.text
    if 'توافقی' in mored:
        print('\n\n\n\n%i:\n%s' % (c, mored))
        c += 1
