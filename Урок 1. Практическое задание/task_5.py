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


#################################################################
class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if self.is_empty():
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)
        elif len(self.elems[len(self.elems) - 1]) < 5:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        while not self.is_empty():
            if self.elems[(len(self.elems) - 1)] == []:
                self.elems.pop()
            else:
                return self.elems[len(self.elems) - 1].pop()
        else:
            return self.is_empty()

    def get_val(self):
        if len(self.elems) > 1:
            return self.elems[len(self.elems) - 1][len(self.elems[len(self.elems) - 1]) - 1]
        else:
            while not self.elems[0]:
                return self.elems[0][len(self.elems[0]) - 1]

    def stack_size(self):
        if len(self.elems) > 1:
            return (len(self.elems) - 1) * 5 + len(self.elems[len(self.elems) - 1])
        else:
            while not self.elems[0]:
                return len(self.elems[len(self.elems) - 1])


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

    print(SC_OBJ.is_empty())  # -> стек уже непустой

    # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)

    # убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 4.4

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 5.5

    # вновь узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 3

    # test
    print(SC_OBJ.elems)
    print(SC_OBJ.stack_size())
    print(SC_OBJ.get_val())
    ###
    SC_OBJ.push_in(1)
    SC_OBJ.push_in(2)
    SC_OBJ.push_in(3)
    SC_OBJ.push_in(4)
    SC_OBJ.push_in(5)
    SC_OBJ.push_in(6)
    SC_OBJ.push_in(7)
    SC_OBJ.push_in(8)
    ###
    print(SC_OBJ.elems)
    print(SC_OBJ.stack_size())
    print(SC_OBJ.get_val())
    ###
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    #print(SC_OBJ.pop_out())
    #print(SC_OBJ.pop_out())
    ###
    print(SC_OBJ.elems)
    print(SC_OBJ.stack_size())
    print(SC_OBJ.get_val())
