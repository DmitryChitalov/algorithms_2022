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
        self.stack = []
        self.stacks = []

    def current_len(self):
        return len(self.stack)

    def current_value(self):
        return self.stack

    def put_in(self):
        if self.current_len() >= 5:
            self.new_stack()
            self.stack.append('plate')
        else:
            self.stack.append('plate')

    def take_out(self):
        if self.current_len() <= 0:
            self.take_stack()
            self.stack.pop()
        else:
            self.stack.pop()

    def new_stack(self):
        self.stacks += [self.stack]
        self.stack = []

    def take_stack(self):
        self.stack = self.stacks.pop()

    def stacks_len(self):
        return len(self.stacks)

    def stacks_value(self):
        return self.stacks

    def __str__(self):
        text = f"current stack length : {self.current_len()}\n" \
               f"current stack values : {self.current_value()}\n\n" \
               f"Stacks amount : {self.stacks_len()}\n" \
               f"stacked values: {self.stacks_value()}\n"
        return text


if __name__ == '__main__':
    stack = PlateStack()
    for i in range(14):
        stack.put_in()
    print(stack)
    for i in range(5):
        stack.take_out()
    print(stack)