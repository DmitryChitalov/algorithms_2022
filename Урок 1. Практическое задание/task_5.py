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
        self.elems = []
        self.max_stack_size = 5

    def is_empty(self):
        return self.elems == []

    def print(self):
        print(self.elems)

    def stack_size(self):
        return len(self.elems)

    def get_last_stack(self):
        if self.is_empty():

            return None
        else:
            return self.elems[len(self.elems) - 1]

    def get_stack_not_complete(self):
        last_stack = self.get_last_stack()

        if last_stack is None:
            self.elems.append([])
            last_stack = self.elems[0]

        if len(last_stack) < self.max_stack_size:
            return last_stack
        else:
            self.elems.append([])
            return self.elems[self.stack_size()-1]

    def push_in(self):
        stack = self.get_stack_not_complete()
        plate = f'plate_{(len(self.elems)-1)*self.max_stack_size+(len(stack)+1)}'
        stack.append(plate)
        return plate

    def pop_out(self):
        stack = self.get_last_stack()
        if stack is None:
            return None

        elem  = stack.pop()
        if stack == []:
            self.elems.pop()
        return elem

if __name__ == '__main__':
    obj_StackPlates = StackPlates()

    for i in range(21):
       print(f'Добавили тарелку: {obj_StackPlates.push_in()}')

    obj_StackPlates.print()

    for i in range(8):
        print(f'Взяли тарелку: {obj_StackPlates.pop_out()}')

    obj_StackPlates.print()
