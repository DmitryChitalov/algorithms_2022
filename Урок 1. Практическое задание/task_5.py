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


class StaksPlates:
    def __init__(self):
        self.elems = [[]]

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if el > 0:
            if not self.elems[-1]:
                self.elems[-1] = [1]
                el = el - 1
            while el > 0:
                if self.elems[-1] == [5]:
                    self.elems.append([])
                if not self.elems[-1]:
                    self.elems[-1] = [0]
                self.elems[-1][0] = self.elems[-1][0] + 1
                el -= 1
            print(f'Стопка по 5 тарелок: {self.elems}')

    def pop_out(self, el):
        while el > 0:
            if not self.elems[-1]:
                self.elems.pop()
            self.elems[-1][0] = self.elems[-1][0] - 1
            el -= 1
            if self.elems[-1] == [0]:
                self.elems.pop()
            if not self.elems:
                print(f'Нельзя убрать {el} тарелок, в стопке больше нет тарелок.')
                break
        if self.elems:
            print(f'Стопка по 5 тарелок: {self.elems}')

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':
    staks_1 = StaksPlates()
    staks_1.push_in(18)
    staks_1.pop_out(16)
    staks_1.pop_out(9)
