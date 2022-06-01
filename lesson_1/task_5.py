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

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[-1]) < 2:
            self.elems[-1].append(el)
        else:
            self.elems.append([])
            self.elems[-1].append(el)

    def pop_out(self):
        if len(self.elems[-1]) > 0:
            self.elems[-1].pop()
        else:
            self.elems.pop()
            self.elems[-1].pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':
    plates = StackClass()
    plates.push_in('plate_1')
    plates.push_in('plate_2')
    plates.push_in('plate_3')
    plates.push_in('plate_4')
    plates.push_in('plate_5')
    print(plates.elems)
    plates.pop_out()
    plates.pop_out()
    print(plates.elems)
    print(plates.get_val())
    print(plates.stack_size())
