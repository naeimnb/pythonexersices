import csv
import hashlib


def hashin(myPassword):
    myHash= hashlib.sha256(myPassword.encode('utf-8')).hexdigest()
    return(myHash)


with open('/home/naeim/Desktop/pythonexersices/projectfinal1/hash_cracker.csv','w') as f: 
    for i in range(1000,9999): 
        print(hashin(str(i)),i ,file=f)