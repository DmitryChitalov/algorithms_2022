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


class StackOfPlates:
    def __init__(self):
        self.stack = [[]]
        self.amount_of_ones = 0

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)

    def push_in(self, item):
        self.stack[self.amount_of_ones].append(item)
        if len(self.stack[self.amount_of_ones]) == 5:
            self.stack.append([])
            self.amount_of_ones += 1

    def pop(self):
        if len(self.stack) > 1 and self.stack[self.amount_of_ones] == []:
            self.stack.pop()
            self.amount_of_ones -= 1
        return self.stack[self.amount_of_ones].pop()


plates = StackOfPlates()
plates.push_in('Plate1')
plates.push_in('Plate2')
plates.push_in('Plate3')
plates.push_in('Plate4')
plates.push_in('Plate5')
print(plates.pop())
print(plates.stack_size())
print(plates.stack)
