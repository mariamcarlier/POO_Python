print("="*50)
print("\ EJEMPLO DE APLICACION \n Y LA IMPORTANCIA DE UTILIZAR LA ENCAPSULACIÒN")
print("="*50+"\n")
print("🟩 VENTAJAS 🟩\n" \
" ✅ Protección de datos: Evita la modificación accidental de datos.\n" 
" ✅ Validación: Puede validar los datos antes de configurarlos.\n"
" ✅ Flexibilidad: La implementación interna puede cambiar sin afectar al código externo.\n"
" ✅ Control: Usted tiene control total sobre cómo se accede a los datos y cómo se modifican.\n")

class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())

print("="*50)
print("\ EJEMPLO DE APLICACION \n PROPIEDADES PROTEGIDAS #")
print("="*50)
print("🟡NOTA:\n \
      El guion bajo simple _es solo una CONVENCIóN.\n Indica a otros programadores que la propiedad está destinada a uso interno,\n pero Python no impone esta restricción.🟡")
print("="*50 +"\n")
print(" Ejercicio: Ejemplo \n ")


class Person:
  def __init__(self, name, salary,age):
    self.name = name
    self._salary = salary # Protected property
    self.__age = age

p1 = Person("Paris", 50000, 26)
p2 = Person("Pattinson",2000, age=30)
print(p1.name)
print(p1._salary) # Can access, but shouldn't = se puede acceder, pero NO SE RECOMIENDA, PQ ESTO CONTRADICE EL PROPOSITO DE LA ENCAPSULACION

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!
print("="*50+ "\n")

print("\ DESAFIO DE ENCAPSULACION  ")
print("="*50)
"""Instrucciones
    1. Crear una clase ScoreBoard
    2.Agregue __init__un score parámetro y guárdelo como un atributo privado.
    3.Agregue un método llamado get_scoreque devuelva la puntuación privada.
    4. Crea un objeto s1con una puntuación de 0.
    5. Imprime la puntuación des1"""

class ScoreBoard:
  def __init__(self, score):
    self.__score = score

  def get_score(self):# METODO
    return self.__score

  #punto 4: Crear un objeto
s1 = ScoreBoard(0)

  #imprimir el parametro score
print(s1.get_score())# Ejecuta la función, activa el return y da el valor real (0).
print(s1.get_score)#Solo hace referencia a la función como un objeto guardado en memoria, por eso muestra el mensaje de <bound method...>.

#Resultado sin paraentesis = : <bound method ScoreBoard.get_score of <__main__.ScoreBoard object at 0x000001EE8FFCD550>>
#reultado con parentesis:0
print("="*50)
print("\n OTRO EJERCICIO  ")
"""¡Vamos a hacer una prueba diferente para que veas la diferencia exacta entre "la máquina" (el método sin paréntesis) y "el producto de la máquina" (el método con paréntesis)!Imagina una clase llamada CajeroAutomatico. El dinero está protegido (encapsulado)."""
print("="*50)
class CajeroAutomatico:
    def __init__(self, dinero_disponible):
        self.__dinero = dinero_disponible  # El dinero está oculto en la caja fuerte

    def entregar_billetes(self):
        return "💵 Aquí tienes tus $100 dólares"

# Creamos el cajero con dinero adentro
mi_cajero = CajeroAutomatico(5000)

#1. Prueba A- Sin parentesis
print(mi_cajero.entregar_billetes)
#¿Qué pasó aquí? El cajero no te dio dinero. 
# Solo te imprimió la ficha técnica del botón físico que dice "entregar billetes". Viste el botón, pero no lo presionaste.

#2. Prueba B- CON parentesis
print(mi_cajero.entregar_billetes())
#¿Qué pasó aquí? Los paréntesis () fueron el dedo que presionó el botón. 
# El mecanismo interno se activó, el return sacó el dinero de la caja fuerte y te lo entregó. 
# ¡Cumpliste el objetivo!