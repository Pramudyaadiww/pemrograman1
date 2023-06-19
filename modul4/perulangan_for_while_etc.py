#perulangan for
for i in range (7):
    print("hello world!")

print("\n")

#perulangan While
i = 0
while i <= 7:
    print("Hello World!")
    i += 1
    
print("\n")

#Range (min, max)
for i in range (1, 10):
    print(f"perulangan ke- {i}")

print("\n")  

#Range (min, max, step)
for i in range (1, 20, 2):
    print(f"Step ke- {i}")

print("\n")

#Range Decrement
for i in range (10, 0, -1):
    print(f"Step ke- {i}")

print("\n")

#While Increment
a = 1
b = 10
while a < b:
    print("Step ke- ",a)
    a += 1

print("\n")

#While Decrement
a = 10
b = 0
while a > b:
    print("Step ke- ",a)
    a -= 1

print("\n")

#Break pada perulangan for
for i in range (1, 10):
    print("ini perulangan ke- ", i)
    if i == 7:
        print("perulangan ke- ", i, "diberhentikan")
        break

print("\n")

#continue decrement pada for
for i in range (0, 10):
    if (i == 5):
        continue
    print(i)

print("\n")

#break pada while
a = 0
while True:
    print("step ke- ", a, "!")
    a += 1
    if a == 7:
        print("Step ke- ", a, "Dihentikan!")
        break

print("\n")

#Continue pada while
angka = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    #Skip jika i adalah bilangan genap
    #dan i lebih dari 0
i = -1
while i < len(angka):
    i += 1
    if 1 % 2 == 0 and i > 0:
        print('Skip')
        continue
    #tidak dieksekusi ketika continue dipanggil
    print(angka[i])

