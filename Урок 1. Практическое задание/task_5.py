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

class PlateStack():

    MAX_STACK = 2

    def __init__(self):
        self.stack = [[]]
        self.idx = 0

    def __str__(self):
        return str(self.stack)

    def add(self, plate):
        """ Добавляем тарелку """
        if len(self.stack[self.idx]) >= self.MAX_STACK:
            self.idx = self.idx + 1
            self.stack.append([])

        self.stack[self.idx].append(plate)

    def is_empty(self):
        return self.stack == [[]]

    # FIX
    def delete(self):
        """ Удаляем тарелку """
        if len(self.stack[self.idx]) > 0:
            self.stack[self.idx].pop()
            if len(self.stack[self.idx]) <= 0:
                self.idx -= 1
                self.stack.pop()

    def clear(self):
        """ Чистим всё """
        self.stack = [[]]
        self.idx = 0

    def stack_size(self):
        """Общее количество тарелок"""
        elem_sum = 0
        for stack in self.stack:
            elem_sum += len(stack)
        return elem_sum


stack = PlateStack()
stack.add(1)
stack.add(1)
stack.add(1)
stack.add(1)
stack.add(1)
stack.add(1)
stack.delete()
stack.delete()
stack.delete()
stack.clear()
stack.add(1)
stack.add(1)
print(stack.stack)
print(str(stack))
print(stack.is_empty())
stack.clear()
print(str(stack))
print(stack.is_empty())
print(stack.stack_size())
stack.add(1)
stack.add(1)
print(stack.stack_size())