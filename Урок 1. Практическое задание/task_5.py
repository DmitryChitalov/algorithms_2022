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


class StackOfPlates:
    def __init__(self):
        self.plates = [[]]

    def is_empty(self):
        return self.plates == [[]]

    def push_in(self, el):
        if len(self.plates[0]) > 9:
            self.plates.insert(0, [])
        self.plates[0].append(el)

    def pop_out(self, s):
        return self.plates[s].pop()

    def stack_size(self, s):
        return len(self.plates[s])

    def plates(self):
        return self.plates


if __name__ == '__main__':

    SC_OBJ = StackOfPlates()

    print(SC_OBJ.is_empty())

    print(SC_OBJ.plates)

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
    SC_OBJ.push_in('plate')
    SC_OBJ.push_in('plate')
    SC_OBJ.push_in('plate')

    print(SC_OBJ.stack_size(1))
    print(SC_OBJ.stack_size(0))

    print(SC_OBJ.is_empty())

    print(SC_OBJ.pop_out(0))
    print(SC_OBJ.pop_out(1))
    print(SC_OBJ.pop_out(1))

    SC_OBJ.push_in('plate')

    print(SC_OBJ.stack_size(0))

    print(SC_OBJ.plates)
