from random import sample

class ensan:
    count=0
    def __init__(self,nam,shomare):
        self.nam=str(nam)
        self.shomare=int(shomare)
        ensan.count+=1
    def tim(self):
        pass


class bazikon(ensan):
    count=0
    def tim(self):
        if self.shomare<=11:
            return('A')
        else:
            return('B')



def randi ():
   lst_randit=list()
   lst_randit=sample(range(1,23),22)
   return(lst_randit)


def name_bazikonan():
    #bazikon='mohsen - saman - shahroz - behroz - soheil - behzad - ali - reza - poria - poya - saeid - amin - mostafa - milad - khashayar - mohammad - farhad - mehdi - nima - akbar - maziar - hosein'
    bazikon='حسین - مازیار - اکبر - نیما -  مهدی - فرهاد - محمد - خشایار - میلاد - مصطفی - امین - سعید - پویا - پوریا - رضا - علی - بهزاد - سهیل - بهروز - شهروز - سامان - محسن'
    lst_bazikon=bazikon.split('-',)
    lst_bazikon_jadid=list()
    for esm in lst_bazikon:
        lst_bazikon_jadid.append(esm.split())
    return(lst_bazikon_jadid)




random_list=randi()
#print(random_list)
list_name_bazokonan=name_bazikonan()
ii=0
for bazikon_amade in list_name_bazokonan:
    Human=str(bazikon_amade[0])
    #print(Human)
    Human=bazikon(Human,random_list[ii])
    ii+=1
    print(Human.nam,Human.tim())