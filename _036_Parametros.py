#Se puede pasar información a las funciones utilizando parámetros. Las funciones pueden tener tantos parámetros como sean necesarios.
def hi(name):
    print("Hola,", name)

hi("Greg")

#Otro ejemplo de una funcion con mas parametros 
def hi_all(name_1, name_2):
    print("Hola,", name_2)
    print("Hola,", name_1)

hi_all("Sebastián", "Konrad")
#
#Una funcion de 3 parametros 
def address(street, city, postal_code):
    print("Tu dirección es:", street,"St.,", city, postal_code)

s = input("Calle: ")
p_c = input("Código Postal: ")
c = input("Ciudad: ")
address(s, c, p_c)

#Ejercicio 2
#Escribe una función llamada suma que tome dos números como argumentos y devuelva su suma. Usa la función si es necesario.

def suma(a,b):
    return a+b

print("Ingresa el sumando: ")
num1 = int(input())
print("Ingresa el sumando: ")
num2 = int(input())
print("La suma da: ", suma(num1,num2))



#Peso de los argumentos
#Cuando se llama a una función, los valores que se pasan a la función se denominan argumentos.
#Los argumentos se pueden pasar a las
#funciones de dos maneras:
#1. Por posición
#2. Por nombre
#Cuando se pasan argumentos por posición, el orden en el que se pasan los argumentos es importante.
#Cuando se pasan argumentos por nombre, el orden en el que se pasan los argumentos no importa.
#Por ejemplo
#
Ejemplo 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # salida: 3
subtra(2, 5)    # salida: -3

#En este ejemplo, la función subtra() acepta dos argumentos, a y b, y luego imprime la resta de a y b en la consola.
#Cuando se llama a la función subtra() con los argumentos 5 y 2, la función imprime 3 en la consola.
#Cuando se llama a la función subtra() con los argumentos 2 y 5, la función imprime -3 en la consola.
#En el primer caso, 5 se asigna a a y 2 se asigna a b.
#En el segundo caso, 2 se asigna a a y 5 se asigna a b.
#En ambos casos, la función imprime la resta de a y b en la consola.

#En este siguiente ejemplo 2 se pasan los argumentos por nombre
Ejemplo 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # salida: 3
subtra(b=2, a=5)    # salida: 3

Ex. 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # salida: 3
subtra(5, 2)    # salida: 3

#En este ejemplo, la función subtra() acepta dos argumentos, a y b, y luego imprime la resta de a y b en la consola.
#Cuando se llama a la función subtra() con los argumentos 5 y b=2, la función imprime 3 en la consola.
#Cuando se llama a la función subtra() con los argumentos 5 y 2, la función imprime 3 en la consola.


 print("\n----------------------\n")
#Es importante recordar que primero se especifican los argumentos posicionales y después los de palabras clave. Es por esa razón que si se intenta ejecutar el siguiente código:
def subtra(x, y):
    print(x - y)

subtra(5, y=2)    # salida: 3
subtra(x=5, 2)    # Syntax Error este error sucede porque se intenta pasar un argumento posicional después de un argumento de palabra clave.


print("\n----------------------\n")


#En este ejemplo, la función name() acepta dos argumentos, first_name y last_name, y luego imprime el nombre completo en la consola.
#El argumento last_name tiene un valor predeterminado de "Pérez".
#Cuando se llama a la función name() con el argumento first_name "Andy", la función imprime "Andy Pérez" en la consola.
#Cuando se llama a la función name() con los argumentos first_name "Bety" y last_name "Rodríguez", la función imprime "Bety Rodríguez" en la consola.
#En este caso, el argumento de palabra clave last_name es reemplazado por "Rodríguez".
def name(first_name, last_name="Pérez"):
    print(first_name, last_name)

name("Andy")    # salida: Andy Pérez
name("Bety", "Rodríguez")    # salida: Bety Rodríguez (el argumento de palabra clave es reemplazado por "Rodríguez")








