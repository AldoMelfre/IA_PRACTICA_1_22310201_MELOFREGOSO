#El ordenamiento burbuja es un algoritmo sencillo de ordenamiento. Funciona revisando cada elemento de la lista que va a ser ordenada con el siguiente, intercambiándolos de posición si están en el orden equivocado. Es necesario revisar varias veces toda la lista hasta que no se necesiten más intercambios, lo cual significa que la lista está ordenada. El nombre de este algoritmo proviene de la forma en que suben por la lista los elementos durante los intercambios, como si fueran pequeñas "burbujas".
#El ordenamiento burbuja es uno de los algoritmos de ordenamiento más simples y menos eficientes. A pesar de esto, es útil para enseñar a los principiantes los conceptos básicos de los algoritmos de ordenamiento.

#ejemplo
numeros = [5, 2, 9, 1, 5, 6]
print("Los numeros originales son", numeros)
#definimos la funcion burbuja
def burbuja(numeros):
    n=len(numeros) #Definimos la longitud de la lista 
    for i in range(n): #creamos un ciclo for que recorra la lista el numero caracteres, lo que obtuve anteriormente con n=len(numeros)
        for i in range(0, n-i-1): #creamos otro ciclo for que recorra la lista de 0 a n-i-1
            if numeros[i] > numeros[i+1]:#si el numero en la posicion i es mayor al numero en la posicion i+1
                numeros[i], numeros[i+1] = numeros[i+1], numeros[i]#intercambiamos los numeros
    return numeros#retornamos la lista ordenada
#llamamos a la funcion burbuja
burbuja(numeros)
#imprimimos la lista ordenada
print("Los numeros ordenados son", numeros)

        
