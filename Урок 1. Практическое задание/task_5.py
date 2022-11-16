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

from random import randint


class StackClass:
    def __init__(self):
        self.elems = [[]]
        self.max_stack_size = 2

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[-1]) == self.max_stack_size:
            return self.elems.append([el])
        else:
            return self.elems[-1].append(el)

    def pop_out(self):
        if len(self.elems[-1]) == 1:
            return self.elems.pop().pop()
        else:
            return self.elems[-1].pop()

    def get_val(self):
        return self.elems[-1][-1]

    def stack_size(self):
        if len(self.elems[-1]) == self.max_stack_size:
            return len(self.elems) * self.max_stack_size
        else:
            return len(self.elems) * self.max_stack_size - (self.max_stack_size - len(self.elems[-1]))


if __name__ == '__main__':
    SC_OBJ = StackClass()

    print(f'is_empty: {SC_OBJ.is_empty()}')

    rand_range = randint(8, 14)

    for i in range(rand_range):
        SC_OBJ.push_in(f'Тарелка {i + 1}')

    print(f'elems: {SC_OBJ.elems}')
    print(f'stack_size: {SC_OBJ.stack_size()}')
    print(f'get_val: {SC_OBJ.get_val()}')
    print(f'pop_out: {SC_OBJ.pop_out()}')
    print(f'elems: {SC_OBJ.elems}')
