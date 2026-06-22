"""La property()función integrada de Python permite gestionar cómo
 se accede a los atributos de una clase y cómo se modifican.
   En lugar de llamar a un método getter o setter explícito, 
   puedes crear atributos que se comporten como variables normales ,
   pero que incluyan lógica personalizada internamente.
   
    -- Respuesta rápida: ¿Qué son las propiedades en Python? --
Una propiedad de Python es un tipo especial de atributo que permite ejecutar código cada vez que se accede a ella,se establece o se elimina. 
Permite mostrar al usuario lo que parece un atributo simple, ocultando la lógica interna para
obtener o establecer su valor (métodos getter y setter). Esto se suele hacer utilizando el
⭐ @propertydecorador `@Property`.  

 Los getters y setters en otros lenguajes te permiten acceder a los atributos de una clase y podés imponer reglas de validación,
 bloquear ciertas cosas, etc controlar cómo se leen o modifican.

    ⭐En Python, un setter es un método diseñado para modificar o asignar el valor 
    de un atributo de una clase (especialmente aquellos que se consideran privados).
      Se utiliza para controlar cómo se actualizan los datos, permitiendo aplicar
     reglas de validación o transformaciones antes de guardar el valor.

    ⭐un getter es un método diseñado para obtener (leer) el valor de un atributo de un objeto, especialmente si es privado o protegido. 
    En lugar de definir métodos clásicos como get_valor(), la práctica estándar y más 🐍🐍"pythonica"🐍🐍
    es utilizar el decorador @property para crear accesores que se leen como atributos normales⭐"""

print("\n 🐍 la estructura general de una función decoradora en Python:")
def decorador(f): #(las chispas de chocolate 🍦✨) que toma una función f como argumento
    def funcion_nueva():
        print("Funcionalidad extra")
        f() #es llamada dentro de funcion_nueva para obtener la misma funcionalidad y agregar funcionalidad nueva antes de la llamada a la función
    return funcion_nueva # La función decoradora retorna la función anidada funcion_nueva.

@decorador #FUNCION DECORADORA 🍦 
def funcion_inicial():
    print("Funcionalidad inicial")

funcion_inicial()
#Resultado:
#Funcionalidad extra
#Funcionalidad inicial

print("="*40)

class Temperature:
    def __init__(self, celsius):
        # Internal, "private" variable
        self._celsius = celsius

     # 1. Define the "getter" with @property    = Adquiridor
    @property
    def temp(self):
     print("Getting temperature...")
     return self._celsius

     # 2. Define the "setter" with @temp.setter = conjunto 
    @temp.setter
    def temp(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible.")
        print("Setting temperature...")
        self._celsius = value

# Usage
t = Temperature(25)
current_temp = t.temp # Accesses the getter
# Outputs: Getting temperature...
print(current_temp)
# Outputs: 25

t.temp = 30 # Accesses the setter
# Outputs: Setting temperature...

print("\n 🐍 ejercicio 2 - Aplicacion de sintaxis:")
#En la programación orientada a objetos, se recomienda ocultar los datos usando un guion bajo antes del nombre del atributo (ej. _edad) y exponer un método decorado con @property
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad  # Atributo privado

    @property
    def edad(self):
        # Este es el getter
        return self._edad

# Uso:
persona1 = Persona("Ana", 28)
print(persona1.edad)  # No requiere paréntesis, se llama como un atributo
"""¿Por qué se utilizan?
Los getters son vitales para cumplir con el principio de encapsulación y ofrecen las siguientes ventajas:
   - Control de lectura: Puedes procesar o transformar el dato antes de entregarlo.
   - Compatibilidad: Te permite cambiar la lógica interna de la clase sin alterar el código de otros programas que utilizan tu objeto."""

print("\n 🐍 ejercicio 3 - El método .get() en diccionarios:")
#Si la consulta se refiere a la función nativa .get() para diccionarios, esta se usa para acceder a una clave de forma segura. 
#Si la clave no existe, no arroja un error, sino que devuelve None (o un valor predeterminado que definas).

# Ejemplo de diccionario
usuario = {"nombre": "Carlos", "rol": "admin"}

# Obtener clave existente
print(usuario.get("nombre"))  # Imprime: Carlos

# Obtener clave que no existe, evitando error
print(usuario.get("apellido"))  # Imprime: None
print(usuario.get("apellido", "No especificado"))  # Imprime: No especificado

print("\n 🐍 @property: sintaxis y lógica:")
class Casa:

	def __init__(self, precio):
		self._precio = precio

	@property
	def precio(self):
		return self._precio
	
	@precio.setter
	def precio(self, precio_nuevo):
		if precio_nuevo > 0 and isinstance(precio_nuevo, float):
			self._precio = precio_nuevo # se considera "protegido"
		else:
			print("Por favor ingrese un precio valido.")

	@precio.deleter
	def precio(self):
		del self._precio

# EXISTEN 3 METODOS PARA UNA PROPIEDAD:
          #Un getter - para acceder al valor del atributo.
          #Un setter - para actualizar el valor del atributo.
          #Un deleter - para eliminar el atributo de la instancia

          # ejemplo metodo setter
casa = Casa(50000.0)    # Crear instancia
casa.precio = 45000.0   # Actualizar valor
casa.precio             # Acceder al valor
#Nota cómo no estamos cambiando la sintaxis pero ahora usamos un intermediario (el setter) para validar el argumento antes de asignarlo. El valor nuevo (45000.0) se pasa como argumento para el setter


casa = Casa(50000.0)
casa.precio = -50
# Resultado :Por favor ingrese un valor valido
"""💡 Dato: esto prueba que el método setter sí está actuando como intermediario. 
Se llama "detrás de escenas" cuando intentamos actualizar el valor y el mensaje 
se muestra cuando el valor no es válido."""