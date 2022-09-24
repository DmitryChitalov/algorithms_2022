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


class Deque:
    def __init__(self):
        self.items = []

    def clear(self):
        return self.items == []

    def add_to_front(self, el):
        self.items.append(el)

    def add_to_rear(self, el):
        self.items.insert(0, el)

    def remove_front(self):
        self.items.pop()

    def remove_rear(self):
        self.items.pop(0)

    def item_count(self):
        return len(self.items)


def pal_checker(string):
    dc_obj = Deque()
    new_str = string.replace(' ', '')
    for el in new_str:
        dc_obj.add_to_rear(el)

    is_equal = True

    while dc_obj.item_count() > 1 and is_equal:

        first = dc_obj.remove_front()
        last = dc_obj.remove_rear()

        if first != last:
            is_equal = False

        return is_equal


print(pal_checker('молоко делили ледоколом'))
