#Python ofrece dos operadores muy poderosos, capaces de revisar la lista para verificar si un valor específico está almacenado dentro de la lista o no.
#Estos operadores son in y not in.
#El primero de ellos, in, devuelve True si el valor especificado está presente en la lista, y False en caso contrario.
#El segundo, not in, hace lo contrario: devuelve True si el valor especificado no está presente en la lista, y False en caso contrario.
#Aquí tienes un ejemplo:
# 

lista = [1, 2, 3, 4, 5]
print(3 in lista) #True
print(6 in lista) #False
print(3 not in lista) #False

#El operador in también se puede usar con cadenas de texto.
#Por ejemplo:
print("\n----------------------\n")
cadena = "Hola, mundo!"
print("!" in cadena) #True
print("z" in cadena) #False
print("H" in cadena) #True

