from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        self._productos = []
        self._clientes = []

    def registrar_producto(self, producto: Producto):
        if not isinstance(producto, Producto):
            raise TypeError("El objeto debe ser de tipo Producto")
        self._productos.append(producto)

    def listar_productos(self):
        return self._productos.copy()

    def buscar_producto(self, nombre: str):
        return [p for p in self._productos if nombre.lower() in p.nombre.lower()]

    def registrar_cliente(self, cliente: Cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("El objeto debe ser de tipo Cliente")
        self._clientes.append(cliente)

    def listar_clientes(self):
        return self._clientes.copy()

    #Busqueda de cliente de manera flexible permitiendo buscar por nombre, correo o ID ademas de crear una lista vacia para almacenar los resultados de la busqueda y recorrer la lista de clientes para verificar si el criterio de busqueda coincide con alguno de los atributos del cliente, si coincide se agrega a la lista de resultados y finalmente se retorna la lista de resultados.
    
    def buscar_cliente(self, criterio: str):
        resultados = []
        for c in self._clientes:
            if (criterio.lower() in c.nombre.lower() or 
                criterio.lower() in c.id_cliente.lower() or 
                criterio.lower() in c.correo.lower()):
                resultados.append(c)
        return resultados