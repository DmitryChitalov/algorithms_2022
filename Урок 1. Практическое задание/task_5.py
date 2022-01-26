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

    def stack_size(self, s):
        self.size = s

    def push_in(self, el):
        if len(self.elems[len(self.elems) - 1]) > 0:
            if len(self.elems[len(self.elems) - 1]) < self.size:
                self.elems[len(self.elems) - 1].append(el)
            else:
                self.elems.append([el])
        else:
            self.elems[0].append(el)

    def pop_out(self):
        return self.elems.pop()


SC_OBJ = StackClass()
SC_OBJ.stack_size(3)  # определяем размер стопки
SC_OBJ.push_in(10)
SC_OBJ.push_in(5)
SC_OBJ.push_in(6)
SC_OBJ.push_in(7)
SC_OBJ.push_in(23)
SC_OBJ.push_in(7)
SC_OBJ.push_in(98)
print(SC_OBJ.elems)
SC_OBJ.pop_out()
print(SC_OBJ.elems)
