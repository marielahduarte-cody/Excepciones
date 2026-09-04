def inventario():
    #Crea una lista de productos y solicita una posición. 
    # Controla IndexError y ValueError con mensajes diferentes.
    
    inventario = ["Laptop", "Teclado", "Mouse", "Monitor", "Impresora"]

    print(f"Productos disponibles en inventario: {len(inventario)} (índices del 0 al {len(inventario)-1})")

    try:
        posicion = int(input("Introduce el índice del producto a consultar: "))

        producto = inventario[posicion]
        print(f"Producto en la posición {posicion}: {producto}")

    except ValueError:
        print("Error de formato: Debes ingresar un número entero válido para la posición.")

    except IndexError:
        print(f"Error de rango: El índice introducido no existe. Elige entre 0 y {len(inventario)-1}.")
        
    inventario()
    
def diccionario_empleados():
    #Consulta información de un empleado mediante una clave. 
    # Controla KeyError y considera si get() podría ser una alternativa.
    
    empleados = {
        "001": {"nombre": "Juan", "departamento": "Ventas"},
        "002": {"nombre": "María", "departamento": "Marketing"},
        "003": {"nombre": "Pedro", "departamento": "IT"}
    }

    try:
        clave = input("Introduce la clave del empleado a consultar: ")
        empleado = empleados[clave]
        print(f"Información del empleado {clave}: {empleado['nombre']}, {empleado['departamento']}")
    except KeyError:
        print(f"Error: La clave '{clave}' no existe en el diccionario de empleados.")
    
    diccionario_empleados()
    
def menu_opciones():
    #Solicita una opción numérica para un menú. Controla ValueError y usa else para
    #ejecutar la lógica solamente cuando la conversión haya sido exitosa.
    
    print("--- MENÚ PRINCIPAL ---")
    print("1. Ver perfil")
    print("2. Editar datos")
    print("3. Salir")

    try:
        opcion = int(input("Selecciona una opción (1-3): "))

    except ValueError:
        print("Error de formato: La opción ingresada debe ser un número entero.")

    else:
        if opcion == 1:
            print("Cargando perfil del usuario...")
        elif opcion == 2:
            print("Abriendo panel de edición...")
        elif opcion == 3:
            print("Saliendo del sistema...")
        else:
            print("Opción no válida: Por favor selecciona un número entre 1 y 3.")