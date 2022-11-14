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

class PlateStack:

    def __init__(self):
        self.index = 0
        self.number = 0
        self.stack = [[]]

    def clearStack(self):
        return self.number == 0

    def push_in(self, plate):
        if len(self.stack[self.index]) >= self.stackLimit:
            self.index += 1
            self.stack.append([])

        self.stack[self.index].append(plate)
        self.number += 1

    def pop_out(self):
        stackPlates = self.stack[self.index].pop()
        self.number -= 1
        if len(self.stack[self.index]) == 0:
            self.index -= 1
        return stackPlates

    def get_val(self):
        return self.stack[len(self.stack) - 1]

    def stack_size(self):
        return self.number

    stackLimit = 5


arg = PlateStack()
print(arg.clearStack())
for i in range(22):
        arg.push_in(i)

print(arg.stack)
print(arg.index)
print(arg.number)
print(arg.stack_size())