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
    PILE_MAX_SIZE = 4  

    class Pile:
        def __init__(self):
            self.elems = []

        def push(self, el):
            self.elems.append(el)

        def pop(self):
            return self.elems.pop()

        def stack_size(self):
            return len(self.elems)  

    def __init__(self):
        self.piles = [self.__class__.Pile()]

    def push(self, el):
        if self.piles[-1].stack_size() == self.__class__.PILE_MAX_SIZE:
            self.piles.append(self.__class__.Pile())
        self.piles[-1].elems.append(el)

    def pop(self):
        if self.piles[-1].stack_size() == 0:
            self.piles.pop()
        return self.piles[-1].elems.pop()

    def stack_size(self):
        stack_len = sum([p.stack_size() for p in self.piles])
        return stack_len

    def curent_pile_size(self):
        return self.piles[-1].stack_size()
    
    def piles_count(self):
        return len(self.piles)

stack = Stack()
stack.push(55)
stack.push(33)
print(stack.piles_count())
stack.push(101)
stack.push(101)
stack.push(101)
print(stack.piles_count())

    

    

        





