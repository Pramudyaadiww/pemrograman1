def insertion_sort(arr, jenis_sort):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        if jenis_sort == '1':
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
        else:
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

def main():
    buku = []
    n = int(input("Masukkan jumlah buku: "))
    for i in range(n):
        nama = input("Masukkan nama buku ke-{}: ".format(i + 1))
        buku.append(nama)
    print("\n")
    print(" <===== Sorting =====> ")
    print("1. Insertion Ascending")
    print("2. Insertion Descending")
    jenis_sort = input("\nPilih jenis sorting: ")
    insertion_sort(buku, jenis_sort)

    print("\nDaftar buku setelah diurutkan:", buku)

main()
