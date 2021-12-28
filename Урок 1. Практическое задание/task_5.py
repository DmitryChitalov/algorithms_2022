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
class Stack_of_plates:

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
        # return None

    def get_val(self):
        return self.elems[-1][-1]
        # return None

    def stack_size(self):
        full_len = 0
        for i in self.elems:
            # print(len(i))
            full_len += len(i)
        return full_len
        # return None

    def show_stack(self):
        return self.elems
        # return None

stack = Stack_of_plates()

for i in range(1,21):
    stack.push_in(i)

print(stack.show_stack())
print(stack.pop_out())
print(stack.show_stack())
print(stack.get_val())
print(stack.stack_size())
print(stack.is_empty())
