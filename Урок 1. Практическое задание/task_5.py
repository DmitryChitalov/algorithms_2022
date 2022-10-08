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


# Реализуем класс стека
class StackClass:
    def __init__(self, ssize):
        self.elems = [[]]
        self.i = -1
        self.num_sc = 0
        self.stack_size = ssize

    def is_empty(self):
        return self.elems == [[]]

    def to_add(self, el):
        self.i += 1
        self.num_sc = int(self.i // self.stack_size)
        if self.num_sc >= len(self.elems):
            self.elems.append([])
        self.elems[self.num_sc].append(el)

    def to_remove(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def get_elems(self):
        return self.elems

    def size_of(self):
        return len(self.elems)


if __name__ == '__main__':

    # Функция для наполнения стека
    def stack_add(lst, ssize):
        stack = StackClass(ssize)

        for i in range(len(lst)):
            stack.to_add(lst[i])

        return stack.get_elems()


    data = ['plate_1', 'plate_2', 'plate_3', 'plate_4', 'plate_5']

    stack_1 = stack_add(data, 2)
    stack_2 = stack_add(data, 1)

    print(stack_1)
    print(stack_2)
