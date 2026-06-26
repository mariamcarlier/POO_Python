# PARÁMETRO PROPIO DE PYTHON🐍- EJ CON SET 
class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name )

  def saludar(myobject):
    print(f"Hola mi nombre es {myobject.name} y tengo {myobject.age} años 🤩🤗" )

p1 = Person("Emil", 36)
p1.greet()

persona_1 = Person("Salome",4)
persona_1.saludar()

#en este caso que no se usa el parametro SELF - Se recomienda:
#no es necesario llamarlo SELF
#Nota: Si bien puedes usar un nombre diferente, se recomienda encarecidamente usar este, (self) ya que es la convención en Python y hace que EL código sea más legible para otros.

# DESAFIO AUTOPARÁMETRO 
"""Instrucciones 🫡
Dentro del editor, complete los siguientes pasos:
    1. Crea una clase llamadaCar
    2. Agregue un __init__método con un brandparámetro y almacénelo como una propiedad.
    3. Agregue un método llamado showque imprima la marca
    4. Crea un objeto c1de la Carclase con la marca "Ford".
    5. Llama al showmétodo enc1"""

print("SOLUCION DEL EJERCICIO -CODIGO BORRADOR / mio")
class Car:
  def __init__(brand, nombre_carro , marca):
    brand.nombre_carro = nombre_carro
    brand.marca = marca

  def show(brand):
    print("Hola , soy " + brand.marca + " y me llaman = 💨NOMBRE:" + brand.nombre_carro)

  def show_1(brand):
    print(f"Soy un {brand.nombre_carro} - {brand.marca} 🏎️")

c1 = Car("Freddy Millonario", "Ferrari")
c1.show()

vehiculo = Car("Freddy Millonario", "Ferrari")
vehiculo.show_1()

print("="*35)
print("SOLUCION DEL EJERCICIO -CODIGO")
#SOLUTION:

# Create the Car class
class Car:
  def __init__(self, brand):
    self.brand = brand

  def show(self):
    print(self.brand)

# Create an object
c1 = Car("Ford")

# Call the show method
c1.show()

print("\n propiedades de acceso \n -CODIGO para Acceder a las propiedades de un objeto: ")
print("="*35)

class Carro:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Carro("Toyota", "Corolla")

print(car1.brand)
print(car1.model)
print("="*35)

#PROPIEDADES PARA ELIMINAR 
#palabra clave -del- ASI: ejemplo:
#del p1.age
#print(p1.name) # This works
# print(p1.age) # This would cause an error
