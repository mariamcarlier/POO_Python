
class Dog: # 1. crear la clase Dog
    def __init__(self, name, age): #2. crear el metodo init con parametros y almacenar como propiedades usando self
        self.name = name
        self.age = age

    def bark(self): # agregar el metodo bark que imprima algo 
        print (f"{self.name} el perro dice Guaaauu!")

#d1= Dog(name= "Buddy" ,age= 3)
d1 = Dog("Buddy" , 3)
d1.bark()
        