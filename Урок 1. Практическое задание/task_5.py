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


class StackPlates:
    def __init__(self, max_size):
        self.elems = [[]]
        self.max_size = max_size

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[-1]) < self.max_size:
            self.elems[-1].append(el)
        else:
            self.elems.append([])
            self.elems[-1].append(el)

    def pop_out(self):
        res = self.elems[-1].pop()
        if len(self.elems[-1]) == 0:
            self.elems.pop()

        return res

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        sum_plates = 0
        for item in self.elems:
            sum_plates += len(item)

        return sum_plates

    def stack_count(self):
        return len(self.elems)

    def __str__(self):
        return str(self.elems)


if __name__ == '__main__':
    plates_1 = StackPlates(3)
    print(plates_1.is_empty())
    plates_1.push_in('Plate1')
    plates_1.push_in('Plate2')
    plates_1.push_in('Plate3')
    plates_1.push_in('Plate4')
    plates_1.push_in('Plate5')
    print(plates_1.get_val())
    print(plates_1.stack_count())
    print(plates_1.stack_size())
    print(plates_1.pop_out())
    print(plates_1)
