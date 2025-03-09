#El and es un operador logico el cual devuelve 1 o true si ambos operandos son verdaderos, y en los demas casos devuelve false.
#& (ampersand) ‒ conjunción a nivel de bits; si ambos bits son 1, el resultado es 1; de lo contrario, es 0.

#Ejemplo de uso de and
x = 10
y = 12
z = 10
print(x==z and z==y) #FALSE

x=1
y=1
z=2
print(x+y==z and y+x==z) #TRUE

print("/n----------------------/n")

#COMPROBAR SI DOS RESULTADOS SON IGUALES
a = 5
b= 10
c=15

operacion = (a<b) and (b<c)
if operacion == True:
	resultado = "Verdadero"
else: 
	resultado = "Falso"
print("a es menor que b y b es menor que c?", resultado)

operacion = (a>b) and (b>c)
if operacion == True:
	resultado = "Verdadero"
else: 
	resultado = "Falso"
print("a es mayor que b y b es mayor que c?", resultado)