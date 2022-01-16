"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""
from functools import reduce


class PlatesStack():
    MAX_PLATES_IN_STACK = 5

    def __init__(self):
        self.plate_stack_arr = [[]]

    def add_new_plates(self, plates_value: int ):
        for plate in range(int(plates_value)):
            if self.stack_height:
                self.plate_stack_arr.append([])
            self.plate_stack_arr[-1].append("_")

    @property
    def stack_height(self) -> bool:
        return len(self.plate_stack_arr[-1]) >= self.MAX_PLATES_IN_STACK

    @property
    def show_all_plate_stacks(self) -> list:
        return self.plate_stack_arr

    @property
    def total_plates_quantity(self):
        return f"Total plates: {len(reduce(lambda x, y: x + y, self.plate_stack_arr))}"

    @property
    def total_stacks(self):
        return "Total stacks: %s with max height %s plates" % (len(self.plate_stack_arr), self.MAX_PLATES_IN_STACK)


if __name__ == "__main__":
    """ инициализация плюс операции """
    testStack = PlatesStack()
    testStack.add_new_plates(3)
    testStack.add_new_plates(6)
    testStack.add_new_plates(14)
    testStack.add_new_plates(17)

    """ Проверка """
    [print(i) for i in testStack.show_all_plate_stacks]  # красиво принтует стопки :)
    print(testStack.total_plates_quantity)
    print(testStack.total_stacks)

