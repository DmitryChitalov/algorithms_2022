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

    def __init__(self, stack_size: int):
        self.stacks = []
        self.stack_size = stack_size

    def _add_empty_stack(self):
        """Добавить пустую стопку в конце полки"""
        self.stacks.append([])

    def _remove_empty_stack(self):
        """Удалить пустую стопку в конце полки, если она есть"""
        if not self.stacks[-1]:
            self.stacks.pop(-1)

    def add_plate(self, plate):
        """Добавить тарелку на полку"""
        if not self.stacks or len(self.stacks[-1]) == self.stack_size:
            # Если пустых стопок нет, или последняя стопка заполнена, добавить пустую стопку
            self._add_empty_stack()

        last_stack = self.stacks[-1]
        last_stack.append(plate)

    def remove_plate(self):
        """Взять тарелку с полки"""
        last_stack = self.stacks[-1]
        last_stack.pop()
        # Удалить пустую стопку, если она образовалась в результате взятия тарелки
        self._remove_empty_stack()

    @property
    def get_stacks(self):
        """Посмотреть состояние полки"""
        return self.stacks


if __name__ == '__main__':

    # Создадим полку с величиной стопки 3
    my_shelf = Shelf(3)

    # Добавим 8 тарелок
    i = 1
    for _ in range(8):
        my_shelf.add_plate(i)
        i += 1
    print(my_shelf.get_stacks)

    # Удалим 3 тарелки
    for _ in range(3):
        my_shelf.remove_plate()
    print(my_shelf.get_stacks)
