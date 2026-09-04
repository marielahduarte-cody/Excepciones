from entradas import cantidadproducto, edad_registro, entrada_consecutiva, nota, precioproducto
from estructura import diccionario_empleados, inventario, menu_opciones
from excepciones import divisionsegura
from operaciones import calculo_comision, conversion_moneda, descuento, promedioventas, tipos_incompatibles
from recursos import archivo, importacion_controlada


def mostrar_menu():
    print("\n========== MENU DE EXCEPCIONES ==========")
    print("1. Registrar precio de producto")
    print("2. Registrar cantidad de producto")
    print("3. Validar calificacion")
    print("4. Registrar edad")
    print("5. Registrar nombre, edad y salario")
    print("6. Consultar inventario")
    print("7. Consultar empleado")
    print("8. Menu de opciones")
    print("9. Calcular promedio de ventas")
    print("10. Calcular descuento")
    print("11. Convertir moneda")
    print("12. Corregir tipos incompatibles")
    print("13. Calcular comision")
    print("14. Division segura")
    print("15. Leer archivo de reportes")
    print("16. Controlar importacion")
    print("0. Salir")


def main():
    opciones = {
        "1": precioproducto, "2": cantidadproducto, "3": nota,
        "4": edad_registro, "5": entrada_consecutiva, "6": inventario,
        "7": diccionario_empleados, "8": menu_opciones, "9": promedioventas,
        "10": descuento, "11": conversion_moneda, "12": tipos_incompatibles,
        "13": calculo_comision, "14": divisionsegura, "15": archivo,
        "16": importacion_controlada,
    }
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()
        if opcion == "0":
            print("Programa finalizado.")
            break
        funcion = opciones.get(opcion)
        if funcion is None:
            print("Opcion no valida.")
            continue
        funcion()
        input("\nPresiona Enter para volver al menu...")


if __name__ == "__main__":
    main()