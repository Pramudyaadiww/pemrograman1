nilai = int(input("Masukkan nilai: "))

if nilai > 85:
    grade = "A"
elif nilai > 75:
    grade = "B"
elif nilai > 65:
    grade = "C"
elif nilai > 55:
    grade = "D"
else:
    grade = "E"

print("Grade anda adalah", grade)
