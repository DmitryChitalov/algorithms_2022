#! +
"""
2021-12-18
Geekbrains. Факультет python-разработки
Студент: Папко Роман.
Четверть 1. Алгоритмы и структуры данных на Python. Базовый курс
Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
Домашнее задание 7.
"""
"""
Задание 7. На закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов,
например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить
проверку на палиндром
и в таких строках (включающих пробелы)

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--код с нуля писать не нужно, требуется доработать пример с урока
"""

class DequeClass:  # Класс притащил сюда, дабы не приписывать импорт "из непонятно откуда"

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


def pal_checker(string):
    dc_obj = DequeClass()

    for el in string:
	# Отфильтровываем пробелы "на берегу", для проверки палиндрома они не нужны.
        if el != ' ':
            dc_obj.add_to_rear(el.lower())

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()

        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("Молоко делили ледоколом"))
print(pal_checker("Я не стар  брат Сеня"))
print(pal_checker("А роза упала на лапу Азора"))