# ← clase independiente (asociación, no herencia)
"""
Módulo: obra_arte.py
Proyecto: ArtSENA - Plataforma de Comercio y Exposición de Arte Digital

Este archivo contiene la clase ObraArte, una clase INDEPENDIENTE que
NO hereda de UsuarioGaleria.

Decisión de diseño importante:
    ObraArte NO es un tipo de usuario, es una entidad del catálogo
    de la galería. Su relación con Artista es de COMPOSICIÓN:
        - Un Artista TIENE una lista de ObraArte (obras_publicadas).
        - Una ObraArte PERTENECE a un Artista.
    En UML esto se representa con una línea de asociación o composición,
    nunca con una flecha de herencia, que fue el error identificado
    en la revisión del diagrama.

Pilares de POO aplicados en este archivo:
    - ABSTRACCIÓN: se modela solo lo que ArtSENA necesita de una
      obra real (titulo, autor, precio, tecnica, anio, dimensiones,
      disponibilidad, fecha_registro). Se ignoran detalles irrelevantes
      para el sistema (como la inspiración del artista o el tiempo
      que tardó en crearla).
    - ENCAPSULAMIENTO: precio se protege con un guion bajo para
      que no pueda modificarse libremente (una obra no debería
      cambiar de precio sin pasar por un método explícito).
"""

from datetime import date


class ObraArte:
    """
    Representa una obra de arte dentro del catálogo de ArtSENA.
    Puede ser de cualquier tipo: pintura, escultura, obra digital, etc.

    Atributos:
        id_obra (int): identificador único de la obra. Público.
        titulo (str): nombre de la obra. Público.
        autor (str): nombre del artista creador. Público.
        _precio (float): valor comercial de la obra. PROTEGIDO,
            accesible mediante propiedad de solo lectura; se modifica
            solo a través de actualizarPrecio().
        tecnica (str): técnica usada (ej. 'Óleo', 'Digital', 'Escultura').
            Público.
        anio (int): año de creación. Público.
        dimensiones (str): medidas físicas o digitales de la obra
            (ej. '120x90 cm' o '4K 3840x2160 px'). Público.
        disponibilidad (str): estado actual de la obra. Solo puede
            tomar tres valores: 'Disponible', 'Reservada', 'Vendida'.
            Público porque el sistema necesita consultarlo y cambiarlo
            en el flujo de compra.
        fecha_registro (date): fecha en que la obra fue registrada
            en la plataforma. Se asigna automáticamente al crear el
            objeto, no se recibe como parámetro.
    """

    # Valores válidos para disponibilidad (constante de clase)
    ESTADOS_VALIDOS = ("Disponible", "Reservada", "Vendida")

    def __init__(self, id_obra: int, titulo: str, autor: str,
                 precio: float, tecnica: str, anio: int,
                 dimensiones: str, disponibilidad: str = "Disponible"):
        self.id_obra = id_obra
        self.titulo = titulo
        self.autor = autor
        self._precio = precio
        self.tecnica = tecnica
        self.anio = anio
        self.dimensiones = dimensiones

        # Validamos que el estado inicial sea uno de los tres válidos
        if disponibilidad not in self.ESTADOS_VALIDOS:
            raise ValueError(
                f"Estado inválido: '{disponibilidad}'. "
                f"Usa uno de: {self.ESTADOS_VALIDOS}"
            )
        self.disponibilidad = disponibilidad

        # La fecha de registro se asigna automáticamente al momento
        # de instanciar el objeto, igual que en el diagrama UML.
        self.fecha_registro = date.today()

    # ------------------------------------------------------------------
    # PROPIEDAD DE SOLO LECTURA para precio
    # ------------------------------------------------------------------

    @property
    def precio(self):
        return self._precio

    def actualizarPrecio(self, nuevo_precio: float) -> str:
        """
        Única vía autorizada para modificar el precio de la obra.
        Incluye validación para evitar precios negativos o en cero.

        Args:
            nuevo_precio (float): nuevo valor comercial de la obra.

        Returns:
            str: mensaje de confirmación o de error.
        """
        if nuevo_precio <= 0:
            return "❌ El precio debe ser mayor a cero."
        self._precio = nuevo_precio
        return f"✅ Precio actualizado a: {nuevo_precio}."

    # ------------------------------------------------------------------
    # MÉTODOS PROPIOS DE OBRAARTE
    # ------------------------------------------------------------------

    def verificarDisponibilidad(self) -> str:
        """
        Consulta y describe el estado actual de la obra.

        Returns:
            str: mensaje legible con el estado actual.
        """
        mensajes = {
            "Disponible": f"✅ '{self.titulo}' está disponible para compra.",
            "Reservada":  f"🕐 '{self.titulo}' está reservada actualmente.",
            "Vendida":    f"🔴 '{self.titulo}' ya fue vendida."
        }
        return mensajes[self.disponibilidad]

    def mostrarPanel(self) -> str:
        """
        Muestra la ficha completa de la obra, tal como aparecería
        en el catálogo público de ArtSENA.

        Nota: aunque ObraArte no hereda de UsuarioGaleria y no
        participa en el polimorfismo principal del sistema de login,
        sí implementa mostrarPanel() como buena práctica de diseño
        uniforme: cualquier entidad del sistema que tenga una "vista
        pública" expone ese comportamiento con el mismo nombre.

        Returns:
            str: ficha completa de la obra.
        """
        return (
            f"🖼️  ══════════════════════════════\n"
            f"   {self.titulo.upper()}\n"
            f"   ══════════════════════════════\n"
            f"   Autor       : {self.autor}\n"
            f"   Técnica     : {self.tecnica}\n"
            f"   Año         : {self.anio}\n"
            f"   Dimensiones : {self.dimensiones}\n"
            f"   Precio      : ${self._precio:,.0f}\n"
            f"   Estado      : {self.disponibilidad}\n"
            f"   Registrada  : {self.fecha_registro}\n"
            f"   ══════════════════════════════"
        )