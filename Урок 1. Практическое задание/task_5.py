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
    def __init__(self):
        """
        При создании обьекта инициализируются следующие переменные:
        max_amount - количество элементов в стопке
        index_of_stack - индекс текущей стопки
        plates_amount = общее количество елементов во всех стопках обьекта
        """
        self.stacks = [[]]
        self.max_amount = 5
        self.index_of_stack = 0
        self.plates_amount = 0
        self.elem_name = 'тарелка'

    def is_empty(self):
        """
        Функция проверяет пустой стек или нет.
        @return: Boolean
        """
        return self.plates_amount == 0

    def add_to_stack(self, amount):
        """
        Добавляет элементы во вложенный список.
        В случае если во вложенном списке количество элементов превышает заданное, создает новый вложенный список
        и передвигает индекс вложенного списка.
        @param amount: Integer
        @return: None
        """
        for plate in range(0, amount):
            if len(self.stacks[self.index_of_stack]) < self.max_amount:
                self.stacks[self.index_of_stack].append(self.elem_name)
                self.plates_amount += 1
            else:
                self.index_of_stack += 1
                self.stacks.append([self.elem_name])
                self.plates_amount += 1

    def remove_from_stack(self, amount):
        """
        Удаляет элементы из вложенного списка.
        Если количество элементов на удаление превышает количество элементов во всех вложенных списках,
        возвращает ошибку.
        @param amount: Integer
        @return: None or ValueError
        """
        _error_text = f'В текущих стопках всего {self.plates_amount} тарелок, вы пытаетесь убрать {amount} тарелок'
        if amount > self.plates_amount:
            raise ValueError(_error_text)
        for plate in range(0, amount):
            if len(self.stacks[self.index_of_stack]) > 0:
                self.stacks[self.index_of_stack].pop()
                self.plates_amount -= 1
            else:
                self.stacks.pop()
                self.index_of_stack -= 1
                self.stacks[self.index_of_stack].pop()
                self.plates_amount -= 1

    def show_stack(self):
        """
        Возвращает текущий стек.
        @return: List
        """
        return self.stacks

    def show_value_of_stack(self):
        """
        Возвращает количество элементов в стеке.
        @return: Integer
        """
        return self.plates_amount


if __name__ == '__main__':
    plate_stack_1 = StackOfPlates()
    plate_stack_1.add_to_stack(12)
    print(plate_stack_1.show_stack())
    plate_stack_1.remove_from_stack(10)
    print(plate_stack_1.show_stack())
