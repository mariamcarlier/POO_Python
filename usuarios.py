"""class Usuario:
    id_usuario = 1
    documento = 1057894567
    nombre = "valery daniela" 
    apellido = "cuta perez"
    correo = "chemistryqueen@gmail.com"
    telefono = 3218765432
    direccion = "Cra 14 43"

#creando una instancia de la clase usuario
usuario_1 = Usuario() #creamos la copia dentro de una variable
usuario_2 = Usuario()

usuario_2.nombre = "daniela"
#se empieza a trabajar con la copia/ acceder a los atributos y metodos
print(usuario_1.nombre) # valery daniela
print(usuario_1.correo) # chemistryqueen@gmail.com
print(usuario_2.nombre) # daniela

"""
# __init__()método se utiliza para asignar valores a las propiedades de un objeto o para realizar operaciones necesarias durante su creación.

#(~LISTA~)
lista_usuarios= [] # Lista global para guardar datos

class Usuario:
     #Crear una funcion para el CONSTRUCTOR
     def __init__(self, id_usuario:int ,  documento, nombre:str , apellido , correo, telefono ,direccion): #parametro de entrada
          # El (parámetro self) debe ser el primer parámetro de cualquier método de la clase. 
          self.id_usuario = id_usuario
          self.documento = documento
          self.nombre = nombre
          self.apellido = apellido
          self.correo = correo
          self.telefono = telefono
          self.direccion = direccion
     
     def saludar (self):
         print(f"Hola, mi nombre es {self.nombre} {self.apellido}")

    # Metodos Base de CRUD (~LISTA~)
        #CREATE
     def crear_usuario (self):
         lista_usuarios.append(self)
         print(f"✅ Éxito: El usuario {self.nombre} ha sido registrado en el sistema")

        #READ
     def ver_usuario (self):
          print(f"ID: {self.id_usuario} Nombre: {self.nombre} {self.apellido}")

        #UPDATE
     def actualizar_usuarios (self, nuevo_nombre , nuevo_apellido):
         self.nombre = nuevo_nombre
         self.apellido = nuevo_apellido
         print(f"✅ Éxito: El usuario ha sido actualizado a {self.nombre} {self.apellido}")

        #DELETE
     def eliminar_usuario(self):
          if self in lista_usuarios:
               lista_usuarios.remove(self)
               print(f"✅ Éxito: El usuario {self.nombre} no se encuentra en el sistema.")
          else:
               print(f"☣️ Advertencia: El usuario {self.nombre} no existe")

#Creando una Instancia de la clase usuario
usuario_1 = Usuario(1,1057856734, "Falcao", "García", "fgarcia@gmail.com",3124567892, "Calle 123")

usuario_2 = Usuario(2,1057101111, "James", "Rodriguez", "james10rodr@gmail.com",3110101011, "Calle 910")

print(usuario_1)
print(usuario_1.nombre)
print(usuario_2.nombre , usuario_2.correo) 
print(usuario_2.documento)
# el constructor es importante para no quemar el codigo

#Llame a los metodos de la clase usuario
usuario_1.saludar()
usuario_2.saludar()

"""# usando las funciones del crud ~LISTA~
usuario_1.ver_usuario()
print(f"Lista de usuarios :{lista_usuarios}")

usuario_1.crear_usuario()
print(f"Lista de usuarios :{lista_usuarios}") #muestra solo el objeto / ninguno en especifico
print(f"Lista de usuarios :{lista_usuarios[0].nombre}") #ser especifico del nombre que se ve con indice = Falcao
print(f"Lista de usuarios :{lista_usuarios[1].nombre}") # = James"""

#Metodos CREATE
print(f"Lista de usuarios :{lista_usuarios}") #Lista vacía
usuario_1.crear_usuario()
usuario_2.crear_usuario()

#Llamar los métodos READ 
print(f"Lista de usuarios :{lista_usuarios[0].nombre}")
print(f"Lista de usuarios :{lista_usuarios[1].nombre}")
usuario_1.ver_usuario
usuario_2.ver_usuario
#✅ya salen en la lista

#Llamar los métodos update
usuario_1.actualizar_usuarios("Messi", "Ronaldo")
usuario_1.ver_usuario()

#
