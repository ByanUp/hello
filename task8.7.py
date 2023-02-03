""" 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
(комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата. """


class Op_Comp_Numb:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма d и e:')
        return f'x = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение d и e:')
        return f'x = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'x = {self.a} + {self.b} * i'


d = Op_Comp_Numb(1, 2)
e = Op_Comp_Numb(3, 4)
print(d)
print(d + e)
print(d * e)
