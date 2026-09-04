def archivo():

    try:
        archivo = open("reportes.txt", "r")
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
        archivo.close()

    except FileNotFoundError:
        print("Error: El archivo 'reportes.txt' no se encontró en el directorio actual.")

    finally:
        print("Proceso de lectura de archivo finalizado.")
    
    archivo()
    
def importacion_controlada():
    #Simula la importación de un módulo que no existe y controla ModuleNotFoundError. 
    # El mensaje debe explicar qué debe revisar la persona desarrolladora.

    try:
        import libreria_inexistente

    except ModuleNotFoundError:
        print("Error de dependencia (ModuleNotFoundError):")
        print("- Verifique que el nombre del módulo esté escrito correctamente.")
        print("- Asegúrese de haber instalado el paquete correspondiente usando pip (ej. 'pip install <modulo>').")
        print("- Verifique que su entorno virtual (si utiliza uno) esté activado correctamente.")
    
    importacion_controlada()