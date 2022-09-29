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


class PlatesStacks:

    def __init__(self, num):
        self.elems = []
        self.num = num

    def is_empty(self):
        return not self.elems

    def push_in(self, element):
        if not self.is_empty() and len(self.elems[len(self.elems) - 1]) < self.num:
            self.elems[-1].append(element)
        else:
            self.elems.append([element])

    def pop_out(self):
        return self.elems[-1].pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        if self.is_empty():
            return 0
        return (len(self.elems) - 1) * self.num + len(self.elems[-1])


if __name__ == '__main__':
    ps = PlatesStacks(3)
    ps.push_in(212)
    ps.push_in(14)
    ps.push_in('ahaf')
    ps.push_in('123')
    ps.push_in('789')
    ps.push_in('qwet')
    print(ps.pop_out())
    print(ps.get_val())
    print(ps.stack_size())
