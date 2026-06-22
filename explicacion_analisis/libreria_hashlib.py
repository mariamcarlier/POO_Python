import hashlib

# 1. Crear el objeto hash (ejemplo con SHA-256)
mensaje = "Hola mundo"
hash_objeto = hashlib.sha256(mensaje.encode('utf-8'))

# 2. Obtener la cadena hexadecimal resultante
resultado = hash_objeto.hexdigest()
print(resultado)

"""Algoritmos disponibles Python 
garantiza soporte para los siguientes algoritmos en todas las plataformas:
md5sha1sha224, sha256, sha384, sha512sha3_224, sha3_256, sha3_384, sha3_512shake_128, shake_256blake2b, blake2s
También se pueden listar los algoritmos soportados dinámicamente por OpenSSL en tu sistema utilizando hashlib.algorithms_available.

Funciones de utilidad
- update(bytes): Añade más datos al objeto hash. El hash final será el equivalente a haber concatenado todas las entradas.

- hexdigest(): Devuelve el resumen del hash como una cadena alfanumérica de caracteres hexadecimales.
- 🧠new(nombre_algoritmo): Método genérico que permite instanciar cualquier algoritmo pasándolo como cadena de texto (muy útil si el nombre del algoritmo viene de una variable"""

hash_objeto = hashlib.sha1(mensaje.encode('utf-8'))

# 2. Obtener la cadena hexadecimal resultante
resultado = hash_objeto.hexdigest()
print(resultado)

print("🧠")
#En este ejemplo, una función recibe el nombre del algoritmo dinámicamente y calcula el hash del mismo texto:
import hashlib

def generar_hash_dinamico(nombre_algoritmo, texto):
    # Convertir el texto a bytes
    datos_bytes = texto.encode('utf-8')
    
    try:
        # Se pasa el string directamente a hashlib.new()
        objeto_hash = hashlib.new(nombre_algoritmo)
        objeto_hash.update(datos_bytes)
        return objeto_hash.hexdigest()
    
    except ValueError:
        return f"Error: El algoritmo '{nombre_algoritmo}' no está soportado."

# Datos de prueba
mensaje = "Python 2026"

# Probamos la función con diferentes algoritmos usando strings
print("SHA-256:", generar_hash_dinamico("sha256", mensaje))
print("MD5:    ", generar_hash_dinamico("md5", mensaje))
print("SHA-512:", generar_hash_dinamico("sha512", mensaje))

"""No, con la librería hashlib no se puede ocultar visualmente el texto en la pantalla mediante puntos o asteriscos.
Cumplen funciones totalmente distintas en la seguridad:
    - HTML (type="password"): Se encarga de la seguridad visual en la interfaz. Oculta los caracteres en la pantalla para que nadie que esté mirando tu monitor pueda ver lo que escribes.
    - hashlib (Python): Se encarga de la seguridad lógica en el servidor. Recibe la contraseña en texto plano (una vez que el usuario la envía) y la transforma en un código irreversible (hash) para guardarla de forma segura en la base de datos.
    
    💻 Cómo ocultar el texto en la terminal de Python
    Si estás creando un programa de consola en Python y quieres lograr el mismo efecto que el type="password" de HTML (que no se vea lo que escribe el usuario), debes usar la librería nativa 🧠getpass"""

"""
# Aqui esta un tipo de implementacion de ambas librerias para un flujo seguro:
import hashlib
import getpass

# 1. getpass oculta visualmente lo que el usuario escribe en la consola
password_oculta = getpass.getpass("Introduce tu contraseña: ")

# 2. hashlib cifra el resultado para que no se guarde en texto plano
hash_objeto = hashlib.sha256(password_oculta.encode('utf-8'))
password_hasheada = hash_objeto.hexdigest()

print("\n[Proceso completado]")
print("Tu contraseña fue procesada de forma segura.")
print(f"Hash guardado en el servidor: {password_hasheada}")"""

print("\n[Opción 1: Con la librería nativa (Oculta el texto por completo)]")
#Este método viene integrado en Python y no requiere instalar nada.
import hashlib
import getpass

print("--- REGISTRO DE USUARIO (CONSOLA) ---")

# 1. Solicitar el texto de forma oculta (no se verá nada mientras escribes)
password = getpass.getpass("Escribe tu contraseña y presiona Enter: ")

# 2. Convertir a bytes y generar el hash con SHA-256
password_bytes = password.encode('utf-8')
hash_resultado = hashlib.sha256(password_bytes).hexdigest()

# 3. Mostrar el funcionamiento
print("\n--- RESULTADO EN EL SERVIDOR ---")
print(f"Longitud de tu contraseña original: {len(password)} caracteres.")
print(f"Hash SHA-256 generado para la base de datos:\n{hash_resultado}")

print("\n[Opción 2: Con asteriscos * (Requiere instalación)]")
#Si quieres emular exactamente el comportamiento visual de HTML, abre tu terminal e instala este paquete:
#pip install pwinput
"""import hashlib
import pwinput

print("--- REGISTRO DE USUARIO (CON ASTERISCOS) ---")

# 1. Solicitar el texto mostrando asteriscos
password = pwinput.pwinput(prompt="Escribe tu contraseña: ", mask="*")

# 2. Generar el hash
hash_resultado = hashlib.sha256(password.encode('utf-8')).hexdigest()

# 3. Mostrar el funcionamiento
print("\n--- RESULTADO EN EL SERVIDOR ---")
print(f"Tu contraseña real sigue oculta, pero su hash es:\n{hash_resultado}")
"""