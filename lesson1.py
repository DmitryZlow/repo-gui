#Задача №1
name = input('Введите ваше имя ')
age = input('Ваш возраст ')
country = input('Страна проживания ')
print(f"Вас зовут {name}, Вам {age} лет, Ваша страна: {country}" )


#Задача №2
time = int(input('Введите время в секундах: '))
hour = time // 3600
minute = (time % 3600) // 60
second = (time % 3600) % 60
print(f'{hour}:{minute}:{second}')


#Задача №3
n = input('Введите число ')
a = str(n + n)
b = str(n + n + n)
answer = int(n) + int(a) + int(b)
print(answer)

#Задача №4
num = int(input('Введите целое положительное число: '))
x = num % 10
while num > 10:
    if num % 10 > x:
        x = num % 10
    num = num // 10
print(x)


#Задача №5
profit = int(input('Выручка вашей фирмы: '))
costs = int(input('Издержки: '))
if profit - costs > 0:
    print('У вас благополучная фирма, прибыль составляет', (profit - costs))
    print('Рентабельность:', int((profit - costs) * 100 / profit),'%')
else:
    print('У вашей фирмы дела плохи, убытки составляют', costs - profit)

person = int(input('Сколько человек в вашей фирме: '))
PpP = (profit - costs) / person
print('Прибыль на одного сотрудника составляет:', PpP)


#Задача №6
a = int(input('1 день кол-во км: '))
b = int(input('общий результат км: '))
x = a * 0.1
day = 0
while a < b:
    a += x
    day += 1
print(day)






