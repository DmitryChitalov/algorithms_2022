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
--создание новой стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""
class StackClass:

    def __init__(self):
        self.elems = [[]]
        self.fullsize = 3

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[-1]) < self.fullsize:
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
        if len(self.elems[-1]) == self.fullsize:
            return len(self.elems) * self.fullsize
        else:
            return len(self.elems) * self.fullsize - (self.fullsize - len(self.elems[-1]))


if __name__ == '__main__':
    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())                # -> True - стек пустой

    # наполнение стека
    SC_OBJ.push_in(1)
    SC_OBJ.push_in('one')
    SC_OBJ.push_in('один')
    SC_OBJ.push_in('2')
    SC_OBJ.push_in('two')
    SC_OBJ.push_in('два')
    SC_OBJ.push_in(3)
    SC_OBJ.push_in('three')

    # значение первого элемента с конца
    print(SC_OBJ.get_val())                 # -> three

    # размер стека
    print(SC_OBJ.stack_size())              # -> 8

    print(SC_OBJ.is_empty())                # -> False - стек не пустой

    # добавление еще одного элемента в стек
    SC_OBJ.push_in('три')

    # значение первого элемента с конца
    print(SC_OBJ.get_val())                 # -> три

    # размер стека
    print(SC_OBJ.stack_size())              # -> 9

    # удаление последнего элемента стека и вывод его значения
    print(SC_OBJ.pop_out())                 # -> три

    # удаление последнего элемента стека и вывод его значения
    print(SC_OBJ.pop_out())                 # -> three

    # размер стека
    print(SC_OBJ.stack_size())              # -> 7

    # элементы в стеке
    print(SC_OBJ.elems)                     # -> [[1, 'one', 'один'], ['2', 'two', 'два'], [3]]