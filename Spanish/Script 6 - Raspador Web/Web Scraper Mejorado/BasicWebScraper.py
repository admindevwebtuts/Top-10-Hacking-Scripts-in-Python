import requests
from bs4 import BeautifulSoup

def guardar_en_archivo(data, nombre_archivo):
     with open(nombre_archivo, 'w') as archivo:
         archivo.write(data)

url = 'https://www.devwebtuts.com'

respuesta = requests.get(url)

if respuesta.status_code != 200:
    print("No se pudo acceder al sitio web")
else:
    sopa = BeautifulSoup(respuesta.text, 'html.parser')
    parrafos = sopa.find_all('p')

    texto = ""
    for para in parrafos:
         texto += para.text + '\n'

    guardar_en_archivo(texto, 'datos_extraidos.txt')