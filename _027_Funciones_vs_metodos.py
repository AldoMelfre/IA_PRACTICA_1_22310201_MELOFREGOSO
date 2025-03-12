#Un método es un tipo específico de función - se comporta como una función y se parece a una función, pero difiere en la forma en que actúa y en su estilo de invocación.
#
#Un método es una función que pertenece a un objeto y se llama a través de ese objeto. En Python, los métodos se definen dentro de la definición de una clase y se utilizan para realizar operaciones en los objetos de esa clase.
#
#Por ejemplo, considera la clase Persona que tiene un método llamado saludar():
#
class persona:
    def saludar(self):
        print("Hola, soy Aldo")

#En este ejemplo, la clase Persona tiene un método llamado saludar(). Este método imprime un mensaje de saludo en la consola.

#Para llamar a un método, primero necesitas crear un objeto de la clase y luego llamar al método a través de ese objeto. Aquí hay un ejemplo que muestra cómo se puede llamar al método saludar() de la clase Persona:
# Crear un objeto de la clase Persona
p = persona()
# Llamar al método saludar() del objeto p
p.saludar()
#En este ejemplo, primero creamos un objeto de la clase Persona llamado p. Luego, llamamos al método saludar() a través de este objeto. Cuando se ejecuta este código, se imprime el mensaje "Hola, soy Aldo" en la consola.

print("\n----------------------\n")
#
result = function(arg)