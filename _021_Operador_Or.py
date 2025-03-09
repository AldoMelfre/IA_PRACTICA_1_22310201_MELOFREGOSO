#EL operador OR se utiliza para evaluar dos condiciones, si alguna de las dos condiciones es verdadera, entonces la condición completa es verdadera.
# | (barra vertical) ‒ disyunción a nivel de bits; si alguno de los bits es 1, el resultado es 1; de lo contrario, es 0.

#Ejemplo de uso de OR
x = 5
y = 10
z =5

print(x==z or z==y) #TRUE

print (x==y or y==z) #FALSE

print("\n----------------------\n")

#COMPROBAR SI DOS RESULTADOS SON IGUALES
a = 5
b= 10

op = (a<b) or (b==a)
print(op) #TRUE

op = (a==b) or (b<a) 
print(op) #FALSE

#Ejemplo de uso de OR
