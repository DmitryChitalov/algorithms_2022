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
        self.letters = []

    def is_empty(self):
        return self.letters == []

    def add_to_front(self, letter):
        self.letters.append(letter)

    def add_to_rear(self, letter):
        self.letters.insert(0, letter)

    def remove_from_front(self):
        return self.letters.pop()

    def remove_from_rear(self):
        return self.letters.pop(0)

    def size(self):
        return len(self.letters)


def checker(line):
    line = line.replace(' ', '')   # убираем пробелы
    deque_obj = DequeClass()

    for elem in line:
        deque_obj.add_to_rear(elem)

    equal = True
    while deque_obj.size() > 1 and equal:
        beginning_p = deque_obj.remove_from_front()
        last_p = deque_obj.remove_from_rear()
        if beginning_p != last_p:
            equal = False

    return equal


if __name__ == '__main__':
    print(checker("лёша на полке клопа нашёл"))
