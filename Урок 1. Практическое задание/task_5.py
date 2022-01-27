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


class MyStack:
    def __init__(self):
        self.stack_list = []
        self.N = 3

    def add(self, new_elem):
        if len(self.stack_list) == 0 or len(self.stack_list[len(self.stack_list) - 1]) == self.N:
            self.stack_list.append([new_elem])
        else:
            self.stack_list[len(self.stack_list) - 1].append(new_elem)

    def delete(self):
        if len(self.stack_list[len(self.stack_list) - 1]) == 1:
            self.stack_list.pop()
        else:
            self.stack_list[len(self.stack_list) - 1].pop()

    def last_elem(self):
        if len(self.stack_list) == 0:
            print('Стек пуст!')
        else:
            print(self.stack_list[len(self.stack_list) - 1][len(self.stack_list[len(self.stack_list) - 1]) - 1])

    def size(self):
        if len(self.stack_list) == 0:
            print('Стек пуст!')
        else:
            print(f"Всего элементов: " + str(
                self.N * (len(self.stack_list) - 1) + len(self.stack_list[len(self.stack_list) - 1])))
            print(f"Всего стеков: " + str(len(self.stack_list)))  # стопок
            print(f"В последней стопке: " + str(len(self.stack_list[len(self.stack_list) - 1])))

    def print_stack(self):
        print(self.stack_list)


new_stack = MyStack()

new_stack.add(3)
new_stack.add(3)
new_stack.add(3)
new_stack.add(333)
new_stack.add(333)
new_stack.print_stack()
new_stack.delete()
new_stack.print_stack()
new_stack.add(666)
new_stack.print_stack()
new_stack.last_elem()
new_stack.size()