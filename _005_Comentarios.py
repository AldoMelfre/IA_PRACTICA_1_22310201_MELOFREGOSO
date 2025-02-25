#Cuando Python se encuentra con un comentario en el programa, el comentario es completamente transparente - desde el punto de vista de Python, el comentario es solo un espacio vacío, sin importar que tan largo sea.
#En Python, un comentario es un texto que comienza con el símbolo gato y se extiende hasta el final de la línea.
# Este programa evalúa la hipotenusa c.
# a y b son las longitudes de los cátetos.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # Se emplea ** en lugar de una raíz cuadrada.
print("c =", c)

print('\n---------------------\n')

#Los comentarios pueden ser útiles en otro aspecto - se pueden utilizar para marcar un fragmento de código que actualmente no se necesita, cual sea la razón. Observa el siguiente ejemplo, sí se descomenta la línea resaltada, esto afectara la salida o resultado del código:\\

# Este es un programa de prueba.
x = 1
y = 2
# y = y + x
print(x + y)
 
# uncomment_me = 1
# uncomment_me_too = 3
# uncomment_me_also = 5

#print(uncomment_me, uncomment_me_too, uncomment_me_also, sep="\n")

#este programa calcula los segundos en cierto número de horas determinadas
# este programa fue escrito hace dos días

a = 2 # número de horas
seconds = 3600 # número de segundos en una hora

print("Horas: ", a) #imprime el numero de horas
# print("Segundos en Horas: ", a * seconds) # se imprime el numero de segundos en determinado numero de horas

#aquí también se debe de imprimir un "Adiós", pero el programador no tuvo tiempo de escribirlo
#este el es fin del programa que calcula el numero de segundos en 2 horas

# Este programa imprime
# una introducción en la pantalla.
print("¡Hola!")  #Invocando a la función print()
print("Soy Python.")

