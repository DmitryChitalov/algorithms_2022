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

    def stack_size(self):
        return len(self.elems)

    def push_in(self, el):
        if self.is_empty() or len(self.elems[self.stack_size() - 1]) == 2:  # указываем, что пороговое значение стопки == 2, для примера
            nlist = []
            nlist.append(el)
            self.elems.append(nlist)
        else:
            self.elems[(self.stack_size() - 1)].append(el)

    def pop_out(self):
        if len(self.elems[self.stack_size() - 1]) == 1:
            self.elems.pop()
        else:
            self.elems[self.stack_size() - 1].pop()


    def get_val(self):
        return self.elems[self.stack_size() - 1][len(self.elems[len(self.elems) - 1]) - 1]


if __name__ == '__main__':

    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty()) # стек пустой
    SC_OBJ.push_in(1) # добавление элементов в стек
    SC_OBJ.push_in(2)
    print(SC_OBJ.get_val()) # последний добавленный в стек элемент
    SC_OBJ.push_in(3) # добавление элементов в стек
    print(SC_OBJ.get_val()) # последний добавленный в стек элемент
    SC_OBJ.push_in(4) # добавление элементов в стек
    SC_OBJ.push_in(5)
    SC_OBJ.push_in(6)
    print(SC_OBJ.get_val()) # последний добавленный в стек элемент
    SC_OBJ.pop_out() # удаление элемента из стека
    print(SC_OBJ.get_val())
    SC_OBJ.pop_out()
    print(SC_OBJ.get_val())
    SC_OBJ.pop_out()
    print(SC_OBJ.get_val())
    SC_OBJ.pop_out()
    SC_OBJ.pop_out()
    print(SC_OBJ.is_empty()) # стек пустой
    print(SC_OBJ.get_val())
    SC_OBJ.pop_out()
    print(SC_OBJ.is_empty())