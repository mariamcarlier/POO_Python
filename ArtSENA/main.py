# ← Mi punto de entrada para probar todo junto, ya que mi metodo en polimorfismo es mostrarpanel
from models.UsuariosGaleria import UsuarioGaleria

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
print(usuario_prueba.mostrarPanel())       # Panel genérico de usuario
