import csv
with open('/home/naeim/Desktop/pythonexersices/projectfinal1/sample.csv') as f: 
    lines=csv.reader(f) 
    read_dic=dict()
    for line in lines:
        user_name=line[0]
        list_pass_hash_shode=list()
        for hash_pass in line[1:]:
            read_dic[hash_pass]=user_name

        print(read_dic)
