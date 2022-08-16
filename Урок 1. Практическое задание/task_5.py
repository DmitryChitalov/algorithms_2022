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

class StackofPlates:
    def __init__(self):
        self.plates = []

    def is_empty(self):
        return self.plates == []

    def push_in(self, plate):
        if self.stack_size() < 10:
            self.plates.append(plate)

    def pop_out(self):
        return self.plates.pop()

    def get_val(self):
        return self.plates[len(self.plates) - 1]

    def stack_size(self):
        return len(self.plates)


def plates_stack(hight_of_stack: int, number_of_plates: int):
    stack = StackofPlates()
    while number_of_plates > 0:
        stack.push_in(1)
        number_of_plates -= 1


