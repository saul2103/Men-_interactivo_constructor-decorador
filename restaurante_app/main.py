from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

#Menu principal
def mostrar_menu():
    print("\n" + "=" * 40)
    print("    RESTAURANTE RECETAS DE MI SIERRA")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("-" * 40)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("-" * 40)
    print("7. Salir")
    print("=" * 40)

#Funciones para registrar, listar y buscar productos y clientes, incluyendo manejo de errores y validaciones de entrada.
def registrar_producto(restaurante):
    try:
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría del producto: ")
        precio = float(input("Precio del producto: "))
        disponible = input("¿Está disponible? (s/n): ").lower() == 's'
        
        producto = Producto(nombre, categoria, precio, disponible)
        restaurante.registrar_producto(producto)
        print("Producto registrado exitosamente.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def listar_productos(restaurante):
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    
    print("\n--- LISTA DE PRODUCTOS ---")
    for contador, producto in enumerate(productos, 1):
        print(f"{contador}. {producto.mostrar_informacion()}")

def buscar_producto(restaurante):
    nombre = input("Ingrese el nombre del producto a buscar: ")
    resultados = restaurante.buscar_producto(nombre)
    
    if not resultados:
        print("No se encontraron productos con ese nombre.")
        return
    
    print(f"\n--- RESULTADOS DE BÚSQUEDA ({len(resultados)} encontrados) ---")
    for contador, producto in enumerate(resultados, 1):
        print(f"{contador}. {producto.mostrar_informacion()}")

def registrar_cliente(restaurante):
    try:
        nombre = input("Nombre del cliente: ")
        correo = input("Correo electrónico: ")
        id_cliente = input("ID del cliente: ")
        
        cliente = Cliente(nombre, correo, id_cliente)
        restaurante.registrar_cliente(cliente)
        print("Cliente registrado exitosamente.")
    except Exception as e:
        print(f"Error: {e}")

def listar_clientes(restaurante):
    clientes = restaurante.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.")
        return
    
    print("\n--- LISTA DE CLIENTES ---")
    for contador, cliente in enumerate(clientes, 1):
        print(f"{contador}. {cliente.mostrar_informacion()}")

def buscar_cliente(restaurante):
    criterio = input("Ingrese nombre, correo o ID del cliente a buscar: ")
    resultados = restaurante.buscar_cliente(criterio)
    
    if not resultados:
        print("No se encontraron clientes con ese criterio.")
        return
    
    print(f"\n--- RESULTADOS DE BÚSQUEDA ({len(resultados)} encontrados) ---")
    for contador, cliente in enumerate(resultados, 1):
        print(f"{contador}. {cliente.mostrar_informacion()}")

def main():
    restaurante = Restaurante()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            listar_productos(restaurante)
        elif opcion == "3":
            buscar_producto(restaurante)
        elif opcion == "4":
            registrar_cliente(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            buscar_cliente(restaurante)
        elif opcion == "7":
            print("Gracias por usar el sistema")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")

if __name__ == "__main__":
    main()