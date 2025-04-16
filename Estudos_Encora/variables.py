#how to use variables and expressions in python

x = 0
y = 5

if x < y:
    print(x, " is less than ", y)

if y < x:
    print(y, "is less than ", x)

if x:
    print(x)

if y:
    print(y)

print("X or Y:")
if x or y:
    print(x or y)

print("X and y")
if x and y:
    print(x and y)

if 'aul' in 'grault':
    print('aul' in 'grault')

if 'quux' in ['foo', 'bar', 'baz', 'quux']:
    print('quux' in ['foo', 'bar', 'baz', 'quux'])

if any('quux' in item for item in ['foo', 'bar', 'baz', 'quuxx']):
    print(any('quux' in item for item in  ['foo', 'bar', 'baz', 'quuxx']))