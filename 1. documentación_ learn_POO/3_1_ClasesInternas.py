"""Una clase interna es una clase DEFINIDA DENTRO DE OTRA CLASE.
 La clase interna puede acceder a las propiedades y métodos de la clase externa.

Las clases internas son útiles para agrupar clases que solo se utilizan en un lugar, 
lo que hace que tu código esté más organizado.- BUENA PRACTICA👍🏼"""

#Ejemplo -Crear una clase interna: 
    # 2. Acceder a la clase interna desde fuera
    # 3. Acceso a la clase externa desde la clase interna

class Outer: # = exterior / externa
  def __init__(self):
    self.name = "Outer Class"

  class Inner: # = interior/ interno
    def __init__(self,outer): #3.
      self.name = "Inner Class"

      # 3 Si desea que la clase interna acceda a la clase externa, debe pasar la instancia de la clase externa como parámetro:
      self.outer = outer 

    def display(self):
      print("This is the inner class")
      print("Hello from inner class") #2.
      print(f"Outer class name: {self.outer.name}") #3.

outer = Outer()
print(outer.name) # Resultado 1 :Outer Class

#inner = outer.Inner() #2. Se crea una variable que permita acceder a la clase interna por medio de otras variables y llamando la clase interna (que en este caso es muy explixita) - haciendo el  punto 3 ya esto no es necesario

inner = outer.Inner(outer) # 3
inner.display() # 2

"""Notas de los puntos de los ejercicios

PUNTO #2 = Para acceder a la clase interna, cree un objeto de la clase externa y, a continuación, cree un objeto de la clase interna

PUNTO #3 = En Python, las clases internas no tienen acceso automático a la instancia de la clase externa.

Si desea que la clase interna acceda a la clase externa, debe pasar la instancia de la clase externa como parámetro:
"""
print("\n" + "="*50)
print(" EJEMPLO Practico \n " \
"Las clases internas son útiles para crear clases auxiliares que solo \n" \
"se utilizan dentro del contexto de la clase externa:")
print("="*50)

# Utilice una clase interna para representar el motor de un automóvil:
class Car:
  def __init__(self, brand, model):
    self.brand = brand #marca
    self.model = model
    self.engine = self.Engine() #motor

  class Engine:
    def __init__(self):
      self.status = "Off" #estado

    def start(self):
      self.status = "Running"
      print("Engine started")

    def stop(self):
      self.status = "Off"
      print("Engine stopped")

  def drive(self):
    if self.engine.status == "Running":
      print(f"Driving the {self.brand} {self.model}")
    else:
      print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()

#Resultado:
#Start the engine first!
#Engine started
#Driving the Toyota Corolla

#-------------------------------
print("\n" + "="*50)
print(" EJEMPLO Practico \n " \
"Múltiples clases internas")
print("="*50)
#-------------------------------

class Computer:
  def __init__(self):
    self.cpu = self.CPU()
    self.ram = self.RAM()

  class CPU:
    def process(self):
      print("Processing data...")

  class RAM:
    def store(self):
      print("Storing data...")

computer = Computer()
computer.cpu.process()
computer.ram.store()