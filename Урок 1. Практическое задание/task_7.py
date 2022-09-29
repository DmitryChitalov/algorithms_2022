"""
Задание 7. На закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов,
например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить
проверку на палиндром и в таких строках (включающих пробелы)

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--код с нуля писать не нужно, требуется доработать пример с урока
"""


class DequeClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_back(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_back(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


def check(string):
    dc = DequeClass()
    replace_string = string.replace(' ', '')
    for el in replace_string:
        dc.add_to_back(el)

    still_equal = True

    while dc.size() > 1 and still_equal:
        first = dc.remove_from_front()
        last = dc.remove_from_back()
        if first != last:
            still_equal = False

    return still_equal


print(check("молоко делили ледоколом"))
