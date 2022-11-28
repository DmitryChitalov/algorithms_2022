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
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_stack(self, el, n):
        self.elems.append([])
        for i in range(len(self.elems)):
            if len(self.elems[i]) < n:
                self.elems[i].append(el)
                break


    def push_in(self):
        self.elems.append(el)


    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def stopka(self):
        if self.stack_size() > 2:
            self.elems.append(self.pop_out())



SC_OBJ = StackClass()

def divide_by_two(dec_number):
    sc_obj = StackClass()

    while dec_number > 0:
        res = dec_number % 2
        sc_obj.push_stack(res, 2)
        dec_number = dec_number // 2


    temp_lst = []
    while not sc_obj.is_empty():
        temp_lst.append(sc_obj.pop_out())
    return temp_lst



print(divide_by_two(233))
