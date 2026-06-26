# PROPIEDAD DE CLASE FRENTE A LA PROPIEDADE DE INSTANCIA:
class Person:
  species = "Human" # Class property
  lastname = "" #👌EJEMPLO MODIFICACION

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

w1 = Person("Samuel") #🆙AGREGAR NUEVAS PROPIEDADES
w1.age = 15#🆙
w1.city= "Bogotá"#🆙

Person.lastname = "Swan" #👌 datos

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

print(p1.lastname, p1.name)#👌 imprimir para verlos
print(p2.lastname, p2.name)#👌 imprime el mismo apellido ya que asi se asigno 

print(p1.name) #🆙
print(p1.age)  #🆙
print(p1.city) #🆙
#NOTA: Agregar propiedades de esta manera solo se agregan a ese objeto específico, no a todos los objetos de la clase.