print("<===== PROGRAM HITUNG KPK =====>")
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))

if num1 > num2:
    max_num = num1
else:
    max_num = num2

i = 1
while True:
    kpk = max_num * i
    if kpk % num1 == 0 and kpk % num2 == 0:
        break
    i += 1

print("KPK dari", num1, "dan", num2, "adalah", kpk)
