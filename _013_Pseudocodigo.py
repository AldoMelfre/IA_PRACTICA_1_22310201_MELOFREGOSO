#Pseudocodigo y bucles
#Un algoritmo es un conjunto de reglas y procedimientos para resolver un problema. Los algoritmos pueden ser expresados en lenguaje natural, pseudocódigo o en un lenguaje de programación.
#El pseudocódigo es un lenguaje de programación informal que no requiere una sintaxis específica y es utilizado para describir los pasos de un algoritmo.   
#El pseudocódigo es una forma de escribir un algoritmo que se asemeja a un lenguaje de programación, pero no sigue las reglas de un lenguaje de programación específico.

#Ejemplo de pseudocódigo:
largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Ir a la línea 02

#En el ejemplo anterior, el pseudocódigo describe un algoritmo que encuentra el número más grande en una secuencia de números. El algoritmo lee un número, verifica si es el número más grande y luego repite el proceso hasta que se ingresa -1. En ese momento, el algoritmo imprime el número más grande y termina.

print('\n---------------------\n')

#Python a menudo viene con muchas funciones integradas que harán el trabajo por ti. Por ejemplo, para encontrar el número más grande de todos, puede usar una función incorporada de Python llamada max(). Puedes usarlo con múltiples argumentos. Analiza el código de abajo:

# Se leen tres números.
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number.

largest_number = max(number1, number2, number3)

# Imprime el resultado.
print("El número más grande es:", largest_number)

#En el código anterior, la función max() toma tres argumentos y devuelve el número más grande de todos. Luego, el número más grande se imprime en la pantalla.
#De la misma manera, puedes usar la función min() para devolver el número más pequeño de todos los argumentos.

print('\n---------------------\n')

#Ejercicio 1
#Escribe un programa que lea un número entero del usuario. Luego, tu programa debe mostrar un mensaje que indique si el número es par o impar.
#Solución
#Lee un número entero del usuario
number = int(input("Ingresa un número entero: "))
#Determina si el número es par o impar
if number % 2 == 0:
    print(number, "es un número par.")
else:
    print(number, "es un número impar.")

print('\n---------------------\n')

#Ejercicio 2
#Escribe un programa que lea un número entero del usuario. Luego, tu programa debe mostrar un mensaje que indique si el número es positivo, negativo o cero.
#Solución
#Lee un número entero del usuario
number = int(input("Ingresa un número entero: "))
#Determina si el número es positivo, negativo o cero
if number > 0:
    print(number, "es un número positivo.")
elif number < 0:
    print(number, "es un número negativo.")
else:
    print(number, "es cero.")

print('\n---------------------\n')

#El pseudo-codigo en este caso es:
#Lee un número entero del usuario
#Determina si el número es positivo, negativo o cero
#Imprime el
#resultado
#El código anterior lee un número entero del usuario y luego determina si el número es positivo, negativo o cero. Finalmente, el programa imprime un mensaje que indica el resultado.
