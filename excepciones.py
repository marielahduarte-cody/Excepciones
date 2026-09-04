def divisionsegura():
    try:
        dividendo = float(input("Dividendo: "))
        divisor = float(input("Divisor: "))
        resultado = dividendo / divisor

    except ValueError:
        print("Error: ingrese valores numericos.")

    except ZeroDivisionError:
        print("Error: el divisor no puede ser cero.")

    else:
        print("Resultado:", resultado)

    finally:
        print("Operacion finalizada.")
    
    divisionsegura()
    
    def abrirArchivo():
        try:
            archivo = open("ventas.txt", "r", encoding="utf-8")
            contenido = archivo.read()
        except FileNotFoundError:
            print("No se encontró el archivo de ventas.")
        else:
            print(contenido)
        finally:
            print("Consulta terminada.")
    abrirArchivo()
    
    def numero():
        try:
            numero = int(input("Número: "))
            resultado = 100 / numero
        except (ValueError, ZeroDivisionError):
            print("La operación no puede realizarse con ese dato.")
        numero()