A = 8
B = 5

print(A, B)

A = B
B = A

print(A, B)

pokok = int (input("masukan gaji pokok: "))
tunjangan = 20/100
pajak = 15/100

gajitunjangan = tunjangan + (pokok + tunjangan)
print("gaji pokok + tunjangan: ", gajitunjangan)

potpajak = gajitunjangan - pajak
print("potongan pajak: ", potpajak)

gajibersih = gajitunjangan - potpajak
print("Gaji bersih karyawan: ", gajibersih)