import requests 
respuesta = requests.get('https://www.python.org') 
print(respuesta.status_code)
