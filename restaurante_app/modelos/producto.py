class Producto:
    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value or not value.strip():
            raise ValueError("El nombre del producto no puede estar vacío")
        self._nombre = value.strip()

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        if not value or not value.strip():
            raise ValueError("La categoría del producto no puede estar vacía")
        self._categoria = value.strip()

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        if value <= 0:
            raise ValueError("El precio del producto debe ser mayor que cero")
        self._precio = float(value)

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, value):
        self._disponible = bool(value)

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Producto: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f} | Estado: {estado}"