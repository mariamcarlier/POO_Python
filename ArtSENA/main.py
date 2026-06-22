# ← Mi punto de entrada para probar todo junto, ya que mi metodo en polimorfismo es mostrarpanel
from models.UsuariosGaleria import UsuarioGaleria
from services.Gestor_Galeria import GestorGaleria #2
from models.Cliente import Cliente #3
from models.Artista import Artista #4

# Instanciamos un usuario base (en la práctica nunca se usa
# UsuarioGaleria directamente, siempre sus subclases, pero
# sirve para probar que la clase padre funciona bien)
usuario_prueba = UsuarioGaleria(
    id_usuario=1,
    nombre="Mariam Carlier Alvarado",
    correo="mariam00estudio@gmail.com",
    telefono="+57 300 123456",
    contraseña="super_aprendiz22"
)

print(usuario_prueba.nombre)               # Mariam Carlier Alvarado
print(usuario_prueba.verificarContraseña("super_aprendiz22"))  # True
print(usuario_prueba.cambiarContraseña("clave_incorrecta", "nueva123"))  # ❌ mensaje de error
print(usuario_prueba.cambiarContraseña("super_aprendiz22", "nueva123"))  # ✅ mensaje de éxito
print(usuario_prueba.verificarContraseña("nueva123"))           # True
print(usuario_prueba.mostrarPanel())       # Panel genérico de usuario"""

# ----------------------------------------------------------------------------------
print("\n")
# ----------------------------------------------------------------------------------
# Creamos el gestor (vacío al inicio)
gestor = GestorGaleria()
print(gestor.listar_usuarios())  # 📭 No hay usuarios registrados aún.

# Creamos dos usuarios de prueba
usuario1 = UsuarioGaleria(1, "Gema Vadillo", "gema.vadillo@artesena.com",
                           "+34 612 34 56 78", "clave123")
usuario2 = UsuarioGaleria(2, "Frida Kahlo", "arti.wordf_amous@artesena.com",
                           "+52 55 1234 5678", "clave456")

# CREATE
print(gestor.crear_usuario(usuario1))   # ✅ Usuario 'Gema Vadillo' registrado...
print(gestor.crear_usuario(usuario2))   # ✅ Usuario 'Frida Kahlo' registrado...
print(gestor.crear_usuario(usuario1))   # ❌ Ya existe un usuario con id_usuario=1.

# READ
print(gestor.ver_usuario(1))            # ID: 1 | Nombre: Gema Vadillo | ...
print(gestor.listar_usuarios())         # lista de ambos usuarios

# UPDATE
print(gestor.actualizar_usuario(1, nuevo_nombre="Gema Vadillo Pro"))
print(gestor.ver_usuario(1))            # nombre actualizado

# DELETE
print(gestor.eliminar_usuario(2))       # ✅ Usuario 'Frida Kahlo' eliminado...
print(gestor.listar_usuarios())         # solo queda Gema 

# ----------------------------------------------------------------------------------
print("\n") #3
# ----------------------------------------------------------------------------------
# Creamos un Cliente — observa que automáticamente tiene id_usuario,
# nombre, correo, telefono y contraseña, sin que Cliente los haya
# vuelto a definir (eso es HERENCIA en acción)
cliente1 = Cliente(
    id_usuario=10,
    nombre="Andrea Gómez",
    correo="andrea.gomez@correo.com",
    telefono="+57 311 222 3344",
    contraseña="clienteSeguro1",
    presupuesto=500000.0
)

print(cliente1.nombre)                    # Andrea Gómez (heredado)
print(cliente1.verificarContraseña("clienteSeguro1"))  # True (heredado)
print(cliente1.mostrarPanel())            # Panel propio de Cliente (polimorfismo)

# Lo registramos también en el gestor, para confirmar que GestorGaleria
# funciona igual de bien con una subclase (esto es polimorfismo aplicado
# desde el lado del gestor)
print(gestor.crear_usuario(cliente1))
print(gestor.ver_usuario(10))

# ----------------------------------------------------------------------------------
print("\n") #4
# ----------------------------------------------------------------------------------

gema = Artista(
    id_usuario=1,
    nombre="Gema Vadillo",
    correo="gema.vadillo@artesena.com",
    telefono="+34 612 34 56 78",
    contraseña="segura2026",
    portafolio_url="instagram.com/gemavadillo",
    ubicacion_stand="Stand Alley #4 - Comic Con Madrid"
)

print(gema.nombre)                  # Gema Vadillo (heredado)
print(gema.ubicacion_stand)         # Stand Alley #4 - Comic Con Madrid (lectura permitida)
print(gema.actualizarStand("Stand B2 - Festival Celsius 232"))  # único modo de cambiarlo

print(gema.mostrarPanel())          # panel propio de Artista (polimorfismo)

# Confirmamos que ubicacion_stand NO se puede sobrescribir directamente:
try:
    gema.ubicacion_stand = "Intento directo"  # esto debe fallar
except AttributeError as e:
    print(f"❌ Como se esperaba, esto falla: {e}")

# Registramos a Gema también en el gestor
print(gestor.crear_usuario(gema))
print(gestor.listar_usuarios())     # ahora muestra Cliente Y Artista juntos