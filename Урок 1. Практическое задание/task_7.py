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
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_to_front(self, elem):
        self.items.append(elem)

    def add_to_rear(self, elem):
        self.items.insert(0, elem)

    def remove_from_front(self):
        return self.items.pop()

    def remove_from_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def pal_checker(string):
    dc_obj = DequeClass()

    # for el in string:
    #     if el == ' ':
    #         continue
    #     dc_obj.add_to_rear(el)

    for el in string.replace(' ', ''):
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:

        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()

        if first != last:
            still_equal = False

    return still_equal


if __name__ == '__main__':
    print(pal_checker("молоко делили ледоколом"))
