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

        #print(read_dic)
        return(read_dic)


def creat_csv(adres):
    with open(adres,'w') as f: 
        for i in range(1000,9999): 
            savedstr=str(i)+','+ hashin(str(i))
            #print(type(savedstr))
            print(savedstr,file=f)

def creat_cracked_file(adres):
    with open(adres,'w') as f: 
        for item in dic_cracked:
            savedstr=item+','+ dic_cracked[item]
            print(savedstr, file=f)

#creat_csv('/home/naeim/Desktop/pythonexersices/projectfinal1/hash_file.csv')

address_sample='/home/naeim/Desktop/pythonexersices/projectfinal1/sample.csv'
address_hashed='/home/naeim/Desktop/pythonexersices/projectfinal1/hash_file.csv'
address_cracked='/home/naeim/Desktop/pythonexersices/projectfinal1/cracked_file.csv'

dic_sample=dict()
dic_hashed=dict()
dic_cracked=dict()

dic_sample=read_csv(address_sample)
#print(dic_sample['99b057c8e3461b97f8d6c461338cf664bc84706b9cc2812daaebf210ea1b9974'])
#print(dic_sample)
dic_hashed=read_csv(address_hashed)
#print(dic_hashed)
#print(dic_hashed['99b057c8e3461b97f8d6c461338cf664bc84706b9cc2812daaebf210ea1b9974'])

for item in dic_sample:
    #print(item)
    user_name=dic_sample[item]
    #print(user_name, dic_hashed[item])
    dic_cracked[user_name]=dic_hashed[item]

#print(dic_cracked)

creat_cracked_file(address_cracked)
