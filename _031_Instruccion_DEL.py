#La instrucción del descrita anteriormente puede eliminar más de un elemento de la lista a la vez - también puede eliminar rebanadas
#Por ejemplo, para eliminar los primeros tres elementos de la lista, podemos hacer lo siguiente:
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

print("\n----------------------\n")

#Para eliminar todos los elementos de la lista, podemos usar la instrucción del con una rebanada que contiene todos los elementos de la lista.
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)#salida: []

print("\n----------------------\n")

#También podemos eliminar la lista completa utilizando la instrucción del.
#Por ejemplo, para eliminar la lista my_list, podemos hacer lo siguiente:

my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)
 
