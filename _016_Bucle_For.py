#EL bucle for es una estructura de control que se repite un número específico de veces.
#Imagina que el cuerpo de un bucle debe ejecutarse exactamente cien veces. Si deseas utilizar el bucle while para hacerlo, puede tener este aspecto:
i = 0
while i < 100:
    # do_something()
    i += 1

#Ahora imagina que deseas hacer lo mismo con un bucle for. El código se vería así:
for i in range(100):
    print('El numero es ',i)
#El valor de la última variable de control es 99 (no 100, ya que comienza desde 0 , no desde 1)

print('\n---------------------\n')

for i in range(2, 8, 3):
    print("El valor de i es", i)
#En este caso, el bucle for se ejecutará tres veces. La primera vez, i será 2, la segunda vez, i será 5 y la tercera vez, i será 8. El valor final de i no se incluye en el rango.
print('\n---------------------\n')

#La variable expo se utiliza como una variable de control para el bucle e indica el valor actual del exponente. La propia exponenciación se sustituye multiplicando por dos
power = 1
for expo in range(1000):
    print("2 a la potencia de", expo, "es", power)
    power *= 2
#En este caso, el bucle for se ejecutará 16 veces. La primera vez, expo será 0, la segunda vez, expo será 1 y así sucesivamente hasta que expo sea 15. El valor final de expo es 15, no 16.

print('\n---------------------\n')

