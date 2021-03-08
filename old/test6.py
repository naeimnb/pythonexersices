textemon=input('')
tool_text=len(textemon)
c=0
d=0
for i in range(0,(tool_text-1)):
    if textemon[i]==textemon[-i-1]:
        c +=1
    else:
        d +=1

if c>d:
    print('palindrome')
else:
    print('not palindrome')