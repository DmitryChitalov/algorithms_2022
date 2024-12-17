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
        """Инициализация пустого массива"""
        self.items = []

    def is_empty(self):
        """Проверка, пуст ли массив"""
        self.items == []

    def add_to_front(self, item):
        """Добавление элемента в конец массива"""
        self.items.append(item)

    def add_to_rear(self, item):
        """Добавление элемента в начало массива"""
        self.items.insert(0, item)

    def remove_from_front(self):
        """Удаление последнего элемента из массива и его возврат"""
        return self.items.pop()

    def remove_from_rear(self):
        """Удаление первого элемента из массива и его возврат"""
        return self.items.pop(0)

    def size(self):
        """Получение длины массива"""
        return len(self.items)


def palindrom_checker(string: str):
    dc_obj = DequeClass()
    for char in string:
        dc_obj.add_to_rear(char)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


# Тестируем функцию
print(palindrom_checker('топот'))  # True
print(palindrom_checker('ротор'))  # True
print(palindrom_checker('молоко делили ледоколом'))  # True
print(palindrom_checker('привет'))  # False
print(palindrom_checker('топот молоко'))  # False
print(palindrom_checker('потом'))  # False
