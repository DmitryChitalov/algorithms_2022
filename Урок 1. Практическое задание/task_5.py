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


class PlatesStack:

    def __init__(self, max_plates=3):
        self.stacks = [[]]
        self.current_stack = 0
        self.max_plates = max_plates

    def __str__(self):
        return str(self.stacks)

    def add_plate(self, plate: str):
        if len(self.stacks[self.current_stack]) == self.max_plates:
            self.stacks.append([])
            self.current_stack += 1
        self.stacks[self.current_stack].append(plate)

    def take_plate(self):
        if len(self.stacks[self.current_stack]) > 0:
            plate = self.stacks[self.current_stack].pop()
            if len(self.stacks[self.current_stack]) == 0 and len(self.stacks) > 1:
                self.stacks.pop()
                self.current_stack -= 1
            return plate

    def current_plate(self):
        return self.stacks[self.current_stack][-1]

    def stack_count(self):
        return len(self.stacks)

    def plates_count(self):
        return sum([len(x) for x in self.stacks])


if __name__ == '__main__':
    plates = PlatesStack()
    plates.add_plate('Plate #1')
    plates.add_plate('Plate #2')
    plates.add_plate('Plate #3')
    plates.add_plate('Plate #4')
    plates.add_plate('Plate #5')
    plates.add_plate('Plate #6')
    plates.add_plate('Plate #7')
    print(plates.plates_count())
    print(plates.current_plate())
    print(plates.stack_count())
    print(plates)
    print(plates.take_plate())
    print(plates.plates_count())
    print(plates)
