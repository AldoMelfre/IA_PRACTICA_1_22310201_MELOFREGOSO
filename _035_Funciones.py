#Definamos la primera condición por la cual es una buena idea comenzar a escribir funciones propias: si un fragmento de código comienza a aparecer en más de una ocasión, considera la posibilidad de aislarlo en la forma de una función invocando la función desde el lugar en el que originalmente se encontraba.
#Las funciones son bloques de código que se pueden reutilizar en diferentes partes de un programa.
#Un buen desarrollador divide el código (o mejor dicho: el problema) en piezas aisladas, y codifica cada una de ellas en la forma de una función.
#Por ejemplo
def saludar():
    print("Hola, soy Aldo")
#En este caso, la función saludar() imprime un mensaje de saludo en la consola.
#Para llamar a la función saludar(), simplemente escribimos su nombre seguido de paréntesis:
saludar()
#Cuando se ejecuta este código, se imprime el mensaje "Hola, soy Aldo" en la consola.
print("\n----------------------\n")
#Las funciones también pueden aceptar argumentos, que son valores que se pasan a la función cuando se llama.
#Por ejemplo:
def saludar(nombre):
    print("Hola, soy " + nombre)
#En este caso, la función saludar() acepta un argumento llamado nombre y lo utiliza para imprimir un mensaje de saludo en la consola.
#Para llamar a la función saludar(), necesitamos pasar un valor al argumento nombre:
saludar("Aldo")
#Cuando se ejecuta este código, se imprime el mensaje "Hola, soy Aldo" en la consola.

print("\n----------------------\n")


#Ejercicio 1
#Escribe una función llamada maximo que tome tres números como argumentos y devuelva el mayor de ellos. Usa la función si es necesario.
#Ejemplo
print("Ingresa un valor: ")
num1 = int(input())

print("Ingresa un valor: ")
num2 = int(input())

print("Ingresa un valor: ")
num3 = int(input())

#definimos la funcion maximo
def maximo(a, b, c):
    if num1 > num2 and num1 > num3:
        return a
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
    
#llamamos a la funcion maximo
print("El numero mayor es: ", maximo(num1, num2, num3))#El numero mayor es:  5