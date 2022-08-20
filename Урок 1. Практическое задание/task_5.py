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

class StackOfPlates():
    limit_stack = 0

    def __init__(self):
        self.stack = [[]]

    def add(self):
        self.stack[self.limit_stack].append(0)
        if len(self.stack[self.limit_stack]) >= 5:
            self.limit_stack += 1
            self.stack.append([])

    def __str__(self):
        return f'{self.stack}'


a = StackOfPlates()

a.add()
a.add()
a.add()
a.add()
a.add()
a.add()
a.add()
a.add()
a.add()
a.add()
a.add()
a.add()

print(a)