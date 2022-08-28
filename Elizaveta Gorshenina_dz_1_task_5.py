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
    def __init__(self, max_num):
        self.plates = [[]]
        self.max_num = max_num
        self.is_full = False

    def __str__(self):
        return str(self.plates)

    def add_empty_stack(self):
        self.plates.append([])

    def full_check(self):
        if len(self.plates[len(self.plates) - 1]) == self.max_num:
            self.is_full = True
        else:
            self.is_full = False

    def put_one(self):
        if self.is_full:
            self.add_empty_stack()
        self.plates[len(self.plates) - 1].append('◎')
        self.full_check()

    def put(self, plates_num):
        for num in range(plates_num):
            self.put_one()


cupboard = PlatesStack(5)
cupboard.put(13)
print(cupboard)
cupboard.put_one()
print(cupboard)
