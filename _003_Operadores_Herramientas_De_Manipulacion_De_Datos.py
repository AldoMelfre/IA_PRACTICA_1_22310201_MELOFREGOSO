#Los operadores son símbolos que realizan operaciones en uno o más operandos. Los operandos son los valores en los que se realizan las operaciones. Los operadores se pueden clasificar en los siguientes tipos:
#Suma: +
print(-4 + 4)
print(-4. + 8)

print('\n---------------------\n')

#Resta: -

print(-4 - 4)
print(4. - 8)
print(-1.1)

print('\n---------------------\n')

#Multiplicación: *
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

print('\n---------------------\n')

#División: / SIEMPRE GENERA FLOTANTES

print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

print('\n---------------------\n')

#División entera: // AYUDA A QUE OBTENGAMOS UN ENTERO COMO RESULTADO
#los resultados siempre son redondeados hacia abajo

print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print('\n---------------------\n')

#Módulo: %
#El operador módulo devuelve el resto de la división de dos números.

print(12 % 4.5)

print('\n---------------------\n')

#Exponeciacion
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#Jerarquia de operadores
#1. ()
#2. **
#3. *, /, //, %
#4. +, -

print('\n---------------------\n')

#Ejemplo de jerarquia de operadores; La mayoría de los operadores de Python tienen un enlazado hacia la izquierda, lo que significa que el cálculo de la expresión es realizado de izquierda a derecha.

print(9 % 6 % 2)
