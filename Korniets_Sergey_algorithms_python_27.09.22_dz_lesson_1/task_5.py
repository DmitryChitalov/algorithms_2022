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

class PlateStack:

    MAX_STACK = 10

    def __init__(self):
        self.stack = [[]]
        self.idx = 0
        self.coun = 0
        
    def is_empty(self):
        return self.coun == 0

    def push_in(self, plate):
        if len(self.stack[self.idx]) >= self.MAX_STACK:
            self.idx += 1
            self.stack.append([])

        self.stack[self.idx].append(plate)
        self.coun += 1

    def pop_out(self):
        item = self.stack[self.idx].pop()
        self.coun -= 1
        if len(self.stack[self.idx]) == 0:
            self.idx -= 1
        return item


    def get_val(self):
        return self.stack[len(self.stack) - 1]

    def stack_size(self):
        return self.coun

if __name__ == '__main__':
    ns = PlateStack()
    print(ns.is_empty())
    for x in range(22):
        ns.push_in(x)

    print(ns.stack)
    print(ns.idx)
    print(ns.coun)
    print(ns.pop_out())
    print(ns.stack)
    print(ns.get_val())
    print(ns.stack_size())

