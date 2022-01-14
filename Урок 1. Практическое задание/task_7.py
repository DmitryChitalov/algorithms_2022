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

class Deque:
    def __init__(self):
        self.elems = []

    def put_to_head(self, elem):
        self.elems.append(elem)

    def put_to_tail(self, elem):
        self.elems.insert(0, elem)

    def get_from_head(self):
        return self.elems.pop()

    def get_from_tail(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)

def pal_checker(string):
    deque = Deque()

    for el in string:
        deque.put_to_head(el)

    still_equal = True

    while deque.size() >= 2 and still_equal:
        first_is_space = True
        last_is_space = True
        while deque.size() >= 2 and first_is_space:
            first = deque.get_from_head()
            first_is_space = (first == ' ')

        while deque.size() >= 1 and last_is_space:
            last = deque.get_from_tail()
            last_is_space = (last == ' ')
        
        is_remain_one_char = (last_is_space and not first_is_space or 
                              not last_is_space and first_is_space)

        if last != first and not is_remain_one_char:
            still_equal = False
            break

    return still_equal

print(pal_checker("молоко делили ледоколом"))