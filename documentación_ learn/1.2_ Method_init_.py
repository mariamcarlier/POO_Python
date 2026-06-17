#NOTAS:
#Método __init__() = se utiliza para asignar valores a las propiedades de un objeto o para realizar operaciones necesarias durante su creación.

# 1 . CLASE SIN DEFINIR NI EL METODO INIT
# preguntas - Por qué se usa init
# tiene muchas desventajas que sin ese metodo tendria que configurarse las propiedades manualmente asi:

#  Ejemplo - Crar una clase sin init
class Person:
  pass # se usa la instrucción pass ya que no se definen elementos en la clase

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name) #Tobias
print(p1.age)   #25

# 2 . AHORA ACON INIT 
# EL USO de este FACILITA la creación de objetos con valores iniciales: - TAMBIEN SE usa lo mismo que los diagramas uml DRY (para no repetir/ hacerlo manualmente)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#ESTO SE HACE como si fueran valores predeterminados
p1 = Person("Linus", 28)
print(p1.name)
print(p1.age)

p2 = Person("Mickey Mouse", 100)
print(p2.name , p2.age)

#3 Múltiples parámetros - el metodo init puede tener tantos parámetros como necesite:
#Ejemplo crear persona con multiples parametros
print("="*35)
print("...  Multiples parámetros  ...")

class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
