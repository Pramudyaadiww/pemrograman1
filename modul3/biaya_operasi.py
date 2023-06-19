print("<------- Menu Biaya Operasi ------->")
print("1.Biaya Operasi Mata \n2.Biaya Operasi Jantung")
operasi = (input("Pilih salah satu (1/2): "))

if(operasi == '1'):
    print("<------- jenis penyakit mata ------->")
    print("1.Katarak \n2.Plus/Minus \n3.Silinder")
    mata = (input("Pilih jenis penyakit mata (1-3): "))
    if(mata == '1'):
        print("Biaya Operasi Katarak: Rp 7.500.000,00")
    elif(mata == '2'):
        print("Biaya Operasi Plus/Minus: Rp 5.000.000,00")
    elif(mata == '3'):
        print("Biaya Operasi Silinder: Rp 4.000.000,00")
    else:
        print("Yang Anda inputkan salah!")
elif(operasi == '2'):
    print("<------- jenis penyakit jantung ------->")
    print("1.Jantung Koroner \n2.Katup Jantung \n3.Otot Jantung")
    jantung = (input("Pilih jenis penyakit jantung (1-3): "))
    if(jantung == '1'):
        print("Biaya operasi Jantung Koroner: Rp 500.000.000,00")
    elif(jantung == '2'):
        print("Biaya operasi Katup Jantung: Rp 350.000.000,00")
    elif(jantung == '3'):
        print("Biaya operasi Otot Jantung: Rp450.000.000,00")
    else:
        print("Yang Anda inputkan salah!")
else:
    print("Yang Anda inputkan salah!")

