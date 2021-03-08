import collections
tedad_ara=int(input(''))
vote=collections.OrderedDict()
for i in range(0,tedad_ara):
    countryName=input('')
    vote[countryName]=vote.get(countryName,0)+1

lst_contry=list(vote.keys())
lst_contry.sort()
for contry in lst_contry:
    print(contry, vote[contry])



