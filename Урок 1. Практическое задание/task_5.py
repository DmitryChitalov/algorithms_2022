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
    def __init__(self, max_size):
        self.elems = [[]]
        self.max_size = max_size
    def push_in(self, el):
        if len(self.elems[len(self.elems) - 1]) < self.max_size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)
    def pop_out(self):
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return self.elems[-1].pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

if __name__ == '__main__':
    stack_1 = StackClass(2)
    stack_1.push_in(1)
    stack_1.push_in(2)
    stack_1.push_in(3)
    stack_1.push_in(4)
    stack_1.push_in(5)
    stack_1.push_in(6)
    stack_1.pop_out()
    stack_1.pop_out()
    stack_1.pop_out()
    stack_1.pop_out()
    stack_1.pop_out()
    print(stack_1.elems)


