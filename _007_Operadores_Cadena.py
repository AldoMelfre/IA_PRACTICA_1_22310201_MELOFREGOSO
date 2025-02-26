#Operadores cadena Simplemente concatena (junta) dos cadenas en una. Por supuesto, puede ser utilizado más de una vez en una misma expresión, y en tal contexto se comporta con enlazado del lado izquierdo.
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")

#el usar + para concatenar cadenas te permite construir la salida de una manera más precisa que con una función print() pura, incluso si está enriquecida con end= y sep= argumentos de palabras clave.

print('\n---------------------\n')

#El signo de * (asterisco), cuando es aplicado a una cadena y a un número (o a un número y cadena) se convierte en un operador de replicación:

"Aldo" * 3  #resulta AldoAldoAldo
3 * "Aldo"  #resulta AldoAldoAldo
'5' * 2     #resulta 55

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


print('\n---------------------\n')
