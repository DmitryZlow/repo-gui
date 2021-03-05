num = int(input("Введите числовое выражение месяца (1-12): "))
if num <= 12 and num >= 1:
    month = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
#    month = list(month_dict.values())
    for i in enumerate(month):
        if i == num-1:
            print(f"Месяц из списка {month[i]}")
            break
    print(f"Месяц: {month[num]}")
else:
    print("Введите корректное число!")