number = int(input("Введите число: "))
my_list = [7, 5, 3, 3, 2]
x = my_list.count(number)
for element in my_list:
    if x > 0:
        i = my_list.index(number)
        my_list.insert(i + x, number)
        break
    else:
        if number > element:
            i = my_list.index(element)
            my_list.insert(i, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)