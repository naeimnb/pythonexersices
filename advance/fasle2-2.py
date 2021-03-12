import datetime


def say_age(sal,mah,roz):
    tarikh_emroz=str(datetime.date.today()).split('-')
    sal_emroz=int(tarikh_emroz[0])
    mah_emroz=int(tarikh_emroz[1])
    roz_emroz=int(tarikh_emroz[2])
    if (sal_emroz-sal)<=0:
        print('WRONG')
    else:
        if (mah_emroz-mah)>=0:
            if (roz_emroz-roz)>=0:
                print(sal_emroz-sal)
            else:
                print(sal_emroz-sal-1)
        else:
            print(sal_emroz-sal-1)

        

    #print(mah_emroz-mah)
    #print(roz_emroz-roz)



Tarikh_tavalod = input('')
lst_tarikh_tavalod=Tarikh_tavalod.split('/')
#print(Tarikh_tavalod)
#print(lst_tarikh_tavalod)

#print(lst_tarikh_tavalod[0])
#print(len(lst_tarikh_tavalod[0]))
c=0
if(len(lst_tarikh_tavalod[0])!=4) or (int(lst_tarikh_tavalod[0]) < 0):
    c+=1
if (len(lst_tarikh_tavalod[1])!=2) or (int(lst_tarikh_tavalod[1]) > 12):
    c+=1
if (len(lst_tarikh_tavalod[2])!=2) or (int(lst_tarikh_tavalod[2]) > 31):
    c+=1

if c!=0:
    print('WRONG')
else:
    say_age(int(lst_tarikh_tavalod[0]),int(lst_tarikh_tavalod[1]),int(lst_tarikh_tavalod[2]))
    
