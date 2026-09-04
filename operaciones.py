def promedioventas():
    # Solicitamos tres ventas y calculamos su promedio
    # Controlamos ValueError (entrada no numérica) y ZeroDivisionError 
    # (en caso de dynamic list size)

        try:
            v1 = float(input("Ingrese la primera venta: "))
            v2 = float(input("Ingrese la segunda venta: "))
            v3 = float(input("Ingrese la tercera venta: "))
        except ValueError:
            print("Error: Todas las ventas deben ser valores numéricos válidos.")
            return

        ventas = [v1, v2, v3]
    
        try:
            promedio = sum(ventas) / len(ventas)
            print(f"El promedio de las ventas es: ${promedio:.2f}")
        except ZeroDivisionError:
            print("Error: No se pueden calcular promedios sin elementos en la lista (división por cero).")
            promedioventas()
            
def descuento():
    #Calcula un porcentaje a partir de un monto y una base. 
    # Controla entradas no numéricas y una base igual a cero.
        
        try:
            monto = float(input("Ingrese el monto del descuento: "))
            base = float(input("Ingrese la base total: "))
    
            porcentaje = (monto / base) * 100
            print(f"El descuento equivale al {porcentaje:.2f}% de la base.")

        except ValueError:
            print("Error: Ambos valores deben ser numéricos.")
        except ZeroDivisionError:
            print("Error: La base no puede ser cero (no se puede dividir por cero).")
        descuento()

def conversion_moneda():
    #Solicita monto y tasa de cambio. 
    # Calcula el equivalente y controla los errores de conversión.
        
    try:
        monto = float(input("Ingrese el monto a convertir: "))
        tasa = float(input("Ingrese la tasa de cambio: "))

        if tasa <= 0:
            print("Aviso: La tasa de cambio debe ser un número positivo mayor a 0.")
        else:
            conversion = monto * tasa
            print(f"Monto convertido: {conversion:.2f}")
            
    except ValueError:
        print("Error: Tanto el monto como la tasa de cambio deben ser números válidos.")
conversion_moneda()

def tipos_incompatibles():
    #Construye un pequeño programa que provoque TypeError y después 
    # corrígelo mediante una conversión o una validación apropiada. 
    #Explica por qué ocurrió.
    
# CÓDIGO CON ERROR (TypeError):
# Ocurre porque input() devuelve un string 'str', y no se puede multiplicar un string por un float/int.
# texto_precio = input("Ingrese precio: ")
# total = texto_precio * 1.15  --> Genera: TypeError: can't multiply sequence by non-int of type 'float'

# CÓDIGO CORREGIDO Y CONTROLADO:
def tipos_incompatibles():
        
    try:
        texto_precio = input("Ingrese el precio base: ")
        precio = float(texto_precio)
        
        total = precio * 1.15
        print(f"Total con 15% de impuesto: ${total:.2f}")
        
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

tipos_incompatibles()

def calculo_comision():
    #Calcula una comisión a partir de ventas y porcentaje. 
    # Usa try/except para controlar datos no numéricos y documenta qué excepción 
    # esperas.
    try:
        ventas = float(input("Ingrese el total de ventas: "))
        porcentaje = float(input("Ingrese el porcentaje de comisión (ej. 10 para 10%): "))
    
        comision = ventas * (porcentaje / 100)
        print(f"La comisión calculada es: ${comision:.2f}")

    except ValueError:
        print("Error: Solo se permiten valores numéricos para el cálculo de la comisión.")
    calculo_comision()