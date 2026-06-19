# Desafío: Propiedades de clase
"""Instrucciones - Dentro del editor, complete los siguientes pasos:

    1. Crea una clase Student con un __init__que tome name y grade, y los almacene como propiedades.
    2. Crea un objeto s1con el nombre "Anna" y la calificación "A".
    3. Imprime la calificación de s1
    4. Cambia la calificación s1a "B".
    5. Imprime la calificación actualizada"""

class Student:
    def __init__ (self, name, grade):
        self.name = name
        self.grade= grade

s1 = Student("Anna", "A" )
#3 Imprimir las calificaciones
print(s1.grade)

#4 cambiar la calificacion
s1.grade = "B"
print(s1.grade)