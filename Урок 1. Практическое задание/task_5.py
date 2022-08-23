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

class Stack:
    def __init__(self):
        self.stack = [[], [], [], [], []]
        self.max = 3    # максимальное количество элементов в одном стэке
        self.substack = 0

    def push_in(self, element):
        if len(self.stack[self.substack]) < self.max:
            self.stack[self.substack].append(element)
        else:
            self.substack += 1
            self.stack[self.substack].append(element)

    def pop(self):
        if len(self.stack[self.substack]) >= 1:
            self.stack[self.substack].pop()
        else:
            self.substack -= 1
            self.stack[self.substack].pop()

    def check(self):
        return self.stack


b = Stack()

for i in range(15):
    b.push_in(i)

print(b.check())

for i in range(4):
    b.pop()

print(b.check())

for i in range(4):
    b.push_in(i)

print(b.check())