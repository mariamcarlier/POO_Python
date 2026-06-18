class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self): 
        print (f"{self.name} el perro dice Guaaauu!")

d1= Dog(name= "Buddy" ,age= 3)

d1.bark()
        