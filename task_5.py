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


class PlatesPile:
    def __init__(self, height):
        self.plates_pile = [[]]
        self.height = height

    def __str__(self):
        return str(self.plates_pile)

    def put_onto(self, plates): # принимает список.
        for i in range(len(plates)):
            if len(self.plates_pile[len(self.plates_pile)-1]) < self.height:
                self.plates_pile[len(self.plates_pile)-1].append(plates[i])
            else:
                self.plates_pile.append([])
                self.plates_pile[len(self.plates_pile)-1].append(plates[i])

    def take_from(self, number_of_plates):
        result = []
        for i in range(number_of_plates):
            result.append(self.plates_pile[len(self.plates_pile)-1].pop()) # результат накопится в обратном порядке
            if len(self.plates_pile[len(self.plates_pile) - 1]) == 0:
                self.plates_pile.pop()

        return result


pile1 = PlatesPile(8)
print(pile1)
pile1.put_onto('1')
print(pile1)
pile1.put_onto([2, True, None, {'Vasya': 17}])
print(pile1)
print(pile1.take_from(2))
print(pile1)
from random import sample
lst = sample(range(-100, 100), 50)
pile1.put_onto(lst)
print(pile1)
print(pile1.take_from(40))
print(pile1)
