passwords = ["123456", "password", "admin", "qwerty", "password1"]
true_password = "qwerty"

for password in passwords:
    if password == true_password:
        print(f"Password has been cracked! It's '{password}'.")
        break
else:
    print("Failed to crack the password.")
