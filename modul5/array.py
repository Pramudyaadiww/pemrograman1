angka = [1,2,3,4,5]
text = ["Satu", "Dua", "Tiga", "Empat", "Lima"]

print(angka)
print(text)

print("\n")

buah = [["Apel", "mangga", "Jeruk", "Nanas", "Semangka"],    ["Melon", "Manggis", "Durian", "Sawo", "Jambu"]]
for i in range (len(buah)):
    for x in range(len(buah[i])):
        print(buah[i][x])
