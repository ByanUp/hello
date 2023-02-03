""" 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а
также других данных, можно использовать любую подходящую структуру (например, словарь). """


class Office_Equip:

    def __init__(self, firm, price, quantity):
        self.firm = firm
        self.price = price
        self.quantity = quantity
        self.items = {'Фирма': self.firm, 'Цена': self.price, 'Количество': self.quantity}

    def income(self):
        try:
            model = input(f'Введите модель: ')
            price = int(input(f'Введите цену: '))
            quantity = int(input(f'Введите количество: '))
            item = {'Модель устройства': model, 'Цена': price, 'Количество': quantity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Недопустимое значение!')


class Printer(Office_Equip):
    pass


class Scanner(Office_Equip):
    pass


class Xerox(Office_Equip):
    pass


p = Printer('Pantum', 100, 100)
s = Scanner('Hp', 500, 10)
x = Xerox('Epson', 700, 15)
p.income()
s.income()
x.income()
