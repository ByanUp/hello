""" 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить её на экран. """


def all_numb():
    try:
        with open('task5.5.txt', 'w+') as file_obj:
            line = input('Введите числа, разделенные пробелом: \n')
            file_obj.writelines(line)
            new_numb = line.split()

            print(sum(map(int, new_numb)))
    except ValueError:
        print('Неправильно выполнено условие, повторите ввод')


all_numb()
