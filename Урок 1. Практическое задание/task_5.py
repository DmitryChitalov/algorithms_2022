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

class StackPlatesClass:
    def __init__(self, max_amount):
        self.stuff= []
        self.max_amount = max_amount

    def __str__(self):
        return str(self.stuff)

    def empty(self):
        return self.stuff == [[]]

    def put_down(self, elems):
        if len(self.stuff[len(self.stuff)-1]) < self.max_amount:
            self.stuff[len(self.stuff)-1].append(elems)
        else:
            self.stuff.append([])
            self.stuff[len(self.stuff) - 1].append(elems)

    def pop_out(self):
        res = self.stuff[len(self.stuff) - 1].pop()
        if len(self.stuff[len(self.stuff) - 1]) == 0:
            self.stuff.pop()
        return res

    def value(self):
        return self.stuff[len(self.stuff) - 1]

    def whole_amount(self):
        sum_of_stuff = 0
        for stack in self.stuff:
            sum_of_stuff += len(stack)
        return sum_of_stuff

    def size(self):
        return len(self.stuff)

if __name__ == '__main__':
    plates = StackPlatesClass(3)
    plates.put_down('Pl1')
    plates.put_down('Pl2')
    plates.put_down('Pl3')
    plates.put_down('Pl4')
    print(plates)
    print(plates.pop_out())
    print(plates.value())
    print(plates.whole_amount())
    print(plates.size())
    print(plates)

