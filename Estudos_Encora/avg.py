def avg(a):
    total = 0
    for v in a:
        total += v
    return total / len(a)

print(avg([1,2,3,4,5,6,7]))

dict = {"nome": "Ana", "idade": 25}

for v in dict:
    print(dict[v])