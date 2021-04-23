names = ['ali', 'naeim', 'mehrdad', 'masoud', 'omid']

print(names)
print(names[0])
print(names[-1])
print(names[-2].title())
message = f"Hello {names[-3].title()} and {names[0].title()} welcome to my program"
print(message)
names.append('milad')
popis = names.pop()
print(popis)
popis = names.pop()
print(popis)
names.insert(3, 'iran')
del names[0]
names.remove('mehrdad')
for name in names:
    print(name)

print('-------------------------------------------------------')

languages = list()
languages.append('farsi')
languages.append('kurdish')
languages.append('english')
languages.append('thai')
print(languages)
print(languages.sort())
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)
print(sorted(languages))
#print(languages)
print(sorted(languages, reverse=True))

print('-------------------------------------------------------')

computer_languages = ['c', 'delphi', 'C', 'F', 'python', 'go']
print(computer_languages)
computer_languages.reverse()
print(computer_languages)


print('-------------------------------------------------------')

alphabets = ['a','A', 'b', 'B','c','C', 'd', 'D','e','E', 'f', 'F']
print(alphabets)
alphabets.sort(reverse=True)
print(alphabets)
print(len(alphabets))
print('b' < 'a')
print('A' < 'a')
print('B' < 'a')

