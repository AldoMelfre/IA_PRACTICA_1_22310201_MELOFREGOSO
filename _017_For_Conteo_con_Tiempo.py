#El siguiente programa cuenta hasta cinco y pausa durante un segundo entre cada número. El programa imprime "¡Listo!" cuando termina.
import time

# Bucle for que cuenta hasta cinco
for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)  # Pausa de 1 segundo

# Mensaje final
print("¡Listo!")
