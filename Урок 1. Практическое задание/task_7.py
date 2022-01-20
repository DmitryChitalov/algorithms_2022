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


class MyDeque:
    def __init__(self):
        self.els = []

    def to_front(self, el):
        self.els.append(el)

    def to_rear(self, el):
        self.els.insert(0, el)

    def from_rear(self):
        return self.els.pop()

    def from_front(self):
        return self.els.pop(0)

    def size(self):
        return len(self.els)

    @staticmethod
    def pal_checker(string):
        string = string.replace(" ", "")
        for el in string:
            deque.to_rear(el)
        pal = True  # паллиндром
        while deque.size() > 1 and pal:
            first = deque.from_front()
            last = deque.from_rear()
            if first != last:
                pal = False
        return pal


if __name__ == '__main__':
    deque = MyDeque()
    print(deque.pal_checker("молоко делили ледоколом"))
