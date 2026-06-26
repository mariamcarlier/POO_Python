# Desafío: Propiedades de clase
# -----------------------------------------------------------------
# EJERCICIO TIPO CALIFICACIONES DE ESTUDIANTES
# -----------------------------------------------------------------

print("="*40)
print("Desafío #1 : Propiedades de clase")
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

# -----------------------------------------------------------------
# EJERCICIO TIPO AREA DE UN RECTANGULO
# -----------------------------------------------------------------

print("="*40)
print("Desafío #2 : Metodos de clase")
"""Instrucciones
    1.Dentro del editor, complete los siguientes pasos:
    2.Crea una clase llamadaRectangle
    3.Agregue un __init__método con widthy height, y almacénelos como propiedades.
    4.Agrega un método area que devuelva el ancho multiplicado por la altura.
    5.Crea un objeto r1con un ancho de 5 y una altura de 3.
    6.Imprime el área der1"""

class Rectangle:
    def __init__ (self, width, height): 
        self.width = width
        self.height = height

    def area (self): #4. METODO AREA QUE DEVUELVA EL ANCHO MULTIPLICADO POR LA ALTURA
        #LOGICA - SE USA (RETURN) PARA DEVOLVER UN VALOR DESDE EL METODO, EN ESTE CASO EL AREA DEL RECTANGULO
        #Tambien se usa self para acceder a las propiedades width y height dentro del metodo area
        return self.width * self.height

r1 = Rectangle(5, 3)
print(r1.area())