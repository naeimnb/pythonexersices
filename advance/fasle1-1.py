def maghsomonAlayh(num):
    lst_maghsom=list()
    for i in range(1,num+1):
        if num%i==0:
            lst_maghsom.append(i)
        
    return(lst_maghsom)

def adadeAval(adad):
    c=0
    for i in range(1,adad):
        if adad%i==0:
            c+=1
    if c==1:
        return(True)
    else:
        return(False)

lst_input=list()
lst_maghosmonalayeha=list()
num_vorodi=0
for i in range(0,10):
    num_vorodi=int(input(''))
    lst_input.append(num_vorodi)

for number in lst_input:
    lst_maghosmonalayeha.append(maghsomonAlayh(number)) 

dic_tasmin=dict()
for item in lst_maghosmonalayeha:
    d=0
    for io in item:
       if adadeAval(int(io))==True:
        d+=1
    
    dic_tasmin[io]=d
lst_input.sort(reverse=True)
print(lst_input[0],dic_tasmin[lst_input[0]])


