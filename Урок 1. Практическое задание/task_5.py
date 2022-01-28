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


class StackClass:
    def __init__(self, max_size):
        self.elems = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[-1]) < self.max_size:
            self.elems[-1].append(el)

        else:
            self.elems.append([])
            self.elems[-1].append(el)

    def pop_out(self):
        last_plate = self.elems[-1].pop()
        if len(self.elems[-1]) == 0:
            self.elems.pop()
        return last_plate

    def get_val(self):
        return self.elems[- 1][-1]

    def stack_size(self):
        cnt_elems = 0
        for el in self.elems:
            cnt_elems += len(el)
        return cnt_elems

    def cnt_stack(self):
        return len(self.elems)


if __name__ == '__main__':
    plates = StackClass(2)     # по 2 тарелки в стопке

    print(plates.is_empty())  # -> True

    # наполняем стек
    plates.push_in('Plate1')
    plates.push_in('Plate2')
    plates.push_in('Plate3')
    plates.push_in('Plate4')
    plates.push_in('Plate5')
    print(plates)

    # получаем значение первого элемента с вершины стека, не удаляя сам элемент из стека
    print(plates.get_val())  # -> Plate5

    # узнаем размер стека
    print(plates.stack_size())  # -> 5

    # узнаем количество стопок
    print(plates.cnt_stack())   # -> 3

    print(plates.is_empty())  # -> False

    # кладем еще один элемент в стек
    plates.push_in('Plate6')

    # убираем элемент с вершины стека и возвращаем его значение
    print(plates.pop_out())  # -> Plate6

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(plates.pop_out())  # -> Plate5

    # вновь узнаем размер стека
    print(plates.stack_size())  # -> 4

    # вновь узнаем количество стопок
    print(plates.cnt_stack())   # -> 2
