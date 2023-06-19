def penjumlahan(bil1, bil2):
    return bil1 + bil2

def pengurangan(bil1, bil2):
    return bil1 - bil2

def perkalian(bil1, bil2):
    return bil1 * bil2

def pembagian(bil1, bil2):
    return bil1 / bil2

def pangkat(bil1, bil2):
    return bil1 ** bil2

print("<===== KALKULATOR =====>")
print("1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Pangkat")
kalkulator = input("Pilih Kalkulator (1-5): ")
print("\n")

if kalkulator == '1':
    bil1 = float(input("Masukkan bilangan pertama : "))
    bil2 = float(input("Masukkan bilangan kedua   : "))
    print("Hasil penjumlahan adalah  :", penjumlahan(bil1, bil2))
elif kalkulator == '2':
    bil1 = float(input("Masukkan bilangan pertama : "))
    bil2 = float(input("Masukkan bilangan kedua   : "))
    print("Hasil pengurangan adalah  :", pengurangan(bil1, bil2))
elif kalkulator == '3':
    bil1 = float(input("Masukan bilangan pertama : "))
    bil2 = float(input("Masukan bilangan kedua   : "))
    print("Hasil perkalian adalah   :", perkalian(bil1, bil2))
elif kalkulator == '4':
    bil1 = float(input("Masukan bilangan pertama : "))
    bil2 = float(input("Masukan bilangan kedua   : "))
    print("Hasil pembagian adalah   :", pembagian(bil1, bil2))
elif kalkulator == '5':
    bil1 = float(input("Masukan bilangan pertama  : "))
    bil2 = float(input("Masukan bilangan pangkat  : "))
    print("Hasil perpangkatan adalah :", pangkat(bil1, bil2))
else:
    print("Yang anda inputkan salah!!!")

