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
from collections import deque as dq


# Дек с урока
class DequeClass:
    def __init__(self, sequence):
        self.elems = list(sequence)

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


def pal_check(string):
    lesson_deque = DequeClass(string.lower().replace(' ', ''))
    checker = True
    while lesson_deque.size() > 1 and checker:
        first = lesson_deque.remove_from_front()
        last = lesson_deque.remove_from_rear()
        if first != last:
            checker = False
    return checker


# Встроенный дек
def is_palindrome(text: str) -> bool:
    clear_text = text.replace(' ', '').lower()
    deque = dq(clear_text)
    while len(deque) != 0:
        if len(deque) == 1:
            break
        if deque.pop() == deque.popleft():
            continue
        return False
    return True


if __name__ == '__main__':
    assert pal_check("молоко делили ледоколом") is True
    assert is_palindrome('молоко делили ледоколом') is True
    print(is_palindrome('молоко делили ледоколом'))
    assert pal_check('Alla') is True
    assert is_palindrome('Alla') is True
    print(is_palindrome('Alla'))
    assert pal_check('All') is False
    assert is_palindrome('All') is False
    print(is_palindrome('All'))
