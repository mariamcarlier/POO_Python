#Encapsulation=  La encapsulaciòn consiste en proteger los datos dentro de una clase .
"""Significa mantener los datos (propiedades) y los métodos juntos en una clase, controlando al mismo tiempo cómo se puede acceder a los datos desde fuera de la clase.

Esto evita cambios accidentales en tus datos y oculta los detalles internos del funcionamiento de tu clase."""

#Private Properties - PROPIEDADES PRIVADAS
"""En Python, puedes hacer que una propiedad sea privada al agregar dos guiones bajos (__) 
antes del nombre de la propiedad. Esto hace que la propiedad no sea accesible desde fuera de la clase.

📐En la documentacion al hacer uso de este concepto en diagrmas UML se representa con un simbolo de menos (-) antes del nombre de la propiedad, lo que indica que es privada."""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Madisson", 25)
print(p1.name)
#print(p1.__age) # This will cause an error
# dice: AttributeError: 'Person' object has no attribute '__age' 
# -> Uso de guiones bajos (Atributos privados): En Python, al usar doble guion bajo (__) al principio de una variable, esta se vuelve privada o masticada (name mangling). El atributo ya no se llama __age, sino _Person__age.


# 2. Get Private Property Value - OBTENER EL VALOR DE UNA PROPIEDAD PRIVADA
# 3. Establecer el valor de la propiedad privada 
"""Para modificar una propiedad privada, puede crear un método Getter = Adquiridor🎖️.

El (método Getter) también puede validar el valor antes de establecerlo:ES CONOCIDO COMO UN METODO PUENTE """

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age # se usa para DEVOLVEER EL VALOR  de la edad hacia afuera 
# EL RETURN Le dice a python:"Toma el valor que está guardado internamente en self.__age y entrégaselo a quien sea que haya llamado a esta función".
#  
  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())
#Gracias al return, al imprimir la linea anterior recibe el número 25 y lo puede mostrar en la pantalla. Sin el return, la función no entregaría nada (devolvería None).

p1.set_age(26)
print(p1.get_age())#Utilizando un método getter para acceder a una propiedad privada:🎖️

#2. METODOS PRIVADOS
#También SE puede hacer que los métodos sean privados utilizando el prefijo de doble guion bajo:
class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):#aqui validate se conviete en un metodo privado
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # This would cause an error