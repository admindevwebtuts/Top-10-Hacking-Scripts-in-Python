import requests
from bs4 import BeautifulSoup

url = 'https://www.devwebtuts.com/'
respuesta = requests.get(url)
sopa = BeautifulSoup(respuesta.text, 'html.parser')

parrafos = sopa.find_all('p')
for para in parrafos:
    print(para.text)