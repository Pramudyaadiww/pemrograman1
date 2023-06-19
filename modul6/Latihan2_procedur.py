def banding(nilai1, nilai2):
    if (nilai1 > nilai2):
        print (nilai1)
    elif (nilai1 == nilai2):
        print ("Kedua nilai sama")
    else:
        print(nilai2)

nilai1 = int(input("Masukkan bilangan ke-1: "))
nilai2 = int(input("Masukkan bilangan ke-2: "))
print("Bilangan yang lebih besar adalah:", banding(nilai1, nilai2))


