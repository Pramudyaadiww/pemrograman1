def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

data_array = [123,4,321,32,45,6,5,2,3,45,12,44]
print(bubble_sort(data_array))

