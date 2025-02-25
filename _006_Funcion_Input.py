#La funcion input() nos permite recibir datos del usuario
#La función input() siempre devuelve una cadena
#La función input() toma un argumento, que es el mensaje que se mostrará en la pantalla
#La función input() espera a que el usuario escriba algo y presione la tecla Enter
#La función input() puede ser utilizada para recibir números, pero estos son tratados como cadenas
print("Dime tu nombre...")
name = input()
print("Hola...", name, "... mucho gusto en conocerte.")
print("¿Cuántos años tienes?")
age = input()
print("Tienes...", age, "... años.")

print('\n---------------------\n')

name2 = input("Dime tu nombre...")
print("Hola...", name2, "... mucho gusto en conocerte.")
age2 = input("¿Cuántos años tienes?")
print("Tienes...", age2, "... años.")

print('\n---------------------\n')

#No se puede realizar operaciones matemáticas con variables que contienen cadenas
anything = input("Ingresa un número:")
something = anything ** 2.0
print(anything, "al cuadrado es", something)

print('\n---------------------\n')

#ERRORES

anything = input("Ingresa un número: ")
something = anything ** 2.0
print(anything, "al cuadrado es", something)


#La última línea lo explica todo, se intentó aplicar el operador ** a 'str' (una cadena) acompañado por un 'float'.
#Esto está prohibido.
#Esto debe de ser obvio. ¿Puedes predecir el valor de "ser o no ser" elevado a la potencia 2?
#No podemos. Python tampoco puede.

print('\n---------------------\n')

#Python ofrece dos simples funciones para especificar un tipo de dato y resolver este problema, aquí están: int() y float().

anything = input("Ingresa un número: ")
something = float(anything) ** 2.0
print(anything, "al cuadrado es", something)

print('\n---------------------\n')

#La función float() convierte su argumento en un número de punto flotante, si es posible.
#Si no es posible, la función generará un error.
#En este caso, el programa espera que el usuario ingrese un número, y si lo hace, el programa calcula el cuadrado del número.
#Si el usuario no ingresa un número, el programa generará un error.

#La función int() convierte su argumento en un número entero, si es posible.
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)

#Toma en cuenta que en el programa que puede ver en el editor, la variable hypo se usa con un solo propósito - guardar el valor calculado entre la ejecución de la línea de código contigua.
#Debido a que la función print() acepta una expresión como argumento, se puede quitar la variable del código.

leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es:", (leg_a**2 + leg_b**2) ** .5)
