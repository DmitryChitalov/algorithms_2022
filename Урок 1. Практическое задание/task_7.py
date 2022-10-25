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
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def add_to_front(self, elem):
        self.elements.insert(0, elem)

    def add_to_rear(self, elem):
        self.elements.append(elem)

    def remove_from_rear(self):
        return self.elements.pop()

    def remove_from_front(self):
        return self.elements.pop(0)

    def size(self):
        return len(self.elements)



def pal_check(pall):
    deque = Deque()

    for el in pall:
        if el == ' ': continue
        deque.add_to_rear(el)

    equal = True

    while deque.size() > 1 and equal:
        first = deque.remove_from_front()
        last = deque.remove_from_rear()
        if first != last:
            equal = False
        return equal



if __name__ == '__main__':
    print(pal_check("молоко делили ледоколом"))
    print(pal_check("молоко делили"))