import time

true_password = "qwerty"
max_failed_attempts = 3

def password_checker(input_password):
    failed_attempts = 0
    while input_password != true_password and failed_attempts < max_failed_attempts:
        failed_attempts += 1
        input_password = input("Enter password: ")
        if failed_attempts == max_failed_attempts:
            print(f"Too many failed attempts. System locked for 10 seconds.")
            time.sleep(10)
            failed_attempts = 0
    if input_password == true_password:
        print("Access granted.")
    else:
        print("Access denied.")

password_checker(input("Enter password: "))
