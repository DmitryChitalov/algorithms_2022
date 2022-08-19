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

    def add_to_front(self, elem):  # добавляет элемент в конец
        self.elems.append(elem)

    def add_to_rear(self, elem):  # добавляет элемент в начало
        self.elems.insert(0, elem)

    def remove_from_front(self):  # удаляет последний элемент
        return self.elems.pop()

    def remove_from_rear(self):  # удаляет первый элемент
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


def pal_checker(string):
    dc_obj = DequeClass()
    new_string = string.replace(' ', '')  # заменили пробелы на ничего
    for el in new_string:  # идём по буквам и добавляем в dc_obj в начало, получаем в обратном порядке буквы
        dc_obj.add_to_rear(el)

    still_equal = True  # флажок

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()  # захватываем первую букву
        last = dc_obj.remove_from_rear()  # захватываем последнюю букву
        if first != last:  # если не равны, меняем флажок
            still_equal = False

    return still_equal


print(pal_checker("молоко делили ледоколом"))
