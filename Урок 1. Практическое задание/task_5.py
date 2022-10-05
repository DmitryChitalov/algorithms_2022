"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class PlatesStack:
    def __init__(self, limit):
        self.limit = limit
        self.stack = [[]]

    def __str__(self):
        return str(self.stack)

    def __len__(self):
        count = (len(self.stack) - 1) * self.limit
        count += len(self.stack[-1])
        return count

    def add(self):
        if len(self.stack[-1]) == self.limit:
            self.stack.append([])
            self.stack[-1].append('plate')
        else:
            self.stack[-1].append('plate')

    def remove(self):
        if len(self.stack[-1]) > 0:
            self.stack[-1].pop()
        if len(self.stack[-1]) == 0 and len(self.stack) > 1:
            self.stack.pop()


plates = PlatesStack(3)
print(type(plates))

plates.add()
plates.add()
plates.add()
plates.add()
plates.add()
print(len(plates))
print(plates)
print(plates.remove())
print(plates.remove())
print(plates.remove())
print(plates.remove())
print(plates.remove())
print(plates.remove())
print(plates.remove())
print(plates.remove())
# print(plates.get_val())
# print(plates.stack_size())
# print(plates.stack_count())
# print(plates)
