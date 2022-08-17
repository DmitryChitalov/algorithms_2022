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


class Stacks_of_Plates():
    quantity_stack = 0

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def add_stack(self, volume=1):
        Stacks_of_Plates.quantity_stack = volume
        self.stack.append([])

    def add_plate(self):
        if self.is_empty():
            self.add_stack()
        if Stacks_of_Plates.quantity_stack == 0:
            self.add_stack()
        self.stack[-1].append('+')
        Stacks_of_Plates.quantity_stack -= 1

    def pop_plate(self):
        if len(self.stack[-1]) == 0:
            self.stack.pop()
            self.stack[-1].pop()
            Stacks_of_Plates.quantity_stack = 1
        elif len(self.stack[-1]) == 1:
            self.stack[-1].pop()
            self.stack.pop()
            Stacks_of_Plates.quantity_stack = 0
        else:
            self.stack[-1].pop()
            Stacks_of_Plates.quantity_stack += 1

    def __str__(self):
        return f'{self.stack}'

