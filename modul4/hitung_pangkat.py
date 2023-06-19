print("<===== MENGHITUNG PANGKAT =====>")
bilangan = int(input("Masukkan bilangan: "))
pangkat = int(input("Masukkan pangkat: "))

hasil = 1

for i in range(pangkat):
    hasil *= bilangan

print(bilangan, "pangkat", pangkat, "adalah", hasil)
