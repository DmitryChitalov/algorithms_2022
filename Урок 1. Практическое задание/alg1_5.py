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


class PlateStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.lst = []

    def is_empty(self):
        return self.lst == []

    def push_in(self, el):
        if self.is_empty() or len(self.lst[-1]) == self.max_size:
            self.lst.append([])
        self.lst[-1].append(el)

    def pop_out(self):
        el = self.lst[-1].pop()
        if len(self.lst[-1]) == 0:
            self.lst.pop()
        return el

    def get_val(self):
        print(self.lst[len(self.lst) - 1])

    def stack_size(self):
        size_list = []
        for el in self.lst:
            size_list.append(len(el))
        return size_list


stack = PlateStack(10)

print(stack.is_empty())
for i in range(68):
    stack.push_in(i)

print(stack.stack_size())

stack.get_val()

print(stack.pop_out())
print(stack.pop_out())
print(stack.pop_out())

print(stack.stack_size())
stack.get_val()

print(stack.is_empty())
