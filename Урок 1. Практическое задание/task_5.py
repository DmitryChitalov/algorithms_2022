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


class StackPlates:

    def __init__(self):
        self.stacks_plates = []
        self.size = 5
        self.plates = []

    def add(self, plate):
        if self.size == len(self.plates):
            self.stacks_plates.append(self.plates.copy())
            self.plates.clear()
            self.plates.append(plate)
        else:
            self.plates.append(plate)

    def take(self):
        if self.plates:
            self.plates.pop()
        elif self.stacks_plates:
            number_stacks = len(self.stacks_plates)
            self.stacks_plates[number_stacks-1].pop()
        else:
            print('Нет тарелок')

    def show(self):
        if self.plates:
            self.stacks_plates.append(self.plates)
        print(self.stacks_plates)


stack = StackPlates()

print('Сложите тарелки , не более 5 в стопку')

stack.add('тарелка1')
stack.add('тарелка2')
stack.add('тарелка3')
stack.add('тарелка4')
stack.add('тарелка5')
stack.add('тарелка6')
stack.add('тарелка7')
stack.add('тарелка8')
stack.add('тарелка9')
stack.add('тарелка10')
stack.add('тарелка11')

stack.take()
stack.take()
stack.take()

stack.show()
