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

class Plates_stack:
    def __init__(self):
        self.elems = [[]]
        # self.lst_lst = self.elems[-1]


    def is_empty(self):
        return self.elems == []


    def push(self, el):

        if len(self.elems[-1]) == 3:
            self.elems.append([])
        return self.elems[-1].append(el)

    def pop(self):
        if self.elems:
            res = self.elems[-1].pop()
            if len(self.elems[-1]) == 0:
                self.elems.pop()
            return res
        else:
            return f'Тарелки отсутствуют'


    def get_val(self):
        if len(self.elems) > 0:
            return self.elems[-1][-1]
        else:
            return f'Тарелки отсутствуют'

    def stack_size(self):
        if len(self.elems) > 0:
            return f'{(len(self.elems)-1) * 3 + len(self.elems[-1])} шт. в {len(self.elems)} стопках(e)'
        else:
            return f'Тарелки отсутствуют'

if __name__ == '__main__':
    a = Plates_stack()

    a.push(1)
    a.push(2)
    a.push(3)
    a.push(4)
    a.push(5)
    a.push(6)
    a.push(7)
    a.push(8)
    a.push(9)
    a.push(10)
    a.push(15)
    # a.get_val()
    # a.pop()
    # a.get_val()
    # a.pop()
    # a.get_val()
    # a.stack_size()
    # a.pop()
    # a.stack_size()
    # a.push(10)
    # a.push(15)
    # a.stack_size()
    # a.is_empty()