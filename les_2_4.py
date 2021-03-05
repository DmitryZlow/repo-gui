string = input("Введите любое количество слов через пробел: ")
a = string.split(' ')
for num, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{num})  {el}")