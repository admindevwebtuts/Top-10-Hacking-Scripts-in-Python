contraseñas = ["123456", "password", "admin", "qwerty", "password1"]
contraseña_correcta = "qwerty"

for contraseña in contraseñas:
    if contraseña == contraseña_correcta:
        print(f"¡Contraseña descifrada! Es '{contraseña}'.")
        break
else:
    print("No se pudo descifrar la contraseña.")