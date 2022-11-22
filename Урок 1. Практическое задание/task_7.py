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

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


def palindrome_check(string):
    deque_string = DequeClass()
    edited_string = string.replace(' ', '')
    for char in edited_string:
        deque_string.add_to_rear(char)

    equal_chars = True
    while deque_string.size() > 1 and equal_chars:
        first_char = deque_string.remove_from_front()
        last_char = deque_string.remove_from_rear()
        if first_char != last_char:
            equal_chars = False

    return equal_chars


print(palindrome_check("молоко делили ледоколом"))
