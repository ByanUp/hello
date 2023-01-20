""" 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные
числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce(). """

# Запуск через терминал

from sys import argv

script_name, output_hours, rate_hour, reward = argv

print("Имя скрипта: ", script_name)
print("\n<< Employee programm >>")
print("Выработка в часах: ", output_hours)
print("Ставка в час: ", rate_hour)
print("Премия: ", reward)
print("Зарплата сотрудника: ", (float(output_hours) * float(rate_hour)) + float(reward))
