import time

passwords = ["123456", "password", "admin", "qwerty", "password1"]
true_password = "qwerty"

start_time = time.time()

for password in passwords:
    print(f"Attempting password: {password}")
    if password == true_password:
        print(f"Password has been cracked! It's '{password}'.")
        break
else:
    print("Failed to crack the password.")

end_time = time.time()

total_time = end_time - start_time
print(f"It took {total_time} seconds to crack the password.")
