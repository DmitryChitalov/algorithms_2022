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

class PlatesQueue:
    def __init__(self):
        self.plates = [[]]


"""Пороговое значение стопки 3"""
    def put_plate (self):
        if len(self.plates[len(self.plates) - 1]) == 0:
            self.plates[len(self.plates) - 1].append('plate')
        elif len(self.plates[len(self.plates) - 1]) < 3 and len(self.plates[len(self.plates) - 1]) > 0:
            self.plates[len(self.plates) - 1].append('plate')
        elif len(self.plates[len(self.plates) - 1]) == 3:
            self.plates.append(['plate'])
        return print(self.plates)



a = PlatesQueue()
a.put_plate()
a.put_plate()
a.put_plate()
a.put_plate()
a.put_plate()
a.put_plate()
a.put_plate()
a.put_plate()
a.put_plate()

