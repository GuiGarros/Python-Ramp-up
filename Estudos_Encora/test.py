x = 5
y = 3

if x > y:
    print('True')

list = ['one', 'two', 'three']
found = False
for item in list:
    if 'two' in item:
        found = True
        break #object found

print(found)

if any('two' in item for list in item)