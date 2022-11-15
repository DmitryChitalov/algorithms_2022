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


class Shelf:
    kitchen_shelf = list()

    def __init__(self, capacity=10):
        self.items = list()
        self.capacity = capacity

    def is_empty(self):
        return len(self.items) == 0

    def is_not_empty(self):
        return len(self.items) != 0

    def shelf_empty(self):
        return len(self.kitchen_shelf) == 0

    def shelf_not_empty(self):
        return len(self.kitchen_shelf) != 0

    def push(self, item):
        if self.size() < self.capacity:
            self.items.append(item)
        else:
            self.kitchen_shelf.append([*self.items])
            self.items.clear()
            self.items.append(item)

    def pop(self):
        if self.is_not_empty():
            return self.items.pop()
        if self.shelf_not_empty():
            self.items = self.kitchen_shelf.pop()
            return self.items.pop()
        print('Нечего забирать')

    def size(self):
        return len(self.items)

    def print(self):
        for key, items in enumerate(self.kitchen_shelf):
            print(f'Полка {key}: {items}')


if __name__ == '__main__':
    kitchen_shelf = Shelf()
    for i in range(100):
        kitchen_shelf.push(f'plane-{i}')

    kitchen_shelf.print()
