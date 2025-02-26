#STR: Este tipo de conversión no es en un solo sentido. También se puede convertir un numero a una cadena, lo cual es más fácil y seguro - esta operación es posible hacerla siempre.

leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))

#La función str() convierte su argumento en una cadena.
#La función str() es muy útil cuando se necesita imprimir un número junto con un mensaje.

print('\n---------------------\n')

