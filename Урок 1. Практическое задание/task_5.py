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
        self.list = []
        self.size = 2

    def add(self, i):
        if len(self.list) == 0 or len(self.list[len(self.list) - 1]) == self.size:
            self.list.append([i])
        else:
            self.list[len(self.list) - 1].append(i)

    def delete(self):
        if len(self.list[len(self.list) - 1]) == 1:
            self.list.pop()
        else:
            self.list[len(self.list) - 1].pop()

    def last_elem(self):
        if len(self.list) == 0:
            print('Стек пуст!')
        else:
            print(self.list[len(self.list) - 1][len(self.list[len(self.list) - 1]) - 1])

    def size_list(self):
        print(f"Всего стопок: " + str(
            self.size * (len(self.list) - 1) + len(self.list[len(self.list) - 1])))
        print(f"Всего стеков: " + str(len(self.list)))
        print(f"Тарелок в последней стопке: " + str(len(self.list[len(self.list) - 1])))

    def print_stack(self):
        print(self.list)


new_stack = Stack()

new_stack.add(1)
new_stack.add(2)
new_stack.add(3)
new_stack.add(4)
new_stack.add(5)
new_stack.print_stack()
new_stack.size_list()
new_stack.delete()
new_stack.print_stack()
new_stack.size_list()
new_stack.add(6)
new_stack.add(7)
new_stack.add(8)
new_stack.add(9)
new_stack.add(10)
new_stack.print_stack()
new_stack.last_elem()
new_stack.size_list()
