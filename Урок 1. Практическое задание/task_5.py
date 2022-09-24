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
    def __init__(self, n):
        self.items = [[]]
        self.stack_size = n  # Размер стопки
        self.idx = 0

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.items == [[]]

    def append_item(self, el):

        new_stack = []
        if len(self.items[self.idx]) < self.stack_size:
            self.items[self.idx].append(el)
        else:
            self.items.append(new_stack)
            self.idx += 1
            self.items[self.idx].append(el)

        return self.items

    def pop_out(self):

        result = self.items[len(self.items) - 1].pop()  # Берем тарелку из крайней стопки
        if len(self.items[len(self.items) - 1]) == 0:  # Если она пустая, удаляем
            self.items.pop()
        return result

    def get_value(self):
        return self.items[len(self.items) - 1]

    def item_count(self):
        """Общее кол-во тарелок"""
        item_sum = 0
        for stack in self.items:
            item_sum += len(stack)
        return item_sum

    def stack_count(self):
        """ Общее кол-во стопок"""
        return len(self.items)


if __name__ == '__main__':
    a = StackOfPlates(4)
    a.append_item("O")
    a.append_item("O")
    a.append_item("O")
    a.append_item("O")
    a.append_item("O")
    a.append_item("O")
    a.append_item("O")
    a.append_item("O")
    a.append_item("O")
    print(a)
    print(a.item_count())
    a.pop_out()
    print(a.item_count())
    # print(a.get_value())
    print(a)
