nombre_del_archivo = 'informacion.txt'

try:
    with open(nombre_del_archivo, 'r') as archivo:
        print("Personas con correos que terminan en '.org':\n")

        for numero_linea, contenido in enumerate(archivo, 1):
            if '.org' in contenido:
                persona = contenido.strip().split(', ')
                print(persona)

except FileNotFoundError:
    print(f"No se encontro el archivo '{nombre_del_archivo}' en el directorio.")







