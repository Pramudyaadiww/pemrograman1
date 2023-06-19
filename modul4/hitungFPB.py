# Input dua bilangan bulat
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))

# Menentukan bilangan terkecil dari dua bilangan
if num1 < num2:
    smaller = num1
else:
    smaller = num2

# Mencari faktor dari bilangan terkecil
factors = []
for i in range(1, smaller+1):
    if((num1 % i == 0) and (num2 % i == 0)):
        factors.append(i)

# Mencetak faktor terbesar
print("FPB dari", num1, "dan", num2, "adalah", max(factors))
