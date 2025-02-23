#Un literal se refiere a datos cuyos valores están determinados por el literal mismo.
#Los literales son constantes que representan valores fijos.
#En Python, los literales se pueden clasificar en los siguientes tipos:
#Literales de cadena que ya conocemos

#Literales de cadena con caracter de escape \  (backslash), con esto no generamos errores al imprimir comillas dobles o simples en una cadena de texto.
print("Me gusta \"Monty Python\"")

#Apostrofe con caracter de escape
print('I\'m Aldo Melo.')


print('\n---------------------\n')

#Literales enteros

print("2")
print(2)


print('\n---------------------\n')

#Literales de punto flotante, Cuando se usan términos como dos y medio o menos cero punto cuatro, pensamos en números que la computadora considera como números punto-flotante:

#El punto decimal es lo que determina si es flotante.

print(2) #Entero
print(2.0) #Flotante

print('\n---------------------\n')

#Por ejemplo, la velocidad de la luz, expresada en metros por segundo. Escrita directamente se vería de la siguiente manera: 300000000. Para evitar escribir tantos ceros, los libros de texto emplean la forma abreviada, la cual probablemente hayas visto: 3 x 108

print(300000000) #Entero
print(3e8) #Flotante

print('\n---------------------\n')

#Booleanos, Los literales booleanos son True y False, que representan los valores verdadero y falso, respectivamente.

#Si true es mayor a false, entonces imprime True, si true es menor a false, entonces imprime False
print(True > False)
print(True < False)

#Escriba un fragmento de código de una línea, utilizando la función print(), así como los caracteres de nuevalínea y de escape, para que coincida con el resultado esperado que se muestra en la salida. 
# "Estoy"
# ""aprendiendo""
# """Python"""
print('\"Estoy\"\n\"\"aprendiendo\"\"\n\"\"\"Python\"\"\"')
 

#Existe un literal especial más utilizado en Python: el literal None. Este literal es llamado un objeto de NoneType, y puede ser utilizado para representar la ausencia de un valor. Pronto se hablará más acerca de ello.
