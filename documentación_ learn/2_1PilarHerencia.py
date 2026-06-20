# -----------------------------------------------------------------
# HERENCIA EN PYTHON
print("="*50)
print("Python Inheritance = PILAR de Herencia 👨‍👩‍👧‍👦")
print("="*50)
# La herencia nos permite definir una clase que hereda todos los métodos y propiedades de otra clase.

# La clase padre es la clase de la que se hereda, también llamada clase base. - SUPERCLASE
# La clase hija es la clase que hereda de otra clase, también llamada clase derivada. -SUBCLASE
# -----------------------------------------------------------------

# 1. Crear una clase padre
"""Crea una clase llamada Person, con las propiedades first name y lastname, y un print name método:"""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the print name method:
x = Person("Robert", "pattison")
x.printname()

# 2, Crear una clase hija
"""crear una clase que -HEREDE LA FUNCIONALIDAD- de otra clase y envie la clase padre como UN PARAMETRO al crear la clase hija 
- osea que la clase hija se define con el nombre de la clase padre entre paréntesis.

Asi: class Student(Person):"""

class Student(Person): # AQUI YA HEREDA LOS ATRIBUTOS Y METODOS DE LA CLASE PADRE-PERSON
            #pass / 2.2,
            # pARAMETRO INIT - Si se utiliza en la clase padre ANULAAA 🙅🏼‍♀️ la herencia, por lo que se debe usar el metodo super()🦸🏼‍♂️ para llamar al metodo init de la clase padre y pasarle los parametros necesarios para inicializar las propiedades heredadas

            #Para mantener la herencia de la función (__init__() ) del padre, agregue HAY QUE AGREGAR todos los parametros , aunque tenga que agregar nuevos parametros para la clase hija, y luego usar super()🦸🏼‍♂️ para llamar el metodo de la clase padre y pasarle los parametros necesarios para inicializar las propiedades heredadas

  def __init__(self, fname, lname, year):
    #Person.__init__(self, fname, lname) #2.2.add properties etc. AQUI SE HA MANTENIDO LA HERENCIA DE LA CLASE PADRE-PERSON, Y SE HAN AGREGADO NUEVAS PROPIEDADES A LA CLASE HIJA-STUDENT

     super().__init__(fname, lname)   
            #2.3.super()🦸🏼‍♂️ se usa para llamar al metodo init de la clase padre y pasarle los parametros necesarios para inicializar las propiedades heredadas / a comparacion de el mensaje anterior tipo codigo ahora NO es necesario usar el nombre de elemento , sino que LA FUNCION SUPER🦸🏼‍♂️ lo hace automaticamente

#3.1 Agregar propiedades - nuevas propias de la clase hija
     #self.graduationyear = 2024 # de Aqui se crea un nuevo parametro (year)
     self.graduationyear = year 

# 4. Agregar métodos
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Yuri", "Corredor", 2024)
x.printname()
print(x.graduationyear)
x.welcome()

#2.1,Utilice la clase Student para crear un objeto y, ejecutar el método print name:
y = Student("Olivia", "Rodrigo", 2021)
y.printname()


# -----------------------------------------------------------------
# DESAFIOOO -- HERENCIA EN PYTHON
print("="*50)
print("Python Inheritance CHALLENGUE 👨‍👩‍👧‍👦")
print("="*50)
""""Instrucciones 
    1. Crea una clase padre Animal con un __init__que tome name
    2. Agregue un método speak que imprima el nombre
    3. Crea una clase hija Dog que herede de Animal
    4. Crear un objeto d1 = Dog("Rex")
    5. Llamar d1.speak()
"""
# -----------------------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says: Woof!")

class Dog(Animal):
    pass
d1 = Dog("Rex")
d1.speak()
# Resultado: Rex says: Woof!
