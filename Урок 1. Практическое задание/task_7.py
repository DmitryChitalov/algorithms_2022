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


if __name__ == '__main__':
    def pal_checker(string_poli):
        obj = DequeClass()

        string = string_poli.replace(" ", "").replace(",", "").replace("-", "").replace(".", "").lower()
        for el in string:
            obj.add_to_rear(el)
        still_equal = f'"{string_poli}" - это полиндром.'
        while obj.size() > 1 and still_equal:
            first = obj.remove_from_front()
            last = obj.remove_from_rear()
            if first != last:
                still_equal = f'"{string_poli}" - это не полиндром.'
        return still_equal


    print(pal_checker('НаЖаЛ кАбАн На БаКлАжАн'))
    print(pal_checker('А лис, он умен - крыса сыр к нему носила.'))
    print(pal_checker('Роза упала на лапу Азора'))      # не полиндром, потому что в начале не хватает буквы А
