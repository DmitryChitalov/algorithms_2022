"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""


class Stack:

    def __init__(self):
        self.elems = [[]]

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[-1]) < 5:
            self.elems[-1].append(el)
        else:
            self.elems.append([el])

    def pop_out(self):
        return self.elems[-1].pop()

    def get_val(self):
        return self.elems[-1][-1]

    def stack_size(self):
        full_len = 0
        for i in self.elems:
            full_len += len(i)
        return full_len

    def show_stack(self):
        return self.elems


stack = Stack()

for i in range(1, 21):
    stack.push_in(i)

print(stack.show_stack())
print(stack.pop_out())
print(stack.show_stack())
print(stack.get_val())
print(stack.stack_size())
print(stack.is_empty())