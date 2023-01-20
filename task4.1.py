""" 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных
значений необходимо запускать скрипт с параметрами. """

# Запуск через терминал

from sys import argv

script_name, output_hours, rate_hour, reward = argv

print("Имя скрипта: ", script_name)
print("\n<< Employee programm >>")
print("Выработка в часах: ", output_hours)
print("Ставка в час: ", rate_hour)
print("Премия: ", reward)
print("Зарплата сотрудника: ", (float(output_hours) * float(rate_hour)) + float(reward))
