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
        self.chars = []

    def is_empty(self):
        return not self.chars

    def add_to_start(self, elem):
        self.chars.insert(0, elem)

    def add_to_end(self, elem):
        self.chars.append(elem)

    def remove_from_end(self):
        return self.chars.pop(0)

    def remove_from_start(self):
        return self.chars.pop()

    def size(self):
        return len(self.chars)

def pal_checker(string):
    original_string = string
    dc_obj = Deque()
    string = ''.join(string.split())

    for el in string:
        dc_obj.add_to_end(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_start()
        last = dc_obj.remove_from_end()
        if first != last:
            still_equal = False
    if still_equal:
        return f'Строка "{original_string}" - Палиндром'
    else:
        return f'Строка "{original_string}" - Не палиндром'

print(pal_checker("молоко делили ледоколом"))