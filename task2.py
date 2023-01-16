""" 1. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой. """

def user_func(first_name, sur_name, birth_year, city, mail, phone):
    print(f'first_name - {first_name}; sur_name - {sur_name}; birth_year - {birth_year}; city - {city}; mail - {mail}; phone - {phone}')


user_func(first_name=input('Фамилия: '), sur_name=input('Имя: '), birth_year=input('Год рождения: '), city=input('Город: '), mail=input('E-mail: '), phone=input('Телефон: '))
