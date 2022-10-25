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

class StackClass:
    def __init__(self, num_el):
        self.elems = []
        self.num_el = num_el

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):

        if len(self.elems) == 0:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)
        elif len(self.elems[len(self.elems) - 1]) < self.num_el:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':
    stack = StackClass(4)

    stack.push_in('stack_1')
    stack.push_in('stack_2')
    stack.push_in('stack_3')
    stack.push_in('stack_4')
    stack.push_in('stack_5')
    print(stack)
    print(stack.pop_out())
    print(stack.get_val())
    print(stack.stack_size())
    print(stack)
    stack.push_in('stack_6')
    stack.push_in('stack_7')
    stack.push_in('stack_8')
    stack.push_in('stack_9')
    print(stack)
    print(stack.stack_size())