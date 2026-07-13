from dataclasses import dataclass

@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str

    def mostrar_informacion(self):
        return f"Cliente: {self.nombre} | Correo: {self.correo} | ID: {self.id_cliente}"