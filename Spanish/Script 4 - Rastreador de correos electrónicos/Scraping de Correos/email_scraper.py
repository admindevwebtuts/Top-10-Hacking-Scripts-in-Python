# Importar bibliotecas necesarias
import re
import requests
from bs4 import BeautifulSoup

# Obtener la página web

#response = requests.get('http://localhost/test.html')
with open('G:\My Drive\Business\Amazon\Hacking\Python\CodeExamplesSpanish\Script 4 - Rastreador de correos electrónicos\EmailScraper\index.html', 'r') as file:
    content = file.read()

# Analizar el contenido de la página

#soup = BeautifulSoup(response.text, 'html.parser')
soup = BeautifulSoup(content, 'html.parser')

# Encontrar correos electrónicos en el contenido de la página
email_regex = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
emails = re.findall(email_regex, str(soup))

# Imprimir todos los correos electrónicos encontrados
print(emails)