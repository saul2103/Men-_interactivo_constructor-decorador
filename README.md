# Sistema de Gestión de Restaurante

**Estudiante:** Bryan Saul Iza Llano

## Descripción del Proyecto

Este sistema permite gestionar productos y clientes de un restaurante a través de un menú interactivo en consola. Los usuarios pueden registrar, listar y buscar tanto productos como clientes, aplicando conceptos fundamentales de POO como:

- **Constructores** (`__init__`)
- **Decoradores** (`@property`, `@setter`)
- **Clases de datos** (`@dataclass`)
- **Encapsulación**
- **Arquitectura modular por capas**

---

## Estructura del Proyecto

```text
restaurante_app/
├── modelos/
│ ├── init.py
│ ├── producto.py     # Clase Producto con encapsulamiento estricto
│ └── cliente.py      # Estructura de datos Cliente usando dataclasses
├── servicios/
│ ├── init.py
│ └── restaurante.py  #Controlador de colecciones
└── main.             # Interfaz de usuario por consola
```

### Capas del Sistema

#### **Modelos** (`modelos/`)
- **Producto**: Entidad que representa un producto del restaurante
- **Cliente**: Entidad que representa un cliente registrado

#### **Servicios** (`servicios/`)
- **Restaurante**: Clase de servicio que administra las listas de productos y clientes

#### **Presentación** (`main.py`)
- Punto de entrada del sistema
- Menú interactivo para el usuario

### Menú Principal
```text
========================================
    RESTAURANTE RECETAS DE MI SIERRA
========================================

1. Registrar producto

2. Listar productos

3. Buscar producto

4. Registrar cliente

5. Listar clientes

6. Buscar cliente

7. Salir
```
El archivo `main.py` actúa como el controlador visual de la aplicación. Mediante un ciclo continuo `while True`, despliega un menú estructurado con 7 opciones operativas:

1.  **Registrar producto:** Solicita datos por teclado, valida las reglas de negocio y añade el objeto.
2.  **Listar productos:** Imprime el formato formateado de todos los alimentos y bebidas del menú.
3.  **Buscar producto:** Filtra los registros existentes por coincidencia parcial de texto en el nombre.
4.  **Registrar cliente:** Captura la información básica y el ID único del consumidor.
5.  **Listar clientes:** Muestra el listado completo de usuarios registrados.
6.  **Buscar cliente:** Búsqueda flexible que filtra de forma simultánea por nombre, ID o correo electrónico.
7.  **Salir:** Rompe el ciclo de ejecución y finaliza el programa de manera segura.

El menú maneja excepciones mediante bloques `try/except` para atrapar entradas inválidas (como ingresar letras en el precio) sin que la aplicación se detenga abruptamente.

---

## La Importancia de Crear Objetos a Partir de Datos del Usuario
La interacción con usuarios del mundo real es inherentemente impredecible; las personas suelen introducir datos erróneos, incompletos o con formatos equivocados. Transformar estas entradas crudas en **objetos validados** es la primera línea de defensa de un software robusto. 

Al instanciar una clase que cuenta con mecanismos de validación interna (como los getters y setters del proyecto), garantizamos que la información peligrosa o corrupta sea rechazada en la frontera misma del sistema. Esto previene fallos en cascada en las capas de lógica o de bases de datos. Diseñar aplicaciones bajo este enfoque asegura que el sistema trabaje únicamente con entidades que cumplen con las reglas del negocio, logrando un código tolerante a fallos, predecible y profesional.