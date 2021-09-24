import json

with open('03092021-20-44-17.json', 'r') as object_1:
    data = json.load(object_1)
c=0
for obj in data:
    c=c+1

def split_in_files(data, amount):
    step = len(data) // amount
    pos = 0
    res=data[pos:pos+step]
    print(type(res[0]))
    for i in range(amount - 1):
        with open('output_file{}.json'.format(i+1), 'w') as file:
            json.dump(res[0],file)        
            pos += step
          
    # last one
    res=data[pos:]
    with open('output_file{}.json'.format(amount), 'w') as file:
        json.dump(res[0], file)

split_in_files(data, c)