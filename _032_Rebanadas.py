#Una rebanada es un elemento de la sintaxis de Python que permite hacer una copia nueva de una lista, o partes de una lista.

list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)#salida: [1]
#En este código, creamos una lista llamada list_1 con un solo elemento, el número 1. Luego, creamos una nueva lista llamada list_2 y le asignamos una rebanada de list_1. Después, cambiamos el único elemento de list_1 a 2. Finalmente, imprimimos list_2. ¿Qué crees que se imprimirá en la consola? ¿Por qué?

# Copiando la lista completa.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)  # Salida: [8, 6]

print("\n----------------------\n")
#
# Copiando la lista completa.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

print("\n----------------------\n")

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]#se copia desde el indice 1 hasta el indice 3, pero no se incluye el indice 3
print(new_list)#salida: [8, 6]

print("\n----------------------\n")

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

#Rebanada vacia
my_list = [10, 8, 6, 4, 2] #creamos una lista
new_list = my_list[-1:1]#se copia desde el indice -1 hasta el indice 1, pero no se incluye el indice 1
print(new_list)#salida: []
#En este caso, la rebanada no contiene ningún elemento, ya que el índice de inicio es mayor que el índice de fin.
print("\n----------------------\n")

#Omitir el inicio y fin crea una copia de la lista completa.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

print("\n----------------------\n")




