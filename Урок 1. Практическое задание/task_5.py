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


class StackPlates:
    def __init__(self, stack_size=5):
        self.__box = []  # шкаф с тарелками
        self.__stack = []  # стопка тарелок
        self.__stack_size = stack_size  # размер стопки

    def pop_out(self):
        """
        Вернуть верхнюю тарелку из стопки
        Если в стопке нет тарелок, посмотреть в шкафу.
        Если в шкафу нет тарелок вернуть None, иначе взять стопку из шкафа и вернуть тарелку
        """
        if self.is_empty():
            if self.is_empty_box():
                return
            self.__stack = self.__box.pop()
        return self.__stack.pop()

    def push_in(self, plate):
        """
        Проверить не переполнена ли стопка.
        Если переполнена, поставить стопку в шкаф и складывать тарелки в новую стопку
        """
        if self.is_overflowing():
            self.__box.append(self.__stack)
            self.__stack = []
        self.__stack.append(plate)

    def is_empty(self):
        """
        Вернуть True если стопка тарелок пуста, иначе вернуть False
        """
        return self.__stack == []

    def is_empty_box(self):
        """
        Вернуть True если в шкафу нет стопок тарелок, иначе вернуть False
        """
        return self.__box == []

    def is_overflowing(self):
        """
        Вернет True если стопка переполнена, иначе False
        """
        return not len(self.__stack) < self.__stack_size

    def get_stack_size(self):
        """
        Вернет общее количество тарелок
        """
        total = 0
        for stack in self.__box:
            total += len(stack)
        total += len(self.__stack)
        return total

    def change_stack_size(self, size):
        """
        Изменяет размер стопки тарелок
        """
        self.__stack_size = size

    def print_box(self):
        """
        для демонстрации. Можно удалить
        """
        return self.__box

    def print_stack(self):
        """
        для демонстрации. Можно удалить
        """
        return self.__stack


if __name__ == '__main__':
    stack = StackPlates()
    # Добавим в стек 17 тарелок
    for i in range(17):
        stack.push_in(i)

    print('В стеке элементов:', stack.get_stack_size())
    print('Стопки в шкафу:', stack.print_box())
    print('Элементы в стопке: ', stack.print_stack())

    x, y, z = [stack.pop_out() for item in range(3)]  # Возьмем три тарелки из стопки
    print('Взяли из стека:', x, y, z)
    print('В стеке элементов:', stack.get_stack_size())

    print('Возьмем больше чем есть в стеке')
    for i in range(15):
        print(stack.pop_out())
    print('В стеке элементов:', stack.get_stack_size())

    print('Изменим размер стопки на 8')
    stack.change_stack_size(8)

    print('Добавим 17 элементов в стопку')
    for i in range(17):
        stack.push_in(i)
    print('В стеке элементов:', stack.get_stack_size())
    print('Стопки в шкафу:', stack.print_box())
    print('Элементы в стопке: ', stack.print_stack())
