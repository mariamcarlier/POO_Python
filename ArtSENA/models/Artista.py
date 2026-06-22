"""📂Módulo: artista.py

            Pilares de POO aplicados en este archivo:
    - HERENCIA: Artista extiende de UsuarioGaleria, igual que Cliente.
    - ENCAPSULAMIENTO: ubicacion_stand se protege con un guion bajo,
      ya que solo debería modificarse a través de un método controlado
      (actualizarStand), no por asignación directa.
    - POLIMORFISMO: Artista sobrescribe mostrarPanel() con su propia
      versión, mostrando información de portafolio y ventas.
"""

from models.UsuariosGaleria import UsuarioGaleria

class Artista(UsuarioGaleria):

    def __init__(self, id_usuario: int, nombre: str, correo: str,
                 telefono: str, contraseña: str, portafolio_url: str,
                 ubicacion_stand: str):
        # HERENCIA: reutilizamos toda la lógica de UsuarioGaleria
        super().__init__(id_usuario, nombre, correo, telefono, contraseña)

        # Atributos exclusivos de Artista
        self.portafolio_url = portafolio_url
        self._ubicacion_stand = ubicacion_stand
        self.obras_publicadas = []
        self.ventas_realizadas = []

    """
    Representa a un creador de contenido visual dentro de ArtSENA:👩🏼‍🎨👨🏼‍🎨🧑🏼‍🎨
    alguien que publica obras, gestiona su portafolio digital y
    administra su presencia física en eventos (stands).

    Atributos propios (no existen en UsuarioGaleria):
        - portafolio_url (str): enlace a la vitrina digital del artista (su Instagram, su web personal, etc.).
              +  Público, porque forma parte de su perfil visible al público.

        -  _ubicacion_stand (str): ubicación física actual del artista en una convención o feria. 
              # PROTEGIDA (un guion bajo _ ),porque su modificación debería pasar siempre por el
            método actualizarStand(), no por asignación directa, evitando que quede en un estado inconsistente.

        - obras_publicadas (list): lista de objetos ObraArte que el artista ha subido a la plataforma.
              + Pública, ya que el sistema necesita mostrarla en el perfil público.

        - ventas_realizadas (list): historial de ventas del artista.
              + Pública por la misma razón.
    """

    # ------------------------------------------------------------------
    # PROPIEDAD DE SOLO LECTURA para ubicacion_stand
    # ------------------------------------------------------------------
    # AL Igual que con nombre/correo/telefono en UsuarioGaleria:
    # se puede LEER libremente (artista.ubicacion_stand), pero no se
    # puede SOBRESCRIBIR directamente sin pasar por actualizarStand().

    @property
    def ubicacion_stand(self):
        return self._ubicacion_stand

    # ------------------------------------------------------------------
    # MÉTODOS PROPIOS DE ARTISTA
    # ------------------------------------------------------------------
# 1.PublicaR una nueva obra en el portafolio del artista.
    def subirObra(self, obra) -> str: # -> obra: objeto ObraArte a publicar.

        self.obras_publicadas.append(obra)
        return (f"🎨 Obra '{obra.titulo}' publicada exitosamente. "
                f"Total de obras: {len(self.obras_publicadas)}.")
    #🔁Retorna : ->str: mensaje de confirmación.

# 2. Actualiza la ubicación física del stand del artista. 
# Esta es la ÚNICA vía autorizada para modificar _ubicacion_stand,manteniendo el principio de encapsulamiento.🛡️
    def actualizarStand(self, nueva_ubicacion: str) -> str: # ->nueva_ubicacion (str): la nueva ubicación del stand.

        self._ubicacion_stand = nueva_ubicacion
        return f"📍 Stand actualizado a: {nueva_ubicacion}"
    #🔁Retorna : str: mensaje de confirmación.

#3. Muestra un resumen de las ventas realizadas por el artista.
    def verMisVentas(self) -> str:

        if not self.ventas_realizadas:
            return "📭 Aún no tienes ventas registradas."

        total = sum(venta.precio for venta in self.ventas_realizadas)
        return (f"💰 Tienes {len(self.ventas_realizadas)} venta(s) "
                f"realizadas. Total acumulado: {total}.")
    #🔁Retorna :str: resumen de ventas o mensaje indicando que no hay
    #               ventas registradas aún.

# -----------------------------------------------------------------------------------------
# 4. RegistraR una obra como vendida✅, moviéndola de obras_publicadas a ventas_realizadas.
#  Este método lo invocará típicamente el flujo de compra del Cliente.
    def registrarVenta(self, obra) -> str: # obra: objeto ObraArte que fue vendida.

        if obra in self.obras_publicadas:
            self.ventas_realizadas.append(obra)
            return f"✅ Venta registrada: '{obra.titulo}'."
        return "❌ Esta obra no pertenece al portafolio de este artista."
    #🔁Retorna :str: mensaje de confirmación.

    # ------------------------------------------------------------------
    # POLIMORFISMO: sobrescritura de mostrarPanel()
    # ------------------------------------------------------------------

    # 1.MOSTRAR PANEL - Cumple la funcion de Sobrescribir el método de UsuarioGaleria con la vista específica del rol Artista.
    def mostrarPanel(self) -> str:

        return (f"🖌️ Panel Artista | {self.nombre}\n"
                f"Portafolio: {self.portafolio_url}\n"
                f"Stand actual: {self.ubicacion_stand}\n"
                f"Obras publicadas: {len(self.obras_publicadas)}\n"
                f"Ventas realizadas: {len(self.ventas_realizadas)}")
        #🔁Retorna str: panel personalizado para el rol Artista.