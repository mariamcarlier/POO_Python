"""📂Módulo #1 : usuario_galeria.py
Proyecto: ArtSENA - Plataforma de Comercio y Exposición de Arte Digital🎨 🧑🏼‍🎨

Este archivo contiene la clase UsuarioGaleria, que es la CLASE PADRE 🦸🏼‍♂️
(superclase) de todo el sistema de usuarios de ArtSENA.

Pilares de POO aplicados en este archivo:
    - ABSTRACCIÓN: solo se modelan los datos esenciales de cualquier usuario 
    (identidad, contacto, credencial de acceso).
    - ENCAPSULAMIENTO:🛡️ la contraseña se protege con doble guion bajo (__)
      y solo se puede leer o modificar a través de métodos controlados.
"""

class UsuarioGaleria:
    def __init__(self, id_usuario: int, nombre: str, correo: str,
                 telefono: str, contraseña: str):
        # Atributo público: se expone sin restricción
        self.id_usuario = id_usuario

        # Atributos protegidos (un solo guion bajo): visibles para esta
        # clase y para las subclases que hereden de ella, pero no
        # pensados para ser modificados libremente desde fuera.
        self._nombre = nombre
        self._correo = correo
        self._telefono = telefono

        # Atributo privado (doble guion bajo): ENCAPSULAMIENTO real. Python aplica
        # "name mangling" = (alteración de nombres) a este atributo, dificultando
        # el acceso accidental desde fuera de la clase. (evitar que se sobrescriban por accidente en subclases).
        self.__contraseña = contraseña

    # ------------------------------------------------------------------
    # PROPIEDADES DE SOLO LECTURA (getters)
    # ------------------------------------------------------------------
    # Usamos @property para exponer nombre, correo y telefono de forma controlada y legible
    #  (usuario.nombre en vez de usuario.get_nombre()), manteniendo el principio de encapsulamiento🛡️: 
    # quien usa la clase puede LEER estos datos, pero no sobrescribirlos directamente
    #  desde fuera sin pasar por un método explícito.

    @property # es un decorador 
    def nombre(self):
        return self._nombre

    @property
    def correo(self):
        return self._correo

    @property
    def telefono(self):
        return self._telefono

    # ------------------------------------------------------------------
    # MÉTODOS DE SEGURIDAD (manejo de la contraseña)
    # ------------------------------------------------------------------

    def encriptarContraseña(self): # Simula la encriptación de la contraseña actual del usuario.
        """
        En un sistema real, aquí se usaría una librería de hashing como bcrypt o hashlib.
          📚Para fines educativos del ejercicio,se simula anteponiendo un prefijo "hash_" a la contraseña..
        """
        self.__contraseña = f"hash_{self.__contraseña}"
        return self.__contraseña
    #🔁Retorna: -> str: la contraseña "encriptada"

    def verificarContraseña(self, clave_ingresada: str) -> bool:
        """
        Compara la clave ingresada por el usuario contra la contraseña
        almacenada internamente. Es el único método público autorizado
        para consultar si una clave es correcta.

        👍🏼Args:   clave_ingresada (str):= la contraseña que el usuario escribió al intentar iniciar sesión.

        🔁Retorna:-> bool: True si coincide, False si no.
        """
        return self.__contraseña == clave_ingresada

    def cambiarContraseña(self, clave_actual: str, clave_nueva: str) -> str:
        """Cambia la contraseña del usuario, pero SOLO si primero se demuestra conocer la contraseña actual. 
        Esta validación interna reemplaza la necesidad de un método separado de "validar",
        manteniendo el código más simple sin perder el principio de encapsulamiento:
         el atributo __contraseña nunca se modifica sin pasar por esta verificación.

        👍🏼Args:   clave_actual (str): la contraseña vigente, para confirmar que quien hace el cambio tiene autorización.🔐🔓
                    clave_nueva (str): la nueva contraseña a establecer.
            
        🔁Retorna: -> str: mensaje de éxito o de error.
        """
        if self.verificarContraseña(clave_actual):
            self.__contraseña = clave_nueva
            return "✅ Contraseña actualizada correctamente."
        return "❌ La contraseña actual no coincide. No se realizó el cambio."

    # ------------------------------------------------------------------
    # MÉTODO POLIMÓRFICO
    # ------------------------------------------------------------------

    def mostrarPanel(self) -> str:
        """
        Método base que será SOBRESCRITO por cada subclase (Cliente, Artista, AdministradorGaleria).
          Esta es la base del PILAR DE 👻POLIMORFISMO: el sistema llamará a este mismo nombre de método 
          sobre cualquier objeto, y cada uno responderá de forma distinta según su propia implementación.

        🔁Retorna: -> str: texto del panel genérico (las subclases lo cambian).
        """
        return "Panel genérico de usuario"