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
    def __init__(self, size_stc):
        self.elems = [[]]
        # self.max_stc = 5
        self.i = -1
        self.num_sc = 0
        self.size_stack = size_stc

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):

        self.i += 1
        self.num_sc = int(self.i // self.size_stack)
        if self.num_sc >= len(self.elems):
            self.elems.append([])
        self.elems[self.num_sc].append(el)
        # print(self.num_sc)
        # print(self.elems)


    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def get_elems(self):
        return self.elems


    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':

    def data_to_stack(lst, size_stc):
        sc_obj = StackClass(size_stc)

        for j in range(len(inp_list)):
            sc_obj.push_in(inp_list[j])

        return sc_obj.get_elems()

    inp_list = [100, 'text', False, 50.8, 'letters', 'some text', 35.6, 652.9, 25, 90, True, 'yesterday']

    print(data_to_stack(inp_list, 3))
    print(data_to_stack(inp_list, 4))