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
        self.full = 2  # величина стопки
        self.elems = [[]]

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[-1]) < self.full:
            return self.elems[-1].append(el)
        else:
            return self.elems.append([el])

    def pop_out(self):
        if len(self.elems[-1]) == 1:
            return self.elems.pop().pop()
        else:
            return self.elems[-1].pop()

    def get_val(self):
        return self.elems[-1][-1]

    def stack_size(self):
        if len(self.elems[-1]) == 2:
            return len(self.elems) * self.full
        else:
            return len(self.elems) * self.full - 1


if __name__ == '__main__':
    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in('word')
    SC_OBJ.push_in(20)
    SC_OBJ.push_in('hello')

    # получаем значение первого элемента с вершины стека,
    # но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())  # -> hello

    # узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 7

    print(SC_OBJ.is_empty())  # -> стек уже непустой

    # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)

    # убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 4.4

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> hello

    # вновь узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 6

    # посмотрим элементы в стеке
    print(SC_OBJ.elems)
