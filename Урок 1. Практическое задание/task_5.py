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
        self.elems = [[], [], [], [], []]

    def push_in(self, el):
        for i in range(0, len(self.elems) - 1, 1):
            if len(self.elems[i]) < 5:
                self.elems[i].append(el)
                break

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


class Stack:
    def __init__(self):
        self.stack = []
        self.max = None

    def push(self, item):
        self.stack.append(item)
        if len(self.stack) == 1 or item > self.max:
            self.max = item


if __name__ == '__main__':
    stack_1 = StackClass()
    i = 0
    while i < 18:
        stack_1.push_in(1 + i)
        i += 1

    print(stack_1.elems)
