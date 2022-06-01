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

    def __init__(self, limit):
        self.limit = limit
        self.lst = []

    def is_empty(self):
        return self.lst == []

    def push_in(self, el):

        if self.is_empty() or len(self.lst[-1]) == self.limit:
            self.lst.append([])
        self.lst[-1].append(el)

    def pop_out(self):
        el = self.lst[-1].pop()
        if len(self.lst[-1]) == 0:
            del self.lst[-1]
        return el

    def get_val(self):
        return self.lst[-1][-1]

    def stack_size(self):
        size_list = []
        for st in self.lst:
            size_list.append(len(st))
        return size_list


if __name__ == '__main__':

    stack = StackOfPlates(10)
    print(stack.is_empty())
    for i in range(7):
        stack.push_in(i)

    print(stack.is_empty())
    print(stack.stack_size())

    print(stack.get_val())
    print(stack.pop_out())
    print(stack.pop_out())
    print(stack.get_val())

    print(stack.stack_size())