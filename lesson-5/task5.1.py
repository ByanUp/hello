""" 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
окончании ввода данных будет свидетельствовать пустая строка. """

new_file = open('smile.txt', 'w')
line = input('Введите текст \n')
while line:
    new_file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

new_file.close()
new_file = open('smile.txt', 'r')
content = new_file.readlines()
print(content)
new_file.close()
