# Para crear una clase utilizar la PALABRA CLAVE = (Class)
# 1. crear una clase 
class MyClass:
  x = 5
  j = 10

# 2. crear un objeto
p1 = MyClass() #llamar la clase para crear dentro de si objetos - variable+clase
print(p1.j)
# 3. eliminar objetos / Utilizando la palabra clave (del)
del p1 

#Multiples objetos
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

print("="*35)
print("...  SINTAXIS  ...")

class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

#Nota: Cada objeto es independiente y tiene su propia copia de las propiedades de la clase.

p1 = Person("Emil")
print(p1.age)

"""La declaración de pase
-Las definiciones no pueden estar vacías, 
pero si por alguna razón LO ESTÁ =(CLASS -sin contenido),

Solucion: incluir la instruccion (~pass~) para evitar obtener un error."""
class Person:
  pass

