#El bucle while es una estructura de control que se repite mientras una condición sea verdadera. En Python, el bucle while se ve de la siguiente manera:
#La diferencia semántica es más importante: cuando se cumple la condición, if realiza sus sentencias sólo una vez; while repite la ejecución siempre que la condición se evalúe como True.
#El bucle while se usa cuando no sabes cuántas veces se repetirá el código. Por ejemplo, si quieres que el usuario ingrese un número hasta que ingrese un número negativo, puedes usar un bucle while.

#Ejemplo
#El siguiente programa solicita al usuario que ingrese un número entero. Luego, el programa muestra el número ingresado. El programa se repite hasta que el usuario ingresa un número negativo.
#Lee un número entero del usuario
number = int(input("Ingresa un número entero: "))
#Muestra el número ingresado
print("Número ingresado:", number)
#Repite hasta que el número ingresado sea negativo
while number >= 0:
    number = int(input("Ingresa un número entero o escribe un negativo para detener: "))
    print("Número ingresado:", number)

print('\n---------------------\n')2




# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)

