search_text=input('')
low='abcdefghijklmnopqrstuvwxyz'
up='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l=0
u=0
for char in search_text:
    for char_low in low:
        if char==char_low:
            l +=1
    
    for char_up in up:
        if char==char_up:
            u +=1
            
if u>l:
    search_text=search_text.upper()
else:
    search_text=search_text.lower()

print(search_text)

        
    