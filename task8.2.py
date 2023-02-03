""" 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой. """


class New_Exception(Exception):

    def separate_func(self, a, b):
        try:
            res = round(a / b, 2)
        except ZeroDivisionError:
            print(f"{a} / {b} -> деление на ноль недопустимо!\n")
        else:
            print(f"Все хорошо, результат: {a} / {b} = {res} \n")


n_e = New_Exception()

n_e.separate_func(10, 5)
n_e.separate_func(5, 0)
n_e.separate_func(10, 2)
n_e.separate_func(0, 0)
