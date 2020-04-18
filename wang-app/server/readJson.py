import json

f = open('books.json')

data = json.load(f)
#print(data)

for i in data['books']:
    print(i)
    # print(i.get("id"), end=': ')
    # print(i.get('title'))

f.close()
