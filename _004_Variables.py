#Las variables son contenedores de datos, en python no es necesario declarar el tipo de dato que se almacenará en la variable, ya que python es un lenguaje de tipado dinámico.
#Para asignar un valor a una variable se utiliza el operador de asignación =, el cual asigna el valor de la derecha a la variable de la izquierda.

pi = 3.14159
print(pi)

print('\n---------------------\n')

#Las variables son sensibles a mayúsculas y minúsculas.
variable = 5
VariaBle = 10
print(variable)
print(VariaBle)

#Las variables pueden ser reasignadas en cualquier momento.
variable = 10
print(variable)
variable = "Hola"
print(variable)
print('\n---------------------\n')

numero = 100
numero = 200 + 300
print(numero)
 

print('\n---------------------\n')
#Las variables pueden contener letras, números y guiones bajos.

variable_1 = 5

print(variable_1)

print('\n---------------------\n')


#Palabras reservadas en Python
#Las palabras reservadas son palabras que tienen un significado especial en Python, no pueden ser utilizadas como nombres de variables, funciones o clases.
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print('\n---------------------\n')

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

print('\n---------------------\n')

#Se puede utilizar print() para combinar texto con variables utilizando el operador + para mostrar cadenas con variables, por ejemplo:
var = "3.8.5"
print("Python version: " + var)

print('\n---------------------\n')  

#Operaciones con variables
#Se pueden realizar operaciones matemáticas con variables, por ejemplo:
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

print('\n---------------------\n')

#Érase una vez en la Tierra de las Manzanas, Juan tenía tres manzanas, María tenía cinco manzanas, y Adán tenía seis manzanas. Todos eran muy felices y vivieron por muchísimo tiempo. Fin de la Historia. 
john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=',')

total_apples = john + mary + adam
print(total_apples)

# peter = 12.5
# suzy = 2
# print(peter / suzy)
# print("Total number of apples:", total_apples)

print('\n---------------------\n')

#Operadores Abrevidados 
#Se pueden utilizar operadores abreviados para realizar operaciones con variables y asignar el resultado a la misma variable, por ejemplo:
x = 10
x += 3
print(x)
 
print('\n---------------------\n')

#Es tiempo de explicar el siguiente conjunto de operadores que harán la vida del programador/desarrollador más fácil. Muy seguido, se desea utilizar la misma variable al lado derecho y al lado izquierdo del operador = operator.

#Variables: un convertidor simple
#Escriba un programa que convierta millas a kilómetros y viceversa. Si no está seguro sobre los factores de conversión, use los siguientes: 1 milla = 1.61 kilómetros.

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
