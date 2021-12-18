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
    kitchen_set = []

    def __init__(self, capacity=10):
        self.items = list()
        self.capacity = capacity

    def is_empty(self):
        return True if len(self.items) == 0 else False

    def push(self, item):
        if self.size() < self.capacity:
            self.items.append(item)
        else:
            Stack.kitchen_set.append(self.items[:self.capacity])
            self.items.clear()

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print('Empty Stack')

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print(f'Empty Stack')

    def size(self):
        return len(self.items)

    def __str__(self):
        return f'Stack of dishes: {self.items}'

    def __repr__(self):
        return f'{self.items}'


plate = 'P'
cup = 'C'
if __name__ == '__main__':
    kitchen_stack = Stack()
    for i in range(11):
        kitchen_stack.push(plate)
    for j in range(11):
        kitchen_stack.push(cup)
    for k in range(10):
        kitchen_stack.push(plate)
    print(Stack.kitchen_set)
    print(kitchen_stack)
