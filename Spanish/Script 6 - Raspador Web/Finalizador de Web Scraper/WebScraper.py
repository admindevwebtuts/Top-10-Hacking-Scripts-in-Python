import requests
from bs4 import BeautifulSoup

def guardar_en_archivo(datos, nombre_archivo):
  with open(nombre_archivo, 'w') as archivo:
    archivo.write(datos)

url = 'https://www.devwebtuts.com'

respuesta = requests.get(url)

if respuesta.status_code != 200:
  print("No se pudo acceder al sitio web")
else:
  sopa = BeautifulSoup(respuesta.text, 'html.parser')
  titulos = sopa.find_all('h4')
  autores = sopa.find_all(class_='card-text')

  datos = ""
  for i in range(len(titulos)):
    datos += f"Título: {titulos[i].text}, Autor: {autores[i].text}\n"

  guardar_en_archivo(datos, 'datos_blog.txt')