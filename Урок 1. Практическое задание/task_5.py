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
        return self.elems == []

    def push_in(self, el):
        global i
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        for i in range(len(self.elems)):
            if len(self.elems[i]) < qs:
                self.elems[i].append(el)
                break
        if len(self.elems[i]) == qs:
            self.elems.append([])

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


def plates(tq):
    SC_OBJ = StackClass()
    for i in range(tq):
        SC_OBJ.push_in(i + 1)
    return SC_OBJ.elems


qs = 4  # количество в одной стопке
# tq = 21 суммарное количество тарелок

print(plates(21))
