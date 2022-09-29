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


class StackOfPlates:
    def __init__(self):
        self.elems = [[]]

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[len(self.elems) - 1]) < 4:  # не больше 4-х тарелок в стопке
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':
    SC_OBJ = StackOfPlates()

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стопки
    SC_OBJ.push_in('plate 1')
    SC_OBJ.push_in('plate 2')
    SC_OBJ.push_in('plate 3')
    SC_OBJ.push_in('plate 4')
    SC_OBJ.push_in('plate 5')
    SC_OBJ.push_in('plate 6')
    SC_OBJ.push_in('plate 7')
    SC_OBJ.push_in('plate 8')
    SC_OBJ.push_in('plate 9')
    SC_OBJ.push_in('plate 10')
    SC_OBJ.push_in('plate 11')
    SC_OBJ.push_in('plate 12')
    SC_OBJ.push_in('plate 13')


    # смотрим какая тарелка лежит на вершине
    print(SC_OBJ.get_val())

    # узнаем количество стопок
    print(SC_OBJ.stack_size())

    print(SC_OBJ.is_empty())  # тарелки есть

