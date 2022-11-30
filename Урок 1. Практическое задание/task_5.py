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
        self.count = 0

    """Пороговое значение стопки 3"""

    def put_plate(self):
        if len(self.plates[len(self.plates) - 1]) == 0:
            self.plates[len(self.plates) - 1].append(f'plate{self.count + 1}')
            self.count += 1
        elif len(self.plates[len(self.plates) - 1]) < 3 and len(self.plates[len(self.plates) - 1]) > 0:
            self.plates[len(self.plates) - 1].append(f'plate{self.count + 1}')
            self.count += 1
        elif len(self.plates[len(self.plates) - 1]) == 3:
            self.plates[len(self.plates) - 1].append(f'plate{self.count + 1}')
            self.plates.append([self.plates[len(self.plates) - 1][2]])
            self.plates[len(self.plates) - 2].pop(2)
            self.count += 1
        return self.plates

    def pop_plate(self):
        self.plates[len(self.plates) - 1].pop()
        if len(self.plates[len(self.plates) - 1]) == 0:
            self.plates.pop()
        return self.plates


a = PlatesQueue()
print(a.put_plate())
print(a.put_plate())
print(a.put_plate())
print(a.put_plate())
print(a.put_plate())
print(a.put_plate())
print(a.put_plate())
print(a.put_plate())
print(a.put_plate())
print(a.put_plate())
print(a.pop_plate())
