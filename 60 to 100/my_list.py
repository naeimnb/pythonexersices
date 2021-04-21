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
for name in names:
    print(name)