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

class StackPlateClass:

    def __init__(self):
        self.elems = [[]]
        self.fullsize = 5

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[-1]) < self.fullsize:
            return self.elems[-1].append(el)
        else:
            return self.elems.append([el])

    def pop_out(self):
        if len(self.elems[-1]) == 1:
            return self.elems.pop().pop()
        else:
            return self.elems[-1].pop()

    def get_val(self):
        return self.elems[-1][-1]

    def stack_size(self):
        if len(self.elems[-1]) == self.fullsize:
            return len(self.elems) * self.fullsize
        else:
            return len(self.elems) * self.fullsize - (self.fullsize - len(self.elems[-1]))


if __name__ == '__main__':
    SPC = StackPlateClass()

    print(SPC.is_empty())                

    SPC.push_in('Hello')
    SPC.push_in('world')
    SPC.push_in('!!!')
    SPC.push_in(111)
    SPC.push_in('@')
    SPC.push_in('65')
    SPC.push_in(7)

    print(SPC.get_val())

    print(SPC.stack_size())

    print(SPC.is_empty())

    SPC.push_in('?')

    print(SPC.get_val())

    print(SPC.stack_size())

    print(SPC.pop_out())

    print(SPC.stack_size())

    print(SPC.elems)