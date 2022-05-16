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


def pal_checker(string):
    dc_obj = DequeClass()

    for el in set([_ for _ in string]):
        dc_obj.add_to_front(el)

    # FIX
    was_odd = False
    while dc_obj.size() > 0:
        first = dc_obj.remove_from_front()
        s = list(filter(lambda x: x == first, string))
        if s and len(s) % 2:
            if was_odd:
                return False
            else:
                was_odd = True
    return was_odd


print("%s[0]: %s" % ("pal_checker", pal_checker("молоко делили ледоколом")))
print("%s[1]: %s" % ("pal_checker", pal_checker("я выл плывя")))
print("%s[2]: %s" % ("pal_checker", pal_checker("пример не палиндрома")))
print("%s[3]: %s" % ("pal_checker", pal_checker("щетина ментов и живот не мани тещ")))
print("%s[4]: %s" % ("pal_checker", pal_checker("утро во рту")))
print("%s[5]: %s" % ("pal_checker", pal_checker("коса в киеве и квасок")))


# PEP Fix
def solver(__string):
    chars = set([_ for _ in __string])
    was_odd = False
    for char in chars:
        s = list(filter(lambda x: x == char, __string))
        if s and len(s) % 2:
            if was_odd:
                return False
            else:
                was_odd = True
    return True


# Доработать пример с урока - видел
print("%s[0]: %s" % ("Solver", solver("молоко делили ледоколом")))
print("%s[1]: %s" % ("Solver", solver("я выл плывя")))
print("%s[2]: %s" % ("Solver", solver("пример не палиндрома")))
print("%s[3]: %s" % ("Solver", solver("щетина ментов и живот не мани тещ")))
print("%s[4]: %s" % ("Solver", solver("утро во рту")))
print("%s[5]: %s" % ("Solver", solver("коса в киеве и квасок")))
