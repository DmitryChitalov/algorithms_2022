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
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""

        if self.elems == []:
            self.elems.append([el])
            print(self.elems)
        elif len(self.elems[-1]) < 3:
            self.elems[-1].append(el)
            print(self.elems)
        else:
            self.elems.append([el])
            print(self.elems)

    def pop_out(self):
        if self.elems == []:
            return self.elems
        else:
            if len(self.elems[-1]) == 1:
                pop_elems = self.elems[-1].pop()
                self.elems.pop()
                return pop_elems
            else:
                1 < len(self.elems[-1]) <= 3
                return self.elems[-1].pop()

    def get_val(self):
        if self.elems == []:
            return None
        else:
            0 < len(self.elems[-1]) <= 3
            return self.elems[-1][len(self.elems[-1]) - 1]

    def stack_size(self):
        if self.elems == []:
            return 0
        elif len(self.elems[-1]) == 3:
            return len(self.elems) * 3
        elif len(self.elems[-1]) < 3:
            return (len(self.elems) - 1) * 3 + len(self.elems[-1])


if __name__ == '__main__':

    SC_OBJ = StackClass()

    print('Стек пустой: ', SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in("Тарелка 1")
    SC_OBJ.push_in('Тарелка 2')
    SC_OBJ.push_in('Тарелка 3')
    SC_OBJ.push_in('Тарелка 4')

    # получаем значение первого элемента с вершины стека,
    # но не удаляем сам элемент из стека
    print('Значение первого элемента с вершины стека: ', SC_OBJ.get_val())  # -> 'Тарелка 4'

    # узнаем размер стека
    print('Размер стека: ', SC_OBJ.stack_size())  # -> 4

    print('Стек пустой: ', SC_OBJ.is_empty())  # -> стек уже непустой

    # кладем еще три элемента в стек
    print("Кладем еще 3 элемента в стек.")
    SC_OBJ.push_in('Тарелка 5')
    SC_OBJ.push_in('Тарелка 6')
    SC_OBJ.push_in('Тарелка 7')

    # убираем элемент с вершины стека и возвращаем его значение
    print('Убираем элемент с вершины стека и возвращаем его значение: ', SC_OBJ.pop_out())  # -> 'Тарелка 5'

    # снова убираем элемент с вершины стека и возвращаем его значение
    print('Убираем элемент с вершины стека и возвращаем его значение: ',SC_OBJ.pop_out())  # -> 'Тарелка 4'

    # вновь узнаем размер стека
    print('Вновь узнаем размер стека: ', SC_OBJ.stack_size())  # -> 5

    # кладем еще один элемент в стек
    print("Кладем еще 1 элемент в стек.")
    SC_OBJ.push_in('Тарелка 8')

    # узнаем размер стека
    print('Узнаем размер стека: ', SC_OBJ.stack_size())  # -> 6