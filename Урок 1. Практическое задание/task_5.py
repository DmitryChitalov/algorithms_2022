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


class StackClass:
    def __init__(self, limit):
        self.elems = [[]]
        self.limit = limit

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        for i in range(len(self.elems)):
            if len(self.elems[i]) < self.limit:
                self.elems[i].append(el)
                if len(self.elems[i]) == self.limit:
                    self.elems.append([])
                break

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def print_stack(self):
        print(self.elems)


stack1 = StackClass(2)
stack1.push_in(23)
stack1.push_in(23)
stack1.push_in(23)
stack1.push_in(23)
stack1.push_in(23)
stack1.push_in(23)
stack1.push_in(23)
stack1.push_in(23)
stack1.push_in(23)

stack1.print_stack()
