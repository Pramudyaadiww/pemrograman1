def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


ips = [3.8, 2.9, 3.3, 4.0, 2.7]
print("IPS sebelum diurutkan:", ips)
bubble_sort(ips)
print("IPS setelah diurutkan:", ips)
