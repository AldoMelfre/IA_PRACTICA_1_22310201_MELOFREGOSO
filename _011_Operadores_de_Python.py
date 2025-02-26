#El operador de igualdad (==) compara los valores de dos objetos. El resultado es True si los valores son iguales, y False si no lo son.
#Recordemos que = es un operador de asignación, no de comparación.
a=5
b=a  

print(b) #resulta 5

print('\n---------------------\n')

#sin embargo si usamos == para comparar
a=5
b=2
a==b
print(b) #resulta False

print('\n---------------------\n')
#Esta pregunta no es tan fácil como la primera. Afortunadamente, Python puede convertir el valor entero en su equivalente real y, en consecuencia, la respuesta es True.
a=2
b=2.
a==b
print(b) #resulta True

print('\n---------------------\n')

#El operador de desigualdad (!=) es un poco más complicado. Compara los valores de dos objetos. El resultado es True si los valores son diferentes, y False si no lo son.
a=5
b=3
a!=b
print(b) #resulta True

print('\n---------------------\n')

var = 0  # Asignando 0 a var
print(var != 0)
 
var = 1  # Asignando 1 a var
print(var != 0)

print('\n---------------------\n')

#operadores de comparación
# > - mayor que
black_sheep > white_sheep  # Mayor que
# < - menor que
black_sheep < white_sheep  # Menor que

# >= - mayor o igual que
black_sheep >= white_sheep  # Mayor o igual que
# <= - menor o igual que
black_sheep <= white_sheep  # Menor o igual que

