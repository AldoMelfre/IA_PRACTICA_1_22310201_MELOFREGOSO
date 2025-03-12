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