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

"""Пример создания стека через ООП"""


class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        print('Стек пустой?: ')
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if (self.elems == []) is True:
            self.elems.append([])
        if len(self.elems[-1+1]) < 7:
            self.elems[-1+1].append(el)
        elif len(self.elems[-1]) < 7:
            self.elems[-1].append(el)
        if len(self.elems[-1]) == 7:
            self.elems.append([])

    def pop_out(self):
        return self.elems[-1+1].pop() if (self.elems[-1] == []) is True \
            else self.elems[-1].pop()

    def get_val(self):
        return self.elems[-1+1] if (self.elems[-1] == []) is True \
            else self.elems[-1][-1]

    def stack_size(self):
        return len(self.elems[-1+1]) if (self.elems[-1] == []) is True \
            else len(self.elems[-1])


if __name__ == '__main__':

    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)

    # получаем значение первого элемента с вершины стека,
    # но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())  # -> 5.5

    # узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 4
    #
    print(SC_OBJ.is_empty())  # -> стек уже непустой
    #
    # # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)
    #
    # убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 4.4
    #
    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 5.5
    #
    SC_OBJ.push_in('тарелка1')
    SC_OBJ.push_in('тарелка2')
    SC_OBJ.push_in('тарелка3')
    SC_OBJ.push_in('тарелка4')
    SC_OBJ.push_in('тарелка5')
    SC_OBJ.push_in('тарелка6')
    SC_OBJ.push_in('тарелка7')
    SC_OBJ.push_in('тарелка8')
    print(SC_OBJ.pop_out())


    # вновь узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 3