name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
year = int(input('Введите ваш год рождения: '))
city = input('Введите ваш город проживания: ')
email = input('Введите ваш E-Mail: ')
phone = input('Введите номер телефона: ')
def func(a, b, c, d, e, f):
    print(f'Ваши данные: гр. {name} {surname}, {year} г.р., г. {city}, {email},тел. {phone}')
func(name, surname, year, city, email, phone)