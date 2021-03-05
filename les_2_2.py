x = list(input('введите числа: '))
i = 0
if len(x) % 2 == 0:
    while i < len(x):
        a = x[i]
        x[i] = x[i + 1]
        x[i + 1] = a
        i += 2
else:
    while i < len(x) - 1:
        a = x[i]
        x[i] = x[i + 1]
        x[i + 1] = a
        i += 2
print(x)