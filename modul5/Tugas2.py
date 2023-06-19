jumlah_matkul = int(input("Masukkan Jumlah Mata Kuliah: "))

nilai_matkul = []
for i in range(1, jumlah_matkul + 1):
    nilai = float(input(f"Masukkan Nilai Mata Kuliah ke-{i}: "))
    nilai_matkul.append(nilai)

rerata = sum(nilai_matkul) / len(nilai_matkul)

predikat = ''
if 100 > rerata >= 90:
    predikat = 'A'
elif 90 > rerata >= 70:
    predikat = 'B'
elif 70 > rerata >= 50:
    predikat = 'C'
elif 50 > rerata >= 30:
    predikat = 'D'
elif 30 > rerata >= 0:
    predikat = 'E'
else:
    predikat = 'Tidak Valid'

print("\n")

print(f"Hasil Predikat '{predikat}' dengan nilai rerata: {rerata}")

for i, nilai in enumerate(nilai_matkul):
    print(f"Mata Kuliah ke-{i + 1}: {nilai}")

