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


class StackPlatesClass:
    def __init__(self, max_size):
        self.elems = []
        self.max_size = max_size  # максимальное количество тарелок в стопке

    def is_empty(self):
        return self.elems == []

    def push_in(self):
        if len(self.elems) == 0 or len(self.elems[-1]) == self.max_size:
            self.elems.append([])
            self.elems[-1].append('plate')
        else:
            self.elems[-1].append('plate')

    def pop_out(self):
        if len(self.elems) == 0:
            print('В стопке не осталось тарелок')
        else:
            self.elems[-1].pop()
            if len(self.elems[-1]) == 0:
                self.elems.pop()

    def stack_size(self):
        if len(self.elems) > 1:
            return f'{(len(self.elems) - 1) * self.max_size + len(self.elems[-1])} тар.'
        if len(self.elems) == 1:
            return f'{len(self.elems[0])} тар.'
        return '0 тар.'


if __name__ == '__main__':
    a = StackPlatesClass(2)
    print(a.stack_size())
    for i in range(3):
        a.push_in()
    print(a.stack_size())
    for i in range(2):
        a.pop_out()
    print(a.stack_size())
    print(a.is_empty())

    a = StackPlatesClass(10)
    print(a.stack_size())
    for i in range(55):
        a.push_in()
    print(a.stack_size())
    for i in range(33):
        a.pop_out()
    print(a.stack_size())
    for i in range(23):
        a.pop_out()
    print(a.stack_size())
    print(a.is_empty())
