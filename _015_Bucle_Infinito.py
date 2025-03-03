#Un bucle infinito, también denominado bucle sin fin, es una secuencia de instrucciones en un programa que se repite indefinidamente (bucle sin fin).

#Ejemplo
while True:
    print("Estoy atrapado dentro de un bucle.")
 
#En el ejemplo anterior, el bucle while se repite indefinidamente porque la condición siempre es True. El programa imprime el mensaje "Estoy atrapado dentro de un bucle." una y otra vez. El programa no se detendrá hasta que se interrumpa manualmente.

print('\n---------------------\n')

#El programa solicita al usuario que ingrese un número. Si el número es mayor que el número más grande actual, se actualiza el número más grande. El programa se repite hasta que el usuario ingresa -1. En ese momento, el programa imprime el número más grande y termina.

# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", largest_number)

