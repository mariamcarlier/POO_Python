# -----------------------------------------------------------------
# POLIMORFISMO EN PYTHON

print("="*50)
print("Python Polymorphism = PILAR de POLIMORFISMO 👨‍👩‍👧‍👦")
print("="*50)

"""""  polymorphism" means     "many forms"
       polimorfismo" significa "muchas formas", 
y en programación se refiere a métodos/funciones/operadores 
con el mismo nombre que pueden ejecutarse en muchos objetos o clases.
"""
# -----------------------------------------------------------------

# 1- POLIMORFISMO FUNCIONAL 
print("\n--- POLIMORFISMO FUNCIONAL ---")

    # 1.1 Cadena - utilizando la funcion LEN()
x = "Hello World!"
print(x)
print(len(x)) #len()devuelve el número de caracteres: Resultado = 12

    # 1.2 Tupla 
mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(len(mytuple)) #len()devuelve el número de elementos: Resultado = 3

    # 1.3 Diccionarios
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "black"
}

print(len(thisdict)) #len()devuelve el número de pares clave/valor en el diccionario: 4
# -----------------------------------------------------------------

# 1- POLIMORFISMO APLICADO A CLASES Y OBJETOS 
print("\n--- POLIMORFISMO DE CLASE ---")

""""El polimorfismo se utiliza a menudo en los métodos de clase, donde podemos tener varias clases con el mismo nombre de método.

Por ejemplo, supongamos que tenemos tres clases: Car, Boat, y Plane, y que todas ellas tienen un método llamado move(): """
print("Ejercicio # 1")
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

print("\n Ejercicio # 2")
"""¿Qué ocurre con las clases que tienen clases hijas con el mismo nombre? ¿Podemos usar polimorfismo en esos casos?

Sí. Si usamos el ejemplo anterior y creamos una clase padre llamada Vehicle, y creamos Car, Boat, Plane clases hijas de Vehicle, las clases hijas heredan los Vehiclemétodos, pero pueden sobrescribirlos:"""

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self): #mover
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

print("\n Ejercicio # 3- DESAFIOSS")
"""Instrucciones
Crea una clase Cat con un método sound que imprima "Miau".
Crea una clase Fox con un método sound que imprima "¡Wa-pa-pa-pa-pa-pow!"
Crear objetos c1 = Cat()yf1 = Fox()
Llamar sound()a ambos objetos"""
class Cat:
    def sound(self):
            print("miau")

#Crear la clase Zorro
class Fox:
    def sound(self):
            print("¡Wa-pa-pa-pa-pa-pow!")

#Crear objetos y bucle 
c1 = Cat()
f1 = Fox()

for animal in (c1, f1):
    animal.sound()