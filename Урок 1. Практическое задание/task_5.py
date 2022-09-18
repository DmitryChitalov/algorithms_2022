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
class StakePlates:
    MAX_SIZE = 5

    def __init__(self):
        self.elems = [[]]

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[len(self.elems) - 1]) < StakePlates.MAX_SIZE:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        if not self.is_empty():
            out = self.elems[len(self.elems) - 1].pop()
            if not len(self.elems[len(self.elems) - 1]) and len(self.elems) > 1:
                self.elems.pop()
            return out
        else:
            return None

    def get_val(self):
        if not self.is_empty():
            return self.elems[len(self.elems) - 1][-1]
        else:
            return None

    def stack_size(self):
        out = 0
        for el in self.elems:
            out = out + len(el)
        return out
    print('Размер стопки: ', MAX_SIZE)

if __name__ == '__main__':
    list = [el for el in range(0, 14)]

    stack = StakePlates()
    for item in list:
        stack.push_in(item)

    print(stack.elems)
    print(stack.pop_out())
    print(stack.get_val())