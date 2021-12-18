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
    def __init__(self, max_stack):
        self.elems = [[]]
        self.max_stack = max_stack

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        for i in range(len(self.elems)):
            if len(self.elems[i]) < self.max_stack:
                self.elems[i].append(el)
                if len(self.elems[i]) == self.max_stack:
                    self.elems.append([])
                break


    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def stack(self):
        print(self.elems)

if __name__ == '__main__':

    SC_OBJ = StackClass(5)
    SC_OBJ.push_in('plate')
    SC_OBJ.push_in('plate')
    SC_OBJ.push_in('plate')
    SC_OBJ.push_in('plate')
    SC_OBJ.push_in('plate')
    SC_OBJ.push_in('plate')
    SC_OBJ.push_in('plate')
    SC_OBJ.push_in('plate')
    SC_OBJ.push_in('plate')
    SC_OBJ.push_in('plate')
    SC_OBJ.push_in('plate')
    SC_OBJ.push_in('plate')
    SC_OBJ.stack()





