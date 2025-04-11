
nombre_del_archivo = 'informacion.txt'

try:
    with open(nombre_del_archivo, 'r') as archivo:
        print("Leyendo el contenido del archivo...\n")

        for numero_linea, contenido in enumerate(archivo, 1):
           
            print(f"Línea {numero_linea}: {contenido.strip()}")
    
except FileNotFoundError:
        print(f"¡No se pudo encontrar el archivo '{nombre_del_archivo}' en el directorio.")



