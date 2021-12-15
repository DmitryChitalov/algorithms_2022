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


class StackOfPlates:
    def __init__(self):
        self.limit = 10
        self.lst = []

    def is_empty(self):
        return self.lst == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
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

    stack = StackOfPlates()

    print(stack.is_empty())
    for i in range(32):
        stack.push_in(i)

    print(stack.is_empty())
    print(stack.stack_size())

    print(stack.get_val())
    print(stack.pop_out())
    print(stack.pop_out())
    print(stack.get_val())

    print(stack.stack_size())
