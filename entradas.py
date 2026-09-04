def precioproducto():
    #Solicita el precio de un producto y conviértelo a float. 
    # Controla ValueError y muestra un mensaje adecuado cuando la entrada 
    # no sea numérica.
    try:
        entrada = input("Introduce el precio del producto: ")
        precio = float(entrada)
        print(f"El precio ingresado es: ${precio:.2f}")
    except ValueError:
        print("Error: Por favor, ingresa un número válido (ej. 15.50 o 10).")
        
    precioproducto()
    
    def cantidadproducto():
        #Solicita la cantidad de unidades que una persona desea comprar. 
        # Controla entradas que no puedan convertirse a entero.
        try:
            entrada = input("Introduce la cantidad de unidades: ")
            cantidad = int(entrada)
            print(f"La cantidad ingresada es: {cantidad}")
        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")
        cantidadproducto()
            
def nota():
    #Solicita una calificación numérica. Controla ValueError y,
    # si la conversión funciona, indica si la calificación está entre 0 y 100.
    
        try:
            entrada = input("Introduce la calificación (0-100): ")
            calificacion = float(entrada)
            if 0 <= calificacion <= 100:
                print(f"La calificación ingresada es: {calificacion}")
            else:
                print("Error: La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Error: Por favor, ingresa un número válido (ej. 85.5 o 90).")
        nota()
        
def edad_registro():
    #Solicita la edad. 
    # Controla ValueError y evita que el programa continúe con una edad 
    # que no sea válida.
    
    while True:
        entrada = input("Introduce tu edad: ")
    
        try:
            edad = int(entrada)
        except ValueError:
                print("Error: Debes ingresar un número entero válido (sin decimales ni letras).\n")
                continue

        if edad < 0 or edad > 120:
            print("Error: La edad debe estar entre 0 y 120 años.\n")
        else:
            break
        print(f"Edad registrada correctamente: {edad} años.")
    
    edad_registro()

def entrada_consecutiva():
    #Solicita nombre, edad y salario. Controla únicamente las 
    # conversiones que pueden producir excepciones y muestra qué dato debe corregirse.
    nombre = input("Introduce tu nombre: ")
nombre = input("Introduce tu nombre: ")

try:
    edad = int(input("Introduce tu edad: "))
except ValueError:
    print("Error: La edad debe ser un número entero válido.")
    exit()  

try:
    salario = float(input("Introduce tu salario: "))
except ValueError:
    print("Error: El salario debe ser un número decimal o entero válido.")
    exit()  

print(f"\n¡Registro exitoso!")
print(f"Nombre: {nombre} | Edad: {edad} | Salario: ${salario:.2f}")
        