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
    """ Класс Дек """
    def __init__(self):
        self.elems = []

    def is_empty(self):
        """ Пустой список"""
        return not self.elems

    def add_to_front(self, elem):
        """ Добавление в голову """
        self.elems.append(elem)

    def add_to_rear(self, elem):
        """ Добавление в хвост"""
        self.elems.insert(0, elem)

    def remove_from_front(self):
        """ Удаление из головы"""
        return self.elems.pop()

    def remove_from_rear(self):
        """Удаление из хвоста"""
        return self.elems.pop(0)

    def size(self):
        """ Размер списка"""
        return len(self.elems)


if __name__ == "__main__":
    def pal_checker(string):
        """ Проверка на палиндром"""
        dc_obg = DequeClass()
        for elem in string.join(' '):
            dc_obg.add_to_rear(elem)
        still_equal = True
        while dc_obg.size() > 1 and still_equal:
            first = dc_obg.remove_from_front()
            last = dc_obg.remove_from_rear()
            if first != last:
                still_equal = False
        return still_equal
    print(pal_checker("молоко делили ледоколом"))
