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


class StackClass:
    def __init__(self):
        self.elems = [[]]

    def create_stack(self):
        self.elems.append([])

    def get_not_filled_stack_index(self):
        last_index_stack = len(self.elems) - 1
        if self.stack_size(last_index_stack) < 5:
            return last_index_stack
        else:
            self.create_stack()
            return last_index_stack + 1

    def push_in(self, el):
        self.elems[self.get_not_filled_stack_index()].append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self, i):
        return len(self.elems[i])


if __name__ == '__main__':
    obj_stack = StackClass()

    i = 0
    while i < 28:
        obj_stack.push_in(1 + i)
        i += 1
    print(obj_stack.elems)

    obj_stack = StackClass()
    i = 0
    while i < 6:
        obj_stack.push_in(1 + i)
        i += 1

    print(obj_stack.elems)

    obj_stack = StackClass()
    i = 0
    while i < 10:
        obj_stack.push_in(1 + i)
        i += 1

    print(obj_stack.elems)

    obj_stack = StackClass()
    i = 0
    while i < 3:
        obj_stack.push_in(1 + i)
        i += 1

    print(obj_stack.elems)
