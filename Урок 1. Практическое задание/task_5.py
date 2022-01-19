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
"""Пример создания стека через ООП"""

"""Пример создания стека через ООП"""


class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if (len(self.elems)-2) % 3 == 0:
            self.elems.append([])
            self.elems.append(el)
        else:
            self.elems.append(el)

    def show_full(self):
        return self.elems

    def pop_out(self):
        if self.elems[-1] == '[]':
            self.elems.pop()
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':
    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> стек пустой

    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    print(SC_OBJ.show_full())
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(5.5)
    print(SC_OBJ.show_full())

print(SC_OBJ.show_full())
print(SC_OBJ.pop_out())
print(SC_OBJ.show_full())
print(SC_OBJ.pop_out())
print(SC_OBJ.pop_out())
print(SC_OBJ.show_full())
print(SC_OBJ.pop_out())
print(SC_OBJ.show_full())