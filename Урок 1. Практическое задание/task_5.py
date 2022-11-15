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


class PlatesStack:
    def __init__(self):
        self.full_st = [[]]

    def push_in(self, el):
        n = (len(self.full_st) - 1)
        if len(self.full_st[n]) < 4:
            self.full_st[n].append(el)
        else:
            self.full_st.append([])
            n = n + 1
            self.full_st[n].append(el)

    def pop_out(self):
        pop_el = self.full_st[(len(self.full_st) - 1)].pop()
        if len(self.full_st[(len(self.full_st) - 1)]) == 0:
            del self.full_st[(len(self.full_st) - 1)]
        return pop_el

    def get_val(self):
        sub_st = self.full_st[len(self.full_st) - 1]
        last_el = sub_st[len(sub_st) - 1]
        return last_el

    def stack_size(self):
        count = 0
        for v in self.full_st:
            count += (len(v))
        return count

    def is_empty(self):
        for v in self.full_st:
            return v == []

    def show_stack(self):
        return self.full_st


if __name__ == '__main__':

    plates = PlatesStack()

    print(plates.is_empty())

    i = 0
    a = 1
    while i < 10:
        plates.push_in(a)
        a = a + 1
        i = i + 1

    print(plates.stack_size())
    print(plates.show_stack())
    print(plates.pop_out())
    print(plates.get_val())
    print(plates.is_empty())
