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


class Plates:
    MAXPLATES = 10

    def __init__(self):
        self.elems = [0]

    def add_plate(self, plates):
        if self.elems[-1] + plates > self.MAXPLATES:
            self.elems[-1] = self.MAXPLATES
            for _ in range((plates // self.MAXPLATES)-1):
                self.elems.append(self.MAXPLATES)
            if plates % self.MAXPLATES:
                self.elems.append(plates % self.MAXPLATES)
        elif self.elems[-1] + plates <= self.MAXPLATES:
            self.elems[-1] += plates

    def num_of_plates(self):
        return self.elems


if __name__ == '__main__':
    Stack_1 = Plates()

    Stack_1.add_plate(15)

    print(Stack_1.num_of_plates())
