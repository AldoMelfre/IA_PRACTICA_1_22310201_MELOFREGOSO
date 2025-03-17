#¿Cuántos pases necesitamos para ordenar la lista completa?
#La respuesta es n-1, donde n es el número de elementos en la lista.
#¿Por qué?
#En cada pase, el algoritmo coloca el elemento más grande en su posición correcta.
#Después del primer pase, el elemento más grande estará en la última posición.
#Después del segundo pase, el segundo elemento más grande estará en la penúltima posición.
#Y así sucesivamente.
#Después de n-1 pases, todos los elementos estarán en su posición correcta.
#Por lo tanto, necesitamos n-1 pases para ordenar la lista completa.

#Creamos una variable llamada swapped, y le asignamos un valor de False para indicar que no hay intercambios. De lo contrario, se le asignará True.

#VERSION INTERACTIVA
calificaciones = []
swapped = True
num = int(input("¿Cuántos alumnos tienes?: "))

for i in range(num):
    val = float(input(f"Ingresa la calificacion del alumno #{i + 1}: "))
    calificaciones.append(val)

while swapped:
    swapped = False
    for i in range(len(calificaciones) - 1):
        if calificaciones[i] > calificaciones[i + 1]:
            swapped = True
            calificaciones[i], calificaciones[i + 1] = calificaciones[i + 1], calificaciones[i]

print("\Las calificaciones:")
print(calificaciones)



#Python, sin embargo, tiene sus propios mecanismos de clasificación. Nadie necesita escribir sus propias clases, ya que hay un número suficiente de herramientas listas-para-usar.
lista = [8, 10, 6, 2, 4]
lista.sort()
print(lista)

