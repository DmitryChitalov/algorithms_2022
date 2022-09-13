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


class PiledPlatesClass:
    def __init__(self, max_size):
        self.itms = []
        self.max_size = max_size    

    def __str__(self):
        return str(self.itms)

    def is_empty(self):
        return self.itms == [[]]

    def push_in(self, el):
        if len(self.itms[len(self.itms)-1]) < self.max_size:
            self.itms[len(self.itms)-1].append(el)
        else:
            self.itms.append([])
            self.itms[len(self.itms) - 1].append(el)

    def pop_out(self):
        result = self.itms[len(self.itms) - 1].pop()
        if len(self.itms[len(self.itms) - 1]) == 0:
            self.itms.pop()
        return result

    def get_val(self):
        return self.itms[len(self.itms) - 1]

    def stack_size(self):
        elem_sum = 0
        for stack in self.itms:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        return len(self.itms)


if __name__ == '__main__':
    plates = PiledPlatesClass(5)
    print(type(plates))
    plates.push_in('plate1')
    plates.push_in('plate2')
    plates.push_in('plate3')
    plates.push_in('plate4')
    plates.push_in('plate5')
    plates.push_in('plate6')
    plates.push_in('plate7')
    print(plates)
    print(plates.pop_out())
    print(plates.get_val())
    print(plates.stack_size())
    print(plates.stack_count())
    print(plates)
