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


class StackOfPlates:
    def __init__(self):
        self.stack = []
        self.amount_of_ones = 0

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)

    def push_and_delete(self, item):
        for value in item.split(' '):
            if value[0] == 0:
                continue
            elif value[0] == '+':
                self.amount_of_ones += int(value[1:])
            elif value[0] == '-':
                self.amount_of_ones -= int(value[1:])
        val = ''
        for iterate in range(1, self.amount_of_ones + 1):
            if len(val) == 5:
                self.stack.append(int(val))
                val = ''
            val += '1'
            if iterate == self.amount_of_ones:
                self.stack.append(int(val))


s = StackOfPlates()

s.push_and_delete('+6 +3 0 -4 +1')
print(s.stack_size())
print(s.stack)
