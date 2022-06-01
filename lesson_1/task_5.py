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


class PlateClass:
    def __init__(self, max_el):
        self.elems = []
        self.max_el = max_el  # количество тарелок в стопке

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):

        if len(self.elems) == 0:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)
        elif len(self.elems[len(self.elems) - 1]) < self.max_el:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':
    plates = PlateClass(3)
    print(plates)  # -> стопка пустая
    # наполняем стoпку
    plates.push_in('plate1')
    plates.push_in('plate2')
    plates.push_in('plate3')
    plates.push_in('plate4')
    plates.push_in('plate5')
    print(plates)  # ->  [['plate1', 'plate2', 'plate3'], ['plate4', 'plate5']]
    print(plates.pop_out())  # ->  plate5
    print(plates.get_val())  # -> ['plate4']
    print(plates.stack_size())  # -> 2
    print(plates)
    plates.push_in('plate6')
    plates.push_in('plate7')
    plates.push_in('plate8')
    print(plates)  # -> [['plate1', 'plate2', 'plate3'], ['plate4', 'plate6', 'plate7'], ['plate8']]
    print(plates.stack_size())  # -> 3
