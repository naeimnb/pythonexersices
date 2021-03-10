import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        lines=csv.reader(f)
        karname=dict()
        for line in lines:
            name=line[0]
            list_data=list()
            for number in line[1:]:
                list_data.append(float(number))

            moadel=mean(list_data)
            karname[name]=moadel

    with open(output_file_name, 'w') as f:
        for item in karname.keys():
            print(item,karname[item] ,file=f)      

def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
    lst1=list()
    dic1=dict()
    lst2=list()
    for line in f:
        lst1.append(line.split())

    for item in lst1:
        dic1[float(item[1])]=item[0]
    
    for key in dic1.keys():
        lst2.append(key)
        lst2.sort()

    with open(output_file_name, 'w') as f:
        for item in lst2:
            print(dic1[item],item ,file=f)


def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name) as f:
        lst1=list()
        dic1=dict()
        lst2=list()
        for line in f:
            lst1.append(line.split())
    
        for item in lst1:
            dic1[float(item[1])]=item[0]
        
        for key in dic1.keys():
            lst2.append(key)
            lst2.sort(reverse=True)

    with open(output_file_name, 'w') as f:
        c=0
        for item in lst2:
            if c<3:
                c+=1
                print(dic1[item],item ,file=f)


def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name) as f:
        lst1=list()
        dic1=dict()
        lst2=list()
        for line in f:
            lst1.append(line.split())

        for item in lst1:
            dic1[float(item[1])]=item[0]
        
        for key in dic1.keys():
            lst2.append(key)
            lst2.sort()

    with open(output_file_name, 'w') as f:
        c=0
        for item in lst2:
            if c<3:
                c+=1
                print(item ,file=f)


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name) as f:
        lst1=list()
        dic1=dict()
        lst2=list()
        for line in f:
            lst1.append(line.split())

        for item in lst1:
            dic1[float(item[1])]=item[0]
        
        for key in dic1.keys():
            lst2.append(key)
            lst2.sort()
    with open(output_file_name, 'w') as f:
        average= mean(lst2)
        print(average,file=f)