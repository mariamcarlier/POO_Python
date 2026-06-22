# ← Mi punto de entrada para probar todo junto, ya que mi metodo en polimorfismo es mostrarpanel
"""from models.UsuariosGaleria import UsuarioGaleria

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

from models.UsuariosGaleria import UsuarioGaleria
from services.Gestor_Galeria import GestorGaleria

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