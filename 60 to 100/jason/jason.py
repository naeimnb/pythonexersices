import json

names = ['ali', 'mehrdad', 'naeim', 'masoud', 'omid']

file_name = 'names.json'
with open(file_name, 'w') as f:
    json.dump(names, f)