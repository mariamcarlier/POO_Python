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
     #def encriptar_contraseña(self, contraseña):
              #print(f"Contraseña encriptada: {contraseña}")

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
               print(f"☣️ Advertencia: El usuario {self.nombre} no existe/ no se encuentra en el sistema.")

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

print("\n ===== APLICACIÓN DE LOS 4 PILARES DE LA POO ===== \n")
#Buenas practicas (crear un nuevo archivo de la clase nueva(si es hija importar de la superclase ))
 
# herencia y encapsulamieneto aprendiz
#solo toca ponerlo (una clase) como parametro de entrada la superclase a una hija
#se esta usando el mismo constructor 

class Aprendiz(Usuario):
     def __init__(self, id_usuario:int ,  documento, nombre:str , apellido , correo, telefono ,direccion, programa , ficha, competencias = None): #se llama los mismos atributos del constructor principal/ por CONVENCION Y NORMA

          #Usamos super() para llamar al constructor de la clase padre (Usuario)
          #va sin self ya no referencia la clase anterior / se esta haciendo referencia a la clase padre
          super().__init__(id_usuario, documento, nombre, apellido, correo, telefono, direccion)

          #Atributos propios del Aprendiz
          self.programa = programa
          self.ficha = ficha
          self.competencias = competencias

aprendiz_1 = (12,10573872836, "rafael", "luñez", "prorafa1@hotmail.com", 3142345678, "Calle 220", "Análisis y Desarrollo de Software","2550001")

aprendiz_2 = (22, 1057980449 , "Amelie", "Carlier Alvarado" , "ameliecarlierdesign@gmail.com" , 3003409567, "Cra 16 8" , "Multimedia" , "33217893")


class Instructor(Usuario):
    def __init__(self, id_usuario, documento, nombre, apellido, correo, telefono, direccion, perfil_profesional, anios_experiencia):
        
        super().__init__(id_usuario, documento, nombre, apellido, correo, telefono, direccion)

     # Atributos propios del Instructor
        self.perfil_profesional = perfil_profesional
        self.anios_experiencia = anios_experiencia

instructor_felipe = Instructor(1, 1213121, "Felipe","Sandoval", "afsandoval@gmail.com","321481513", "Carrera 123","Análisis y Desarrollo de Software","2550001" )
print(instructor_felipe.nombre )


print(f"Imprimir atributo privado {aprendiz_1.get_resultados }")