#Los operadores bit a bit son operadores que trabajan en los bits de los números.
#Los operadores bit a bit funcionan con enteros a nivel de bits.
#Los operadores bit a bit incluyen operadores AND, OR, XOR y NOT.

#AND (&) - Conjunción
a = 5
b = 3 
resultado = a & b 
print(resultado) #1

x = False
y = True
resultado = x & y
print(resultado) #FALSE

#OR (|) - Disyunción
# Realiza una disyunción a nivel de bits.
# Cada bit del resultado es 1 si al menos uno de los bits correspondientes de los operandos es 1.
# Si ambos bits son 0, el resultado es 0.
a = 5
b = 3
resultado = a | b
print(resultado) #7

x = True
y = False
resultado = x | y
print(resultado) #TRUE 

x1 = False
y1 = False
resultado = x1 | y1
print(resultado) #FALSE

#XOR (^) - OR exclusivo
# Realiza una operación OR exclusiva a nivel de bits.
# Cada bit del resultado es 1 si solo uno de los bits correspondientes de los operandos es 1.

a = 5
b = 3
resultado = a ^ b
print(resultado) #6

x = True
y = False
resultado = x ^ y
print(resultado) #TRUE

#NOT (~) - Negación
# Realiza una negación a nivel de bits.
# Invierte todos los bits.
a = 5
resultado = ~a
print(resultado) #-6  (5 = 00000101, después de la negación, se convierte en 11111010, que es -6 en decimal *(complemento a dos)* )

#Desplazamiento a la izquierda (<<)
# Desplaza los bits a la izquierda.
# Los bits que se desplazan fuera del rango se eliminan.
a = 5
resultado = a << 1
print(resultado) #10  (5 = 00000101, después de desplazar 1 bit a la izquierda, se convierte en 00001010, que es 10 en decimal)

#Desplazamiento a la derecha (>>)
# Desplaza los bits a la derecha.
# Los bits que se desplazan fuera del rango se eliminan.
a = 1000
resultado = a >> 3
print(resultado) #125  (1000 = 1111101000, después de desplazar 3 bits a la derecha, se convierte en 0001111101, que es 125 en decimal)
