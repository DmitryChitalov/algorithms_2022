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
    SIZE = 3

    def __init__(self):
        self.stack = [[]]
        self.stack_number = 0

    def is_empty(self):
        return self.stack == [[]]

    def push_in(self, el):
        if len(self.stack[self.stack_number]) == self.SIZE:
            self.stack.append([])
            self.stack_number += 1
        self.stack[self.stack_number].append(el)

    def pop_out(self):
        value = self.stack[self.stack_number].pop()
        if len(self.stack[self.stack_number]) == 0:
            del (self.stack[self.stack_number])
            if not self.is_empty():
                self.stack_number -= 1
        return value

    def get_val(self):
        return self.stack[self.stack_number][-1]

    def stack_size(self):
        return (len(self.stack) - 1) * self.SIZE + len(self.stack[self.stack_number])


my_stack = StackOfPlates()
print(my_stack.is_empty())
for i in range(10):
    my_stack.push_in(i)
print("Пустой ли стек?", my_stack.is_empty())
print("Стек: ", *my_stack.stack, sep='\n')
print("Количество элементов ", my_stack.stack_size())

print("Вытаскиваем верхний элемент ", my_stack.pop_out())
print("Стек: ", *my_stack.stack, sep='\n')
print("Номер текущей стопки ", my_stack.stack_number)

print("Количество элементов ", my_stack.stack_size())
