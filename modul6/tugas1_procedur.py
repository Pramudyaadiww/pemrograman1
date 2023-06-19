def cek_bilangan (bil):
    if bil % 2 == 0:
        print(f"Bilangan {bil} adalah bilangan genap")
    else:
        print(f"Bilangan {bil} adalah bilangan ganjil")

bilangan = int(input("Masukan bilangan: "))
cek_bilangan(bilangan)

