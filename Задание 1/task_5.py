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
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

class MyStackClass:
    def __init__(self, limit):
        self.limit = limit # предельный размер текущего стека
        self.elems = [] # текущий стек
        self.list_elems = [] # стек стеков

    def is_empty(self):
        return self.elems == [] and self.list_elems == []

    def push_in(self, el):
        # если текущий стек заполнен, поместить его в стек стеков и создать новый текущий стек
        if len(self.elems) == self.limit:
            self.list_elems.append(self.elems)
            self.elems = []
        self.elems.append(el)

    def pop_out(self):
        # если текущий стек пустой, извлечь из стека стеков предыдущий текущий и работать с ним
        # если стек стеков пустой, возвратить None 
        if self.elems == []:
            if self.list_elems == []:
                return None
            else:
                self.elems = self.list_elems.pop()
        return self.elems.pop()

    def get_val(self):
        # если текущий стек пустой, извлечь из стека стеков предыдущий и работать с ним
        # если стек стеков пустой, возвратить None 
        if self.elems == []:
            if self.list_elems == []:
                return None
            else:
                self.elems = self.list_elems.pop()
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.list_elems) * self.limit + len(self.elems)

stack = MyStackClass(3)
print(stack.get_val())
stack.push_in(11)
print(stack.get_val())
stack.push_in(12)
stack.push_in(13)
stack.push_in(14)
print(stack.stack_size())
print(stack.get_val())
print(stack.pop_out())
print(stack.stack_size())
print(stack.pop_out())
print(stack.stack_size())
print(stack.pop_out())
print(stack.stack_size())
print(stack.pop_out())
print(stack.stack_size())
print(stack.pop_out())
print(stack.stack_size())
