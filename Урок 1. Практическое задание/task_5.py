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
        self.elems = [[]]

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == []

    def push_in(self, el, n):
        """Предполагаем, что верхний элемент стека находится в конце списка
        если размер стопки равен пороговому значению то создается новая стопка
        и туда кладется значние, n - размер стопки"""

        if len(self.elems[len(self.elems) - 1]) < n:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        """Берем тарелку из крайней стопки, если она пустая удаляем ее"""
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        """Общее количество тарелок"""
        elem_sum = 0
        for stack in self.elems:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        """Количество стоек"""
        return len(self.elems)




def divide_by_two(dec_number):
    sc_obj = StackClass()

    while dec_number > 0:
        res = dec_number % 2
        sc_obj.push_in(res, 3)
        dec_number = dec_number // 2
    return sc_obj

print(divide_by_two(233))
