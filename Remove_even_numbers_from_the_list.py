a = input("Введите список чисел через пробел: ").split()
lst = []
i = len(a) - 1
while i >= 0:
    if int(a[i]) % 2 == 0:
        lst.append(a[i])
    i = i - 1
print(lst)
