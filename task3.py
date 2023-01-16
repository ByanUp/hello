""" 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
аргументов. """


def my_func(var1, var2, var3):
    x = [var1, var2, var3]
    a = max(x)
    x.remove(a)
    b = max(x)
    print(a + b)


my_func(5, 10, 15)
