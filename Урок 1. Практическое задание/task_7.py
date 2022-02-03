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


def checking_for_palindrome_phrase_with_spaces(phrase):

    object_of_deque_class = DequeClass()
    phrase = "".join(phrase.split())
    for member in phrase:
        object_of_deque_class.add_to_rear(member)
    for index in range(len(phrase)//2):
        first_element_of_object_of_deque_class = object_of_deque_class.remove_from_front()
        last_element_of_object_of_deque_class = object_of_deque_class.remove_from_rear()
        if first_element_of_object_of_deque_class != last_element_of_object_of_deque_class:
            return "Эта фраза с пробелами не является полиндромом"
    return "Эта фраза с пробелами является полиндромом"


if __name__ == '__main__':
    print(checking_for_palindrome_phrase_with_spaces("молоко делили ледоколом"))
    print(checking_for_palindrome_phrase_with_spaces("лев с ума ламу свел"))
    print(checking_for_palindrome_phrase_with_spaces("чем нежен меч"))
    print(checking_for_palindrome_phrase_with_spaces("мат и тут и там"))
    print(checking_for_palindrome_phrase_with_spaces("топот"))
    print(checking_for_palindrome_phrase_with_spaces("уещузц узкешузщ впвап"))

