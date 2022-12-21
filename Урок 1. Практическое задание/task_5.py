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
    def __init__(self, limit):
        self.elems = [[]]
        self.limit = limit

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        for i in range(len(self.elems)):
            if len(self.elems[i]) < self.limit:
                self.elems[i].append(el)
                if len(self.elems[i]) == self.limit:
                    self.elems.append([])
                break

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def print_stack(self):
        print(self.elems)

if __name__ == '__main__':
    max_limit = int(input("Пороговое значение: "))
    stack = PlateStack(max_limit)
    n = 0
    while n < max_limit:
        stack.push_in(n)
        n += 1
    stack.print_stack()
    stack.push_in(5)
    stack.push_in(3)
    stack.push_in(22)
    stack.print_stack()
