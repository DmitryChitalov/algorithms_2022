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


class PlateStackClass:
    def __init__(self, max_size: int):
        self.elems = []
        self.max_size = max_size

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return len(self.elems) == [[]]

    def push_in(self, item):
        if len(self.elems[-1]) < self.max_size:
            self.elems[len(self.elems) - 1].append(item)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(item)

    def pop_out(self):
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_value(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        elem_sum = 0
        for stack in self.elems:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        return len(self.elems)


if __name__ == '__main__':
    plates = PlateStackClass(3)
    print(type(plates))
    plates.push_in('Plate1')
    plates.push_in('Plate2')
    plates.push_in('Plate3')
    plates.push_in('Plate4')
    plates.push_in('Plate5')
    print(plates)
    print(plates.pop_out())
    print(plates.get_value())
    print(plates.stack_count())
    print(plates.stack_count())
    print(plates)
