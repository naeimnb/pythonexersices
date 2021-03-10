import csv
from statistics import mean
from collections import OrderedDict

with open('/home/naeim/Desktop/nomarat.csv') as f:
    lines=csv.reader(f)
    karname=dict()
    for line in lines:
        name=line[0]
        list_data=list()
        for number in line[1:]:
            list_data.append(float(number))

        moadel=mean(list_data)
        karname[name]=moadel

with open('/home/naeim/Desktop/karname.csv', 'w') as f:
    for item in karname.keys():
        print(item,karname[item] ,file=f)