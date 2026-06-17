#Poniendo a prueba los conocimientos
"""Dentro del editor, complete los siguientes pasos:
1.Crea una clase llamada Person
2.Agregue el método [__init__] que tome (name) y (age) como parámetros.
3.Agregue un método llamado (greet) que imprima un mensaje seguido del nombre
4.Crea un objeto p1 de la clase con el nombre "John" y la edad 36.
5.Llama al método (greet) en p1"""

#PASO 1 - Crear la clase
class Person:
    def __init__ (self, name , age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hola, mi nombre es " + self.name)

# PASO 2 - Crear un objeto -punto 4
p1= Person("Uma",22)

# Call the greet method
p1.greet()
