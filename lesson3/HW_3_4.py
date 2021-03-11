x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
#1 способ
def func(x, y):
    if x <= 0 or y >= 0:
        return 'Введите корректные числа'
    else:
        return x ** y
print(func(x, y))

#2 способ
def func(x, y):
    return 1 if y == 0 else func(x, y + 1) * 1 / x

print(func(x, y))
