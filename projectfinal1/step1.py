import csv
import hashlib


# define  hashing function
def hashin(myPassword):
    myHash= hashlib.sha256(myPassword.encode('utf-8')).hexdigest()
    return(myHash)

# print(hashin(input('')))


# define rading csv file
def read_csv(adres):
    with open(adres) as f: 
        lines=csv.reader(f) 
        read_dic=dict()
        for line in lines:
            user_name=line[0]
            for hash_pass in line[1:]:
                read_dic[hash_pass]=user_name

            print(read_dic)


def creat_hash_csv(adres):
    with open(adres,'w') as f: 
        for i in range(1000,9999): 
            print(hashin(str(i)),i ,file=f)

read_csv('/home/naeim/Desktop/pythonexersices/projectfinal1/sample.csv')
creat_hash_csv('/home/naeim/Desktop/pythonexersices/projectfinal1/hash_file.csv')

