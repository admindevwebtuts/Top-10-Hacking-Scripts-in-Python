import re
from bs4 import BeautifulSoup

def extraer_correos(archivo):
    try:
        # Abrir el archivo HTML local
        with open(archivo, 'r') as archivo:
            contenido = archivo.read()

        # Analizar el contenido HTML
        sopa = BeautifulSoup(contenido, 'html.parser')

        # Mejorar la expresión regular para buscar correos electrónicos
        regex_correo = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        correos = re.findall(regex_correo, str(sopa))

        # Imprimir todos los correos encontrados
        print(correos)

    except Exception as e:
        print(f"Se produjo un error: {e}")

# Pedir al usuario que ingrese el nombre del archivo
archivo = input("Ingrese el nombre del archivo HTML: ")
extraer_correos(archivo)