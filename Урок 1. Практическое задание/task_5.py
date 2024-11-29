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


def push_in_dec(func):
    def new_stack(*args):
        n_stack = []
        if args[0].stack != [] and len(args[0].stack[len(args[0].stack)-1]) < args[0].n:
            n_stack = args[0].stack[len(args[0].stack)-1]
            n_stack.append(args[1])
            args[0].stack[len(args[0].stack) - 1] = n_stack
        else:
            n_stack.append(args[1])
            func(args[0], n_stack)
    return new_stack


def get_val_ext(func):
    def new_get_val(*args):
        return args[0].stack[len(args[0].stack) - 1][len(args[0].stack[len(args[0].stack) - 1]) - 1]
    return new_get_val


def pop_out_ext(func):
    def new_pop_out(*args):
        if 1 < len(args[0].stack[len(args[0].stack) - 1]) <= args[0].n:
            return args[0].stack[len(args[0].stack) - 1].pop()
        else:
            return func(args[0])
    return new_pop_out


def stack_size_ext(func):
    def new_stack_size(*args):
        length = 0
        for i in range(len(args[0].stack)):
            length += len(args[0].stack[i])
        return length
    return new_stack_size


class StackOfPlates:

    def __init__(self):
        self.stack = []
        self.n = 4                  # defines the size of a part of the stack

    def is_empty(self):
        return self.stack == []

    @push_in_dec
    def push_in(self, el):
        self.stack.append(el)

    @pop_out_ext
    def pop_out(self):
        return self.stack.pop()

    @get_val_ext
    def get_val(self):
        return self.stack[len(self.stack) - 1]

    @stack_size_ext
    def stack_size(self):
        return len(self.stack)


plates = StackOfPlates()

for i in range(5):
    plates.push_in(i+1)

print(plates.stack_size())
print(plates.stack)
print(plates.get_val())
plates.pop_out()

plates.pop_out()
plates.pop_out()
print(plates.get_val())
plates.pop_out()

print(plates.get_val())
print(plates.is_empty())
