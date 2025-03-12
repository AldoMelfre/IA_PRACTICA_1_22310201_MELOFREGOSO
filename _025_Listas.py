#Las listas son una estructura de datos que nos permite almacenar varios valores en una sola variable.
#Podemos acceder a estos valores utilizando un índice.
#Las listas en Python se definen utilizando corchetes [].
#Por ejemplo, aquí hay una lista de números:
numbers = [1, 2, 3, 4, 5]
#Podemos acceder a un elemento de la lista utilizando un índice.
# Los índices en Python comienzan en 0.
# Por ejemplo, para acceder al primer elemento de la lista, usamos el índice 0:
print(numbers[0]) #1
#Para acceder al segundo elemento de la lista, usamos el índice 1:
print(numbers[1]) #2 
#Y asi consecutivamente.
print("\n----------------------\n")
#También podemos modificar los elementos de una lista utilizando un índice. A esto se le llama INDEXACION.
#Por ejemplo, para cambiar el segundo elemento de la lista, hacemos lo siguiente:
numbers[1] = 10 #Cambiamos el valor 2 por 10
print(numbers) #[1, 10, 3, 4, 5]

print("\n----------------------\n")
#Tambien si queremos copiar una lista a otra, podemos hacerlo de la siguiente manera:
bebidas=["Coca Cola", "Pepsi", "Sprite"]
bebidas[0] = bebidas[2] #Cambiamos el valor de la primera posicion por el valor de la tercera posicion
print(bebidas[0]) 

print("\n----------------------\n")
#Si queremos ver toda la lista simplemente escribimos el nombre de la lista:
print(bebidas) #['Sprite', 'Pepsi', 'Sprite']


print("\n----------------------\n")

#ELIMINAR LISTAS 
#Para eliminar un elemento de una lista, podemos usar la palabra clave del seguida del nombre de la lista y el índice del elemento que queremos eliminar
numbers = [1, 2, 3, 4, 5]
del numbers[1]
print(len(numbers))
print(numbers)

print("\n----------------------\n")

#Indices negativos
#También podemos acceder a los elementos de una lista utilizando índices negativos.
#Los índices negativos cuentan desde el final de la lista.
#Por ejemplo, para acceder al último elemento de la lista, podemos usar el índice -1:
numbers = [1, 2, 3, 4, 5]
print(numbers[-1]) #5
#Para acceder al penúltimo elemento de la lista, usamos el índice -2:
print(numbers[-2]) #4
#Y asi consecutivamente.
print("\n----------------------\n")

#Append 
#Para agregar un elemento a una lista, podemos usar el método append().
#Este método agrega un elemento al final de la lista.
#Por ejemplo, aquí hay una lista de números:
numbers = [1, 2, 3, 4, 5]
#Para agregar el número 6 al final de la lista, podemos hacer lo siguiente:
numbers = numbers.append(6)
print(numbers) #[1, 2, 3, 4, 5, 6]
print("\n----------------------\n")
#insert
#Para insertar un elemento en una posición específica de una lista, podemos usar el método insert().
#Este método toma dos argumentos: el índice donde queremos insertar el elemento y el elemento que queremos insertar.
#Por ejemplo, aquí hay una lista de números:
numbers = [1, 2, 3, 4, 5]
#Para insertar el número 6 en la segunda posición de la lista, podemos hacer lo siguiente:
numbers.insert(1, 6)
print(numbers) #[1, 6, 2, 3, 4, 5]

#ahora con nombres
nombre = ["aldo", "jose", "juan", "pedro"]
print("Los nombres originales son", nombre)
nombre.insert(1, "matilda")
print("Los nombres con el nuevo nombre son", nombre)

print("\n----------------------\n")

#Puedes iniciar la vida de una lista creándola vacía (esto se hace con un par de corchetes vacíos) y luego agregar nuevos elementos según sea necesario.

my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)  # Salida: [1, 2, 3, 4, 5]
#el ciclo for agrega los numeros del 1 al 5 a la lista my_list como tiene rango de 5, el ciclo for se ejecuta 5 veces.

#ahora si utilizamos insert 
my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)  # Salida: [5, 4, 3, 2, 1]
#En este caso, el ciclo for agrega los numeros del 1 al 5 a la lista my_list pero con el metodo insert, por lo que se agrega al inicio de la lista.
