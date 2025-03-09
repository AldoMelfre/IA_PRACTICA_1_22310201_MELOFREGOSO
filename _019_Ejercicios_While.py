#Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.
#Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.

# Solicitar la cantidad de bloques
bloques = int(input("Ingresa la cantidad de bloques: "))
5
altura = 0
bloques_necesarios = 1

# Construcción de la pirámide
while bloques >= bloques_necesarios:
    bloques -= bloques_necesarios
    altura += 1
    bloques_necesarios += 1  # La siguiente capa necesita un bloque más

# Imprimir la altura alcanzada
print("La altura de la pirámide es:", altura)

#toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0; si es par, evalúa un nuevo c0 como c0 ÷ 2; de lo contrario, si es impar, evalúe un nuevo c0 como 3 × c0 + 1; si c0 ≠ 1, salta al punto 2. La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.

c0 = int(input("Ingrese un entero positivo:"))

if c0 <= 0:
    print("El número debe ser positivo")
else:
    pasos = 0

    while c0 != 1:
        print(c0)
        if c0 % 2 == 0:
            c0 = c0 //2
        else:
            c0 = 3*c0+1
        pasos +=1
print(c0)
print("Pasos = ",pasos)

