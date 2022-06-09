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
    def __init__(self):
        self.elements = []
        self.max_size = 5

    def empty(self):
        return self.elements == []

    def print(self):
        print(self.elements)

    def size(self):
        return len(self.elements)

    def last_stack(self):
        if self.empty():
            return None
        else:
            return self.elements[len(self.elements) - 1]

    def stack_not_complete(self):
        last_stack = self.last_stack()

        if last_stack is None:
            self.elements.append([])
            last_stack = self.elems[0]

        if len(last_stack) < self.max_size:
            return last_stack
        else:
            self.elements.append([])
            return self.elements[self.size() - 1]

    def push_in(self):
        stack = self.stack_not_complete()
        plate = f'plate_{(len(self.elements) - 1) * self.max_size + (len(stack) + 1)}'
        stack.append(plate)
        return plate

    def pop_out(self):
        stack = self.last_stack()
        if stack is None:
            return None

        element  = stack.pop()
        if stack == []:
            self.elements.pop()
        return element

if __name__ == '__main__':
    stack_plates = StackPlates()

    for i in range(10):
       print(f'Положили тарелку: {stack_plates.push_in()}')

    stack_plates.print()

    for i in range(5):
        print(f'Положили тарелку в новую стопку: {stack_plates.pop_out()}')

    stack_plates.print()
