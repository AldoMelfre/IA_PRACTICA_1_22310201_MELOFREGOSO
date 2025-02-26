#Los operadores de condiciones son usados para comparar valores. El resultado de la comparación es un valor booleano, es decir, True o False.
#If (si) es una condición que se ejecuta o no, dependiendo del valor de la expresión booleana.
#El bloque de código que sigue a la condición es ejecutado si la condición es True.
#if el_clima_es_bueno:
 #   salir_a_caminar()
#almorzar()
contador_de_ovejas = int(input("¿Cuántas ovejas has visto? ")) 
if contador_de_ovejas >= 120: # Evaluar una expresión condicional 
    print('hora de dormir')# Ejecutar si la expresión condicional es verdadera0

print('\n---------------------\n')

if sheep_counter >= 120:
    make_a_bed()
    take_a_shower()
    sleep_and_dream()
feed_the_sheepdogs()

#if-else
#El bloque de código que sigue a la palabra clave else es ejecutado si la condición es False.
#Si el clima es bueno, sal a caminar, de lo contrario, ve a ver una película.

if el_clima_es_bueno:
    salir_a_caminar()
else:
    ver_una_pelicula()

print('\n---------------------\n')

#else-if  anidadas 
#La palabra clave elif es una abreviatura de else if.
#El bloque de código que sigue a la palabra clave elif es ejecutado si la condición es True.

if el_clima_es_bueno:
    salir_a_caminar()
elif el_clima_es_malo:
    ver_una_pelicula()
else:
    leer_un_libro()

print('\n---------------------\n')

# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)

print('\n---------------------\n')


#Ahora vamos a mostrarte un hecho intrigante. Python tiene una característica interesante - mira el código a continuación:

# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2: larger_number = number1
else: larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)

#Nota: si alguna de las ramas de if-elif-else contiene una sola instrucción, puedes codificarla de forma más completa (no es necesario que aparezca una línea con sangría después de la palabra clave), pero solo continúa la línea después de los dos puntos).


# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1

# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
    largest_number = number2

# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
    largest_number = number3

# Imprime el resultado.
print("El número más grande es:", largest_number)


