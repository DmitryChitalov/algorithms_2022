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


class Stack:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def push_in(self, item):
        self.elements.append(item)

    def pop_out(self):
        return self.elements.pop()

    def stack_size(self):
        return len(self.elements)

    def __repr__(self):
        return str(self.elements)


class PlateStack:
    def __init__(self):
        self.plates = []

    def add_plate(self):
        if len(self.plates) == 0 or self.plates[-1].stack_size() == 3:  # Ограничение в три тарелки в одной стопке
            self.plates.append(Stack())
        self.plates[-1].push_in('plate')

    def take_plate(self):
        if len(self.plates) != 0:
            self.plates[-1].pop_out()
            if self.plates[-1].stack_size() == 0:
                self.plates.pop()

    def print_plates(self):
        print(self.plates)


if __name__ == '__main__':

    plates = PlateStack()

    plates.add_plate()
    plates.add_plate()
    plates.add_plate()
    plates.add_plate()
    plates.add_plate()
    plates.add_plate()
    plates.add_plate()
    plates.print_plates()

    plates.take_plate()
    plates.take_plate()
    plates.print_plates()

    plates.take_plate()
    plates.take_plate()
    plates.take_plate()
    plates.take_plate()
    plates.take_plate()
    plates.print_plates()
