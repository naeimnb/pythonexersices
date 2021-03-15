import re
entry_email = input()

def list_get (lis,xi,yi):
    if len(lis) > xi :
        return lis[xi]
    else:
        return yi
def in1 (x):
    return re.findall("^[\w\d]+@\w+\.[\w]+$",x)


if re.findall(".+@[^\d]+\.[^\d]+",list_get(in1(entry_email),0,'')) == []:
    print ('WRONG')
else:
    if re.findall('[^\d]',list_get(re.findall ('^(.+)@',entry_email),0,'')) != []:
        print('OK')
    else:
        print('WRONG')