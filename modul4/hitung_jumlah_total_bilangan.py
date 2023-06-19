print("<===== PROGRAM SEDERHANA MENGHITUNG TOTAL JUMLAH BILANGAN =====>")
bilangan = int(input("Masukkan bilangan: "))
total = 0
i = 1
while i <= bilangan:
    total += i
    i += 1

print("Total nilai dari 1 hingga", bilangan, "adalah", total)
