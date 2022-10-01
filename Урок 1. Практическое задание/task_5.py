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

class PlatesClass:
    def __init__(self):
        self.elems = []
        self.max = 10

    def is_empty(self):
        if self.elems == []:
            return True
        else:
            return False

    def push_in(self, el):
        if len(self.elems[len(self.elems) - 1]) < self.max:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        if len(self.elems) == 0:
            return "Стек пуст"
        return self.elems[len(self.elems) - 1].pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':

    PlatesStack = PlatesClass()

    PlatesStack.push_in(1)
    PlatesStack.push_in(2)
    PlatesStack.push_in(3)
    PlatesStack.push_in(4)
    PlatesStack.push_in(5)

    print(PlatesStack.stack_size())

    print(PlatesStack.pop_out())

    print(PlatesStack.stack_size())