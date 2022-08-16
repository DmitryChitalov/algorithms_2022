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
--создание новой стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class StacksPlatesClass():
    remain_volume_stack = 0

    def __init__(self):
        self.stacks = []

    def is_empty(self):
        return self.stacks == []

    def add_stack(self, volume=1):
        StacksPlatesClass.remain_volume_stack = volume
        self.stacks.append([])

    def add_plate(self):
        # если нет ниодной стопки
        if self.is_empty():
            self.add_stack()    # создаем место для будущей стопки
        # если места в последней стопке нет
        if StacksPlatesClass.remain_volume_stack == 0:
            self.add_stack()
        self.stacks[-1].append('+')
        StacksPlatesClass.remain_volume_stack -= 1

    def pop_plate(self):
        # если последняя стопка пустая
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
            self.stacks[-1].pop()
            StacksPlatesClass.remain_volume_stack = 1
        # если в последней стопке 1 тарелка
        elif len(self.stacks[-1]) == 1:
            self.stacks[-1].pop()
            self.stacks.pop()
            StacksPlatesClass.remain_volume_stack = 0
        else:
            self.stacks[-1].pop()
            StacksPlatesClass.remain_volume_stack += 1

    def __str__(self):
        # переопределение вывода стопок с тарелками
        return f'{self.stacks}'

