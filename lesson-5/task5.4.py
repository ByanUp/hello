""" 4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
заменяться на русские. Новый блок строк должен записываться в новый текстовый файл. """

glossary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

source_file = open("task5.4.txt", "r")
final_file = open("task5.4_new.txt", "a", encoding="utf8")

for line in source_file.readlines():
    for word in glossary:
        if word == line.split()[0]:
            line = line.replace(line.split()[0], glossary.get(word))
            final_file.write(f"{line}")
            print(line)

source_file.close()
final_file.close()
