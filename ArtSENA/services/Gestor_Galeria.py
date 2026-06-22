from models.UsuariosGaleria import UsuarioGaleria

class GestorGaleria: # Administra el conjunto de usuarios registrados en ArtSENA.
    """
    Esta clase NO hereda de UsuarioGaleria, porque un gestor no ES un usuario 🧠;
      un gestor TIENE una colección de usuarios. Esta relación se llama "composición" o "agregación" ➕ ,
      y es distinta de la herencia que usaremos más adelante para Cliente, Artista y AdministradorGaleria.

    Atributos:
    __usuarios (list): lista privada que almacena los objetos UsuarioGaleria (o de sus subclases) registrados.
          Es privada porque no queremos que código externo manipulela lista directamente 
          (por ejemplo, agregando un usuario sin pasar por las validaciones de crear_usuario()).
    """

    def __init__(self):
        # Lista privada: encapsulamiento aplicado a la colección completa,
        # no solo a un atributo individual.
        self.__usuarios = []

    # ------------------------------------------------------------------
    # CREATE
    # ------------------------------------------------------------------
    def crear_usuario(self, usuario: UsuarioGaleria) -> str:
        """  Registra un nuevo usuario en el sistema.

        👍🏼Args: usuario (UsuarioGaleria): instancia de UsuarioGaleria o de cualquiera de sus subclases
                 (Cliente, Artista, AdministradorGaleria). 
            
        🔁Retorna:- > str: mensaje de confirmación.
        """
        # Validación simple: evitar registrar el mismo id_usuario dos veces.
        if self._buscar_por_id(usuario.id_usuario) is not None:
            return f"❌ Ya existe un usuario con id_usuario={usuario.id_usuario}."

        self.__usuarios.append(usuario)
        return f"✅ Usuario '{usuario.nombre}' registrado en el sistema."

    # ------------------------------------------------------------------
    # READ
    # ------------------------------------------------------------------
    def ver_usuario(self, id_usuario: int) -> str: # id_usuario (int): identificador del usuario a consultar
        # Consulta y muestra la información básica de un usuario por su id.
      
        usuario = self._buscar_por_id(id_usuario)
        if usuario is None:
            return f"❌ No existe un usuario con id_usuario={id_usuario}."
        return (f"ID: {usuario.id_usuario} | Nombre: {usuario.nombre} "
                f"| Correo: {usuario.correo} | Tipo: {type(usuario).__name__}")
        #🔁 Retorna: -> str: información del usuario o mensaje de error si no existe.

    def listar_usuarios(self) -> str:   # Muestra un resumen de todos los usuarios registrados.

        if not self.__usuarios:
            return "📭 No hay usuarios registrados aún."

        resumen = "📋 Usuarios registrados en ArtSENA:\n"
        for usuario in self.__usuarios:
            resumen += (f"  - [{type(usuario).__name__}] "
                        f"ID {usuario.id_usuario}: {usuario.nombre}\n")
        return resumen.strip()         
    #🔁Retorna: -> str: lista formateada de todos los usuarios, o mensaje indicando que la lista está vacía.

    # ------------------------------------------------------------------
    # UPDATE
    # ------------------------------------------------------------------
    def actualizar_usuario(self, id_usuario: int, nuevo_nombre: str = None,
                            nuevo_correo: str = None) -> str:
        """ 👍🏼 Args:
            id_usuario (int): identificador del usuario a actualizar.
            nuevo_nombre (str, opcional): nuevo nombre, si se desea cambiar.
            nuevo_correo (str, opcional): nuevo correo, si se desea cambiar.
        """
        usuario = self._buscar_por_id(id_usuario)
        if usuario is None:
            return f"❌ No existe un usuario con id_usuario={id_usuario}." #🔁

        if nuevo_nombre:
            usuario._nombre = nuevo_nombre
        if nuevo_correo:
            usuario._correo = nuevo_correo

        return f"✅ Usuario {id_usuario} actualizado correctamente." #🔁
        #🔁 Retorna un mensaje de confirmacion o error

    # ------------------------------------------------------------------
    # DELETE = Elimina un usuario del sistema por su id.
    # ------------------------------------------------------------------

    def eliminar_usuario(self, id_usuario: int) -> str:
        usuario = self._buscar_por_id(id_usuario)
        if usuario is None:
            return f"❌ No existe un usuario con id_usuario={id_usuario}."

        self.__usuarios.remove(usuario)
        return f"✅ Usuario '{usuario.nombre}' eliminado del sistema."

    # --------------------------------------------------------------------------
    # MÉTODO AUXILIAR PRIVADO ⭐Busca internamente un usuario por su id_usuario.
    # --------------------------------------------------------------------------
    def _buscar_por_id(self, id_usuario: int): # -> identificador a buscar

        for usuario in self.__usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None
    #🔁Retorna : -> UsuarioGaleria | None: el objeto encontrado o None.