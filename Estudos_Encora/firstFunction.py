#function don have delimiters 
def teste():
    x = 10
    y = x + 10
    print(y)
#python is oriented by identation, the syntax is extremely important 

#how to pass arguments to functions
def teste2(item1, item2, item3):
    soma = item1 + item2 + item3
    print(soma)
#functio + list
def teste3(my_list = []):
    my_list.append(1)
    return my_list
    
#main program
teste()
teste2(10, 20.5, 30)
my_list = [1, 2, 4]
my_list = teste3(my_list)
my_list = teste3(my_list)
print(my_list)