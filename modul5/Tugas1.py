jumlahkata = int(input("Masukan Jumlah Kata: "))
array_kata = []

for i in range(jumlahkata):
    kata = input("Masukan kata: ")
    array_kata.append(kata)

print("\n")

cari_kata = input("Masukan kata yang ingin dicari: ")

if cari_kata in array_kata:
    indeks = array_kata.index(cari_kata)
    print(f"'{cari_kata}' Ditemukan pada indeks ke- {indeks}.")
else:
    print("Kata tidak ditemukan")
