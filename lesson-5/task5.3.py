""" 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10
строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт
средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32 """


def salary_e():
    salary = {}
    try:
        with open('task5.3.txt', encoding='utf-8') as file:
            for line in file:
                salary[line.split()[0]] = float(line.split()[1])
        print('Меньше 20000 получают:')
        for name, wage in salary.items():
            if wage < 20000:
                print(name)
        print(f'Средняя зарплата равна {sum(salary.values()) / len(salary)}')
    except IOError:
        print('Денег нет, но вы держитесь')


salary_e()
