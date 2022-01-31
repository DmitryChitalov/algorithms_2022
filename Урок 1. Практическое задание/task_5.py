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
        self.elems = [[]]

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[len(self.elems) - 1]) > 0:
            if len(self.elems[len(self.elems) - 1]) < 3:
                self.elems[len(self.elems) - 1].append(el)
            else:
                self.elems.append([el])
        else:
            self.elems[0].append(el)
        print(f'added', el)

    def pop_out(self):
        if len(self.elems[len(self.elems)-1]) == 1:
            self.elems[len(self.elems)-1].pop()
            self.elems.pop()
        else:
            self.elems[len(self.elems) - 1].pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems[len(self.elems) - 1])

    def stack_count(self):
        return len(self.elems)


if __name__ == '__main__':
    SC_OBJ = StackClass()
    print(f'stack empty', SC_OBJ.is_empty())
    SC_OBJ.push_in(10)
    print(f'stack empty', SC_OBJ.is_empty())
    print(f'stack size is', SC_OBJ.stack_size())
    print(f'stack last el is', SC_OBJ.get_val())
    SC_OBJ.push_in(11)
    print(f'stack size is', SC_OBJ.stack_size())
    print(f'stack is', SC_OBJ.elems)
    SC_OBJ.push_in(12)
    print(f'stack size is', SC_OBJ.stack_size())
    print(f'stack is', SC_OBJ.elems)
    SC_OBJ.push_in(13)
    print(f'stack is', SC_OBJ.elems)
    print(f'stack count is', SC_OBJ.stack_count())
    print(f'stack is', SC_OBJ.elems)
    SC_OBJ.push_in(14)
    print(f'stack count is', SC_OBJ.stack_count())
    print(f'stack is', SC_OBJ.elems)
    SC_OBJ.push_in(15)
    print(f'stack count is', SC_OBJ.stack_count())
    print(f'stack is', SC_OBJ.elems)
    SC_OBJ.push_in(16)
    print(f'stack count is', SC_OBJ.stack_count())
    print(f'stack is', SC_OBJ.elems)
    SC_OBJ.pop_out()
    print(f'stack is', SC_OBJ.elems)
    SC_OBJ.pop_out()
    print(f'stack is', SC_OBJ.elems)
    SC_OBJ.pop_out()
    print(f'stack is', SC_OBJ.elems)
    SC_OBJ.pop_out()
    print(f'stack is', SC_OBJ.elems)
    SC_OBJ.pop_out()
    print(f'stack is', SC_OBJ.elems)
