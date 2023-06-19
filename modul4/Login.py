print("<==== SISTEM LOGIN SEDERHANA ====>")
login = 0
while True:
    username = (input("Masukan Username: "))
    password = (input("Masukan Password: "))

    if login == 3:
        print("Login gagal akun anda telah diblokir")
        break
    
    if username == "adiwww" and password == "adiwicaksono" :
        print("Selamat Datang ", username, "!")
        break

    else:
        print("Username atau password salah, silahkan coba lagi")
        login += 1
    
    