myString= input('')
myString = myString.lower()
newString=''
for harf in myString:
    if (harf!='a') and (harf!='e') and (harf!='i') and (harf!='o') and (harf!='u'):
        newString = newString+'.'+harf

print(newString)