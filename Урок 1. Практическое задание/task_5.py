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


class StackTask:
    def __init__(self, maxsize=5):
        self.stacks =[[]]
        self.maxsize = maxsize

    def current_pile(self):
        """ текущая стопка """
        return self.stacks[-1]

    def add_next_pile(self):
        """ добавить ещё одну стопку """
        self.stacks.append([])

    def add_to_pile(self, new_plates):
        """ добавить в стопку"""
        while new_plates > 0:
            if len(self.stacks[-1]) < self.maxsize:
                self.stacks[-1].append('plate')
                new_plates -= 1
            else:
                self.add_next_pile()

    def show_stacks(self):
        return [s for s in self.stacks]


plates = StackTask()
user_plates = int(input('Сколько тарелок разложить по стопкам: '))

plates.add_to_pile(user_plates)
print(plates.show_stacks())

