# Este archivo contiene la clase Cliente, una SUBCLASE de UsuarioGaleria.
"""  📂Módulo #2 -Cliente      Pilares de POO aplicados en este archivo:
    - HERENCIA: Cliente extiende de UsuarioGaleria, reutilizando
      id_usuario, nombre, correo, telefono y toda la lógica de contraseña sin volver a escribirla.

    - POLIMORFISMO: Cliente sobrescribe mostrarPanel() con su propia versión, distinta a la de Artista y AdministradorGaleria."""

from models.UsuariosGaleria import UsuarioGaleria

class Cliente(UsuarioGaleria):

    """ Representa a un comprador dentro de la plataforma ArtSENA: una
    persona que navega el catálogo de obras, las agrega a un carrito
    y realiza compras.

    Atributos propios (no existen en UsuarioGaleria):
        carritoCompras (list): lista de obras que el cliente ha agregado para comprar.
          + Pública, porque la interfaz de usuario necesita poder mostrar su contenido en cualquier momento.
            
            presupuesto (float): monto disponible que el cliente tiene para gastar en la plataforma.
             + Pública por la misma razón.
    """

    def __init__(self, id_usuario: int, nombre: str, correo: str,
                 telefono: str, contraseña: str, presupuesto: float = 0.0):
        # super().__init__() llama al constructor de UsuarioGaleria, encargándose de id_usuario, nombre, correo, telefono y __contraseña SIN tener que volver a escribir esa lógica aquí.
        # Esto es la esencia de la HERENCIA: reutilización de código.
        super().__init__(id_usuario, nombre, correo, telefono, contraseña)

        # Atributos exclusivos de Cliente
        self.carritoCompras = []
        self.presupuesto = presupuesto

    # ------------------------------------------------------------------
    # MÉTODOS PROPIOS DE CLIENTE 
    # ------------------------------------------------------------------
    #   1.Agregar una obra de arte al carrito de compras del cliente.
    def agregarAlCarrito(self, obra) -> str:

        self.carritoCompras.append(obra)
        return f"🛒 Obra agregada al carrito. Total en carrito: {len(self.carritoCompras)}."
        #🔁Retorna : ->str: mensaje de confirmación

    #2. Realizar la compra de una obra específica, validando que el cliente tenga presupuesto suficiente.
    def comprarObra(self, obra) -> str:

        # obra: objeto ObraArte con un atributo .precio.
        if obra.precio > self.presupuesto:
            return (f"❌ Presupuesto insuficiente. Precio: {obra.precio}, "
                    f"disponible: {self.presupuesto}.")

        self.presupuesto -= obra.precio
        if obra in self.carritoCompras:
            self.carritoCompras.remove(obra)

        return (f"✅ Compra realizada: '{obra.titulo}' por {obra.precio}. "
                f"Presupuesto restante: {self.presupuesto}.")
#🔁Retorna : ->str: éxito o de error según el presupuesto.

    # ------------------------------------------------------------------
    # POLIMORFISMO: sobrescritura de mostrarPanel()
    # ------------------------------------------------------------------

    def mostrarPanel(self) -> str:

        return (f"🛍️ Panel Cliente | {self.nombre}\n"
                f"Presupuesto disponible: {self.presupuesto}\n"
                f"Obras en carrito: {len(self.carritoCompras)}")

"""
        Sobrescribe el método de UsuarioGaleria. Cuando el sistema
        ejecute usuario.mostrarPanel() sobre un objeto Cliente,
        esta es la versión que se ejecutará (en vez de la genérica
        del padre), gracias al polimorfismo.

        Returns:
            str: panel personalizado para el rol Cliente."""