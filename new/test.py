import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    def hashin(myPassword):
        myHash= hashlib.sha256(myPassword.encode('utf-8')).hexdigest()
        return(myHash)
    
    def read_csv(adres):
        with open(adres) as f: 
            lines=csv.reader(f)
            read_dic=dict()
            for line in lines:
                user_name=line[0]
                for hash_pass in line[1:]:
                    read_dic[hash_pass]=user_name

            return(read_dic)

    def creat_csv(adres):
        with open(adres,'w') as f: 
            for i in range(1000,9999): 
                savedstr=str(i)+','+ hashin(str(i))
                print(savedstr,file=f)
    
    def creat_cracked_file(adres):
        with open(adres,'w') as f: 
            for item in dic_cracked:
                savedstr=item+','+ dic_cracked[item]
                print(savedstr, file=f)
    

    dic_sample=dict()
    dic_hashed=dict()
    dic_cracked=dict()

    dic_sample=read_csv(input_file_name)

    for i in range(1000,9999): 
        dic_hashed[hashin(str(i))]=str(i)

    for item in dic_sample:
        user_name=dic_sample[item]
        #print(user_name)
        #print(dic_hashed)
        dic_cracked[user_name]=dic_hashed[item]

    creat_cracked_file(output_file_name)





input_file_name='/home/naeim/Desktop/pythonexersices/projectfinal1/sample.csv'
output_file_name='/home/naeim/Desktop/pythonexersices/projectfinal1/cracked_file_new.csv'
hash_password_hack(input_file_name, output_file_name)