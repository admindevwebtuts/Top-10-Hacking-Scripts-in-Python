import time

contraseñas = ["123456", "password", "admin", "qwerty", "password1"]
contraseña_correcta = "qwerty"

hora_inicio = time.time()

for contraseña in contraseñas:
    print(f"Intentando la contraseña: {contraseña}")
    if contraseña == contraseña_correcta:
        print(f"¡Contraseña descifrada! Es '{contraseña}'.")
        break
else:
    print("No se pudo descifrar la contraseña.")

hora_fin = time.time()

tiempo_total = hora_fin - hora_inicio
print(f"Tomó {tiempo_total} segundos para descifrar la contraseña.")