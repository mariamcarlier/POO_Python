#from models.UsuariosGaleria import UsuarioGaleria
from models.Cliente import Cliente
from models.Artista import Artista
from models.Administrador_Galeria import AdministradorGaleria
from models.Obra_Arte import ObraArte
from services.Gestor_Galeria import GestorGaleria

"""# #1. Instanciamos un usuario base (en la práctica nunca se usa
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

print("\n" + "="*50)
print("  ArtSENA — PRUEBA INTEGRAL DEL SISTEMA")
print("="*50)

# ── INSTANCIAMOS USUARIOS ─────────────────────────
gestor = GestorGaleria()

gema = Artista(
    id_usuario=1,
    nombre="Gema Vadillo",
    correo="gema.vadillo@artesena.com",
    telefono="+34 612 34 56 78",
    contraseña="segura2026",
    portafolio_url="instagram.com/gemavadillo",
    ubicacion_stand="Stand Alley #4 - Comic Con Madrid"
)

cliente1 = Cliente(
    id_usuario=10,
    nombre="Andrea Gómez",
    correo="andrea.gomez@correo.com",
    telefono="+57 311 222 3344",
    contraseña="clienteSeguro1",
    presupuesto=6000000.0
)

admin1 = AdministradorGaleria(
    id_usuario=99,
    nombre="Mariam Carlier Alvarado",
    correo="mariam00estudio@gmail.com",
    telefono="+57 300 123456",
    contraseña="super_aprendiz22",
    modulo_asignado="Moderación de obras",
    nivel_acceso=3
)

# Registramos todos en el gestor
print(gestor.crear_usuario(gema))
print(gestor.crear_usuario(cliente1))
print(gestor.crear_usuario(admin1))
print(gestor.listar_usuarios())

# ── FLUJO DE OBRA ─────────────────────────────────
print("\n--- ARTISTA SUBE UNA OBRA ---")
obra1 = ObraArte(
    id_obra=1024,
    titulo="Noche Estrellada sobre el Sogamoso",
    autor="Gema Vadillo",
    precio=4500000.0,
    tecnica="Óleo",
    anio=2026,
    dimensiones="120x90 cm"
)
print(obra1.mostrarPanel())
print(gema.subirObra(obra1))

# ── ADMINISTRADOR APRUEBA ─────────────────────────
print("\n--- ADMIN APRUEBA LA PUBLICACIÓN ---")
print(admin1.aprobarPublicacionObra(obra1))
print(obra1.verificarDisponibilidad())

# ── CLIENTE COMPRA ────────────────────────────────
print("\n--- CLIENTE AGREGA AL CARRITO Y COMPRA ---")
print(cliente1.agregarAlCarrito(obra1))
print(cliente1.comprarObra(obra1))
print(gema.registrarVenta(obra1))
print(gema.verMisVentas())

# ── POLIMORFISMO EN ACCIÓN ────────────────────────
print("\n--- POLIMORFISMO: misma orden, 3 comportamientos distintos ---")
for usuario in [cliente1, gema, admin1]:
    print(usuario.mostrarPanel())
    print("-" * 40)