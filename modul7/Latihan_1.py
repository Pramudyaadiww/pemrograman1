#tambah data mahasiswa
def addmahasiswa(arraymahasiswa):
    jumlah = int(input("Jumlah mahasiswa: "))
    mahasiswa = []
    while jumlah > 0:
        nama = input("Nama Mahasiswa: ")
        mahasiswa.append(nama)
        jumlah = jumlah - 1

    while True:
        panggil(mahasiswa)
        jumlah = jumlah - 1
        if jumlah < 0:
            break

#Hapus data mahasiswa
def removemahasiswa(arraymahasiswa):
    mahasiswa = arraymahasiswa
    print("Data mahasiswa: %s" % arraymahasiswa)
    mahasiswa_to_remove = input("Hapus mahasiswa: ")
    mahasiswa.remove(mahasiswa_to_remove)
    print("Data Mahasiswa: %s" % mahasiswa)
    panggil(mahasiswa)

#urutkan data mahasiswa
def ascmahasiswa(arraymahasiswa):
    mahasiswa = arraymahasiswa
    mahasiswa.sort()
    print(mahasiswa)
    panggil(mahasiswa)

#lihat data mahasiswa
def viewmahasiswa(arraymahasiswa):
    mahasiswa = arraymahasiswa
    for x in mahasiswa:
        print("Nama mahasiswa: %s" % x)
    panggil(arraymahasiswa)

#menu
def panggil(arraymahasiswa):
    print("\n <===== MENU DATA MAHASISWA =====>")
    print("1. Tambah data mahasiswa ")
    print("2. Hapus data mahasiswa ")
    print("3. Urutkan data mahasiswa ")
    print("4. Lihat data mahasiswa ")
    print("5. Tutup")

    pilih = int(input("Pilih (1-5): "))
    if pilih == 1:
        addmahasiswa(arraymahasiswa)
    elif pilih == 2:
        removemahasiswa(arraymahasiswa)
    elif pilih == 3:
        ascmahasiswa(arraymahasiswa)
    elif pilih == 4:
        viewmahasiswa(arraymahasiswa)
    else:
        print("Selesai")

mahasiswa = []
addmahasiswa(mahasiswa)
