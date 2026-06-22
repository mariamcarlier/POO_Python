"""
Módulo: administrador_galeria.py
Proyecto: ArtSENA - Plataforma de Comercio y Exposición de Arte Digital

Este archivo contiene la clase AdministradorGaleria, una SUBCLASE de
UsuarioGaleria.

Pilares de POO aplicados en este archivo:
    - HERENCIA: AdministradorGaleria extiende de UsuarioGaleria,
      igual que Cliente y Artista.
    - ENCAPSULAMIENTO: nivel_acceso se protege con un guion bajo,
      ya que representa un dato sensible de seguridad que no debería
      modificarse libremente desde fuera de la clase.
    - POLIMORFISMO: AdministradorGaleria sobrescribe mostrarPanel()
      con su propia versión, mostrando el control total del sistema.
"""

from models.UsuariosGaleria import UsuarioGaleria

class AdministradorGaleria(UsuarioGaleria):


    def __init__(self, id_usuario: int, nombre: str, correo: str,
                 telefono: str, contraseña: str, modulo_asignado: str,
                 nivel_acceso: int = 1):
        # HERENCIA: reutilizamos toda la lógica de UsuarioGaleria
        super().__init__(id_usuario, nombre, correo, telefono, contraseña)

        # Atributos exclusivos de AdministradorGaleria
        self.modulo_asignado = modulo_asignado
        self._nivel_acceso = nivel_acceso

    """
    Representa al rol de gobernanza de la plataforma ArtSENA: la
    persona encargada de aprobar publicaciones, gestionar comisiones
    y supervisar el funcionamiento general del sistema.

    Atributos propios (no existen en UsuarioGaleria):
        _nivel_acceso (int): nivel de privilegios del administrador
            (por ejemplo, 1 = soporte básico, 2 = supervisor,
            3 = administrador total). PROTEGIDO, porque modificarlo
            sin control podría otorgar permisos indebidos; solo se
            cambia a través de un método explícito.
        modulo_asignado (str): área específica de la plataforma que
            este administrador supervisa (por ejemplo, "Moderación
            de obras" o "Finanzas"). Pública, ya que es información
            organizativa visible en el panel.
    """
    # ------------------------------------------------------------------
    # PROPIEDAD DE SOLO LECTURA para nivel_acceso
    # ------------------------------------------------------------------

    @property
    def nivel_acceso(self):
        return self._nivel_acceso

    # ------------------------------------------------------------------
    # MÉTODOS PROPIOS DE ADMINISTRADORGALERIA -  Aprueba la publicación de una obra, cambiando su disponibilidad
           #a visible para el público en general
    # ------------------------------------------------------------------
    def aprobarPublicacionObra(self, obra) -> str: # obra: objeto ObraArte a aprobar.
       
        obra.disponibilidad = "Disponible"
        return f"✅ Obra '{obra.titulo}' aprobada y publicada en la galería."


    def modificarComisiones(self, nuevo_porcentaje: float) -> str:
        #Simula la modificación del porcentaje de comisión que la plataforma cobra por cada venta realizada.

        return f"⚙️ Comisión de la plataforma actualizada a {nuevo_porcentaje * 100}%."

    def gestionarUsuarios(self, gestor, accion: str, id_usuario: int) -> str:
        """
        Permite al administrador ejecutar acciones sobre la colección
        de usuarios, delegando en GestorGaleria. Este método demuestra
        cómo AdministradorGaleria puede colaborar con la clase de
        servicio sin tener que reimplementar su lógica.

        Args:
            gestor (GestorGaleria): instancia del gestor del sistema.
            accion (str): "ver" o "eliminar".
            id_usuario (int): identificador del usuario sobre el que
                se ejecuta la acción.
        """
        if self._nivel_acceso < 2:
            return "⛔ No tienes el nivel de acceso suficiente para esta acción."

        if accion == "ver":
            return gestor.ver_usuario(id_usuario)
        elif accion == "eliminar":
            return gestor.eliminar_usuario(id_usuario)
        else:
            return "❌ Acción no reconocida. Usa 'ver' o 'eliminar'."

    def verReportes(self, gestor) -> str: # gestor (GestorGaleria): instancia del gestor del sistema.

        return f"📊 Reporte general:\n{gestor.listar_usuarios()}"

    # ------------------------------------------------------------------
    # POLIMORFISMO: sobrescritura de mostrarPanel()
    # ------------------------------------------------------------------
    def mostrarPanel(self) -> str:

        return (f"🛡️ Panel Administrador | {self.nombre}\n"
                f"Módulo asignado: {self.modulo_asignado}\n"
                f"Nivel de acceso: {self.nivel_acceso}\n"
                f"Control total del sistema")
    #retorna un panel personalizado para el rol Administrador