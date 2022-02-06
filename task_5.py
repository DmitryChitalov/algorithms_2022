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
    def __init__(self):
        self.stack = [[]]
        self.max = 3

    def is_empty(self):
        return self.stack == [[]]

    def push_in(self, item):
        if len(self.stack[len(self.stack) - 1]) < self.max:
            self.stack[len(self.stack) - 1].append(item)
        else:
            self.stack.append([])
            self.stack[len(self.stack) - 1].append(item)

    def pop_out(self):
        if len(self.stack) == 0:
            return "Стек пуст"
        return self.stack[len(self.stack) - 1].pop()

    def get_val(self):
        return self.stack[len(self.stack) - 1]

    def stack_size(self):
        return len(self.stack)


if __name__ == '__main__':

    SC_OBJ = StackClass()

    SC_OBJ.push_in(1)
    SC_OBJ.push_in(2)
    SC_OBJ.push_in(3)

    print(SC_OBJ.stack_size())

    SC_OBJ.push_in(4)
    SC_OBJ.push_in(5)
    SC_OBJ.push_in(6)

    print(SC_OBJ.pop_out())

    print(SC_OBJ.stack)
