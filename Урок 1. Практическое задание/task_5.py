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
        self.elems = [[]]
        self.id = 0

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems[self.id].append(el)
        if len(self.elems[self.id]) == 5:
            self.elems.append([])
            self.id += 1

    def pop_out(self):
        if len(self.elems) > 1 and self.elems[self.id] == []:
            self.elems.pop()
            self.id -= 1
        return self.elems[self.id].pop()

    def get_val(self):
        return self.elems[self.id][-1]

    def stack_size_all(self):
        return len(self.elems)

    def stack_size_id(self):
        return len(self.elems[self.id])


if __name__ == '__main__':

    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(34.5)
    SC_OBJ.push_in(4.5)
    SC_OBJ.push_in(5.3)

    # получаем значение первого элемента с вершины стека,
    # но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())  # -> 5.3

    # узнаем размер стека (количество стопок)
    print(SC_OBJ.stack_size_all())  # -> 2

    print(SC_OBJ.is_empty())  # -> стек уже непустой

    # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)

    # убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 4.4

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 5.3

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 4.5

    # узнаем размер стопки стека
    print(SC_OBJ.pop_out())  # -> 34.5

    # узнаем размер стопки стека
    print(SC_OBJ.stack_size_id())  # -> 4


