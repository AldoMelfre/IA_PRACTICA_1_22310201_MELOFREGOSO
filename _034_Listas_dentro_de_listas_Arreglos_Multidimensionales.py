# #Las listas dentro de listas son una forma de almacenar datos más complejos. Por ejemplo, si tienes una lista de estudiantes, cada estudiante puede tener su propia lista de calificaciones.
# #Aquí hay un ejemplo:
# #
estudiantes = [ ["Juan", 8], ["Maria", 9], ["Luis", 7] ]
print(estudiantes)
# #En este ejemplo, la lista estudiantes contiene tres elementos, cada uno de los cuales es una lista que contiene dos elementos: el nombre del estudiante y su calificación.
#
# #Para acceder a los elementos de la lista estudiantes, primero necesitas acceder a la lista que contiene los datos del estudiante y luego acceder a los elementos individuales de esa lista.
# #Por ejemplo, para acceder a la calificación de Maria, puedes hacer lo siguiente:
print(estudiantes[1][1]) #9
# #En este ejemplo, estudiantes[1] accede a la lista que contiene los datos de Maria, y estudiantes[1][1] accede a la calificación de Maria.

# #También puedes modificar los elementos de una lista dentro de una lista.
# #Por ejemplo, para cambiar la calificación de Luis a 8, puedes hacer lo siguiente:
estudiantes[2][1] = 8
print(estudiantes[2][1]) #8

# #Ahora un ejemplo más complejo:
# #suponemos una agencia de viajes que ofrece paquetes de viaje a diferentes destinos.
# #Cada paquete de viaje tiene un nombre, una lista de destinos y un precio.
# #Aquí hay un ejemplo:
paquetes = [
    ["Paquete 1", ["Paris", "Londres"], 1000],
    ["Paquete 2", ["Tokio", "Osaka"], 1500],
    ["Paquete 3", ["Nueva York", "Los Angeles"], 1200]
]
print(paquetes)
# #En este ejemplo, la lista paquetes contiene tres elementos, cada uno de los cuales es una lista que contiene tres elementos: el nombre del paquete, la lista de destinos y el precio del paquete.

# #Si queremos hacerla interactiva podemos agregar menus input() y un ciclo while
# #Por ejemplo:
paquetes = [
    ["Paquete 1", ["Paris", "Londres"], 1000],
    ["Paquete 2", ["Tokio", "Osaka"], 1500],
    ["Paquete 3", ["Nueva York", "Los Angeles"], 1200]
]
print(paquetes)
while True:
    print("\n1. Mostrar paquetes")
    print("2. Agregar paquete")
    print("3. Salir")
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        print(paquetes)
    elif opcion == 2:
        nombre = input("Ingresa el nombre del paquete: ")
        destinos = input("Ingresa los destinos separados por comas: ").split(",")
        precio = int(input("Ingresa el precio del paquete: "))
        paquetes.append([nombre, destinos, precio])
    elif opcion == 3:
        break
    else:
        print("Opción inválida")

#Ademas si queremos hacer un menu para ingresar datos de viajes y almacenarlos en una lista, podemos hacer lo siguiente:
paquetes = []
while True:
    print("\n1. Mostrar paquetes")
    print("2. Agregar paquete")
    print("3. Salir")
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        print(paquetes)
    elif opcion == 2:
        nombre = input("Ingresa el nombre del paquete: ")
        destinos = input("Ingresa los destinos separados por comas: ").split(",") #La funcion split() divide una cadena en una lista. Puedes especificar el separador, el separador predeterminado es cualquier espacio en blanco.
        precio = int(input("Ingresa el precio del paquete: "))
        paquetes.append([nombre, destinos, precio])
    elif opcion == 3:
        break
    else:
        print("Opción inválida")

print("\n----------------------\n")

#Imagina un hotel con tres torres, cada una con 15 pisos y 20 habitaciones por piso.
#Podemos representar esto con una lista de tres elementos, cada uno de los cuales es una lista de 15 elementos, cada uno de los cuales es una lista de 20 elementos.
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
print(rooms)



