import time

true_password = "qwerty"
max_failed_attempts = 3

def password_checker(input_password):
  failed_attempts = 0
  while input_password != true_password and failed_attempts < max_failed_attempts:
    failed_attempts += 1
    input_password = input("Ingresa la contraseña: ")
    if failed_attempts == max_failed_attempts:
      print(f"Demasiados intentos fallidos. Sistema bloqueado durante 10 segundos.")
      time.sleep(10)
      failed_attempts = 0
  if input_password == true_password:
    print("Acceso concedido.")
  else:
    print("Acceso denegado.")

password_checker(input("Ingresa la contraseña: ")) 