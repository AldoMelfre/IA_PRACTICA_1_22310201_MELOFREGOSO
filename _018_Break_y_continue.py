# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")
#En este caso, el bucle for se ejecutará cinco veces. La primera vez, i será 1, la segunda vez, i será 2 y la tercera vez, i será 3. En este punto, la condición if se evaluará como True y la instrucción break se ejecutará. El programa saldrá del bucle y continuará con la siguiente instrucción después del bucle.

# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")
#En este caso, el bucle for se ejecutará cinco veces. La primera vez, i será 1, la segunda vez, i será 2 y la tercera vez, i será 3. En este punto, la condición if se evaluará como True y la instrucción continue se ejecutará. El programa omitirá la impresión de "Dentro del bucle." y continuará con la siguiente iteración del bucle.

print('\n---------------------\n')
#El programa solicita al usuario que ingrese un número. Si el número es mayor que el número más grande actual, se actualiza el número más grande. El programa se repite hasta que el usuario ingresa -1. En ese momento, el programa imprime el número más grande y termina.
largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

print('\n---------------------\n')

#El programa solicita al usuario que ingrese un número. Si el número es mayor que el número más grande actual, se actualiza el número más grande. El programa se repite hasta que el usuario ingresa -1. En ese momento, el programa imprime el número más grande y termina.

largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

print('\n---------------------\n')  