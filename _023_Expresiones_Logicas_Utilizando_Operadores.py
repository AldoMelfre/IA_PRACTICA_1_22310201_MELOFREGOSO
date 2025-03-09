#Podemos expresar condiciones lógicas utilizando operadores de comparación
#🔵 Conjunción ("Y")
#na conjunción es cuando juntamos dos afirmaciones con la palabra "Y".
#Por ejemplo, "Estoy cansado Y tengo hambre".
#Ambas afirmaciones deben ser verdaderas para que la conjunción sea verdadera.
#En Python, podemos usar el operador "and" para expresar una conjunción.
#Por ejemplo, la expresión "x > 5 y x < 10" es verdadera solo si x es mayor que 5 y menor que 10.
#🔵 Disyunción ("O"
#Una disyunción es cuando juntamos dos afirmaciones con la palabra "O".
#Por ejemplo, "Estoy cansado O tengo hambre".
#Solo una de las afirmaciones debe ser verdadera para que la disyunción sea verdadera.
#En Python, podemos usar el operador "or" para expresar una disyunción.
#Por ejemplo, la expresión "x < 5 o x > 10" es verdadera si x es menor que 5 o mayor que 10.
#🔵 Negación ("NO")


# Las leyes de De Morgan. Dicen que:
#La negación de una conjunción es la separación de las negaciones.
#La negación de una disyunción es la conjunción de las negaciones.
p = True
q = False
not (p and q) == (not p) or (not q) 
not (p or q) == (not p) and (not q)

#EJEMPLO CONJUCION & o AND
a = 7
b = 12
c = 5

#CONJUNCION FALSA (ALGUNO o AMBOS SON FALSOS)
resultado_conjuncion = (a < b) and (b < c)
#AQUI ESTABLECIMOS QUE A SERA MENOR A B Y B MENOR A C
print ("a es menor que b y b mayor que c?",resultado_conjuncion) #FALSE
#CONJUNCION VERDADERA (AMBOS SON VERDADEROS)
resultado_conjuncion = (a < b) and (b > c)
print("a es menor que b y b es mayor que c?", resultado_conjuncion)

print("\n----------------------\n")

#EJEMPLO DISYUNCION | o OR
a = 7
b = 12
c = 5

#DISYUNCION FALSA (AMBOS SON FALSOS)
resultado_disyuncion = (a < b) or (b < c)
#AQUI ESTABLE
print("a es menor que b o b es menor que c?", resultado_disyuncion) #TRUE
#DISYUNCION VERDADERA (ALGUNO O AMBOS SON VERDADEROS)
resultado_disyuncion = (a < b) or (b > c)
print("a es menor que b o b es mayor que c?", resultado_disyuncion) #TRUE