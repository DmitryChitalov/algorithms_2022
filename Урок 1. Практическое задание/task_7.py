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

class DequeClass:
    def __init__(self):
        self.elem = []

    def is_empty(self):
        return self.elem == []

    def add_to_front(self, elem):
        self.elem.append(elem)

    def add_to_rear(self, elem):
        self.elem.insert(0, elem)

    def remove_from_front(self):
        return self.elem.pop()

    def remove_from_rear(self):
        return self.elem.pop(0)

    def size(self):
        return len(self.elem)

def pal_checker(string):
    string = string.replace(" ", "")
    dc_obj = DequeClass()

    for elem in string:
        dc_obj.add_to_rear(elem)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal

if __name__ == '__main__':
    print(pal_checker('молоко делили ледоколом'))









