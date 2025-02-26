x = float(input("Ingresa el valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

#El programa calcula el valor de la expresión matemática y = 1/(x + 1/(x + 1/(x + 1/x)))
#El programa solicita al usuario que ingrese un valor para x.

print('\n---------------------\n')
#El siguiente programa calcula el área de un círculo. Solicita al usuario que ingrese el valor del radio y luego muestra el resultado.
#El valor de PI se asume como 3.1416.
r = float(input("Ingresa el valor del radio: "))
area = 3.1416 * (r ** 2)
print("El área del círculo es:", area)

print('\n---------------------\n')

#El siguiente programa calcula la duración de un evento en horas y minutos.
#Solicita al usuario que ingrese la hora de inicio, los minutos de inicio y la duración del evento en minutos.
#El programa muestra la hora de finalización del evento.
#El programa no tiene en cuenta la duración del evento en horas.
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
mins = mins + dura # encuentra el número total de minutos, la suma de la duracion y minutos es el total de minutos
hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas Como la suma de minutos puede superar los 60, calculamos cuántas horas completas se han formado dividiendo mins entre 60 (división entera //).
mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
print(hour, ":", mins, sep='')

