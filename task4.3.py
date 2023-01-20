""" 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
Подсказка: используйте функцию range() и генератор. """

# Запуск через терминал

from sys import argv

script_name, output_hours, rate_hour, reward = argv

print("Имя скрипта: ", script_name)
print("\n<< Employee programm >>")
print("Выработка в часах: ", output_hours)
print("Ставка в час: ", rate_hour)
print("Премия: ", reward)
print("Зарплата сотрудника: ", (float(output_hours) * float(rate_hour)) + float(reward))
