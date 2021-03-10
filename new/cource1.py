import csv
from statistics import mean
from collections import OrderedDict

with open('/home/naeim/Desktop/karname.csv') as f:
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

with open('/home/naeim/Desktop/task2.csv', 'w') as f:
    for item in lst2:
        print(dic1[item],item ,file=f)
    