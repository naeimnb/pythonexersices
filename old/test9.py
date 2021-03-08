text = input('')
text_list=text.split()
for i in range(0,len(text_list)):
    text_list[i]=int(text_list[i])

text_list_min=min(text_list)
text_list_max=max(text_list)
answer= text_list_max- text_list_min
print(answer)