# phishing_detection.py
import http.client
import re

# Una lista de palabras que podrían indicar una página de phishing
PALABRAS_CLAVE = ["contraseña", "tarjeta de crédito", "cuenta bancaria"]

def buscar_pagina(url):
    conn = http.client.HTTPSConnection(url)
    conn.request("GET", "/")
    response = conn.getresponse()
    return response.read().decode()

def es_pagina_de_phishing(contenido_html):
    for palabra_clave in PALABRAS_CLAVE:
        if re.search(palabra_clave, contenido_html, re.I):  # re.I hace que la búsqueda no sea sensible a mayúsculas y minúsculas
            return True
    return False

def verificar_pagina(url):
    contenido_html = buscar_pagina(url)
    if es_pagina_de_phishing(contenido_html):
        print(f"¡ADVERTENCIA: La página en {url} puede ser una página de phishing!")
    else:
        print(f"La página en {url} no parece ser una página de phishing.")

# Ejemplo de uso:
verificar_pagina("localhost:8080")