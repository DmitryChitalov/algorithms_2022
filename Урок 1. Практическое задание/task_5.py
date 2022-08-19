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


class PlateStack:
    def __init__(self):
        self.stack = []  # стопка
        self.stacks = []  # стопки

    def put_in(self):
        """
        добавление тарелки в стопку
        :return:
        """
        # если в тарелке ровно 10 тарелок создает новую стопку
        if len(self.stack) == 10:
            self.new_stack()

        self.stack.append(f'Plate{len(self.stack) + 1}')

    def take_out(self):
        """
        Достаем тарелку из стопки если есть стопка или стопки
        :return:
        """
        if self.stack:
            self.stack.pop()
        elif (not self.stack) and self.stacks:
            self.stack_is_over()
        else:
            print("No more plates")

    def show_current(self):
        """
        количество тарелок в нынешней стопке
        :return:
        """
        return self.stack

    def show_all(self):
        """
        показывает все стопки
        :return:
        """
        return self.stacks

    def new_stack(self):
        """
        создает новую стопку
        :return:
        """
        self.stacks.append(self.stack)
        self.stack = []

    def stack_is_over(self):
        """
        Берет стопку из скалад стопок
        :return:
        """
        self.stack = self.stacks.pop()


if __name__ == "__main__":
    test = PlateStack()
    # добавление- удаление из стопки
    test.put_in()
    test.put_in()
    # print(test.show_current())
    test.take_out()
    # print(test.show_current())
    # проверка на  создание новой стопки
    for i in range(30):
        test.put_in()
    print(test.show_current())
    print(test.show_all())
    # стопка заканчивается
    for i in range(20):
        test.take_out()
    print(test.show_current())
    print(test.show_all())
    for i in range(20):
        test.take_out()
