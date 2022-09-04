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


class PlatesStacks:
    """
    Стопка тарелок
"""
    def __init__(self, num):
        """ num - количество тарелок в одной стопке"""
        self.elems = []
        self.num = num

    def is_empty(self):
        """
        нет тарелок
        """
        return not self.elems

    def push_in(self, element):
        """ добавление тарелок """
        if not self.is_empty() and len(self.elems[len(self.elems) - 1]) < self.num:
            self.elems[-1].append(element)
        else:
            self.elems.append([element])

    def pop_out(self):
        """ удаление тарелок """
        return self.elems[-1].pop()

    def get_val(self):
        """ возвращение последней добавленной тарелки """
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        """ количество тарелок в сумме """
        if self.is_empty():
            return 0
        return (len(self.elems) - 1) * self.num + len(self.elems[-1])


if __name__ == '__main__':
    ps_obj = PlatesStacks(4)
    ps_obj.push_in(765)
    ps_obj.push_in(23)
    ps_obj.push_in('jhjhg')
    ps_obj.push_in('567')
    ps_obj.push_in('123')
    ps_obj.push_in('456')
    ps_obj.push_in('jkuhg')
    print(ps_obj.pop_out())
    print(ps_obj.get_val())
    print(ps_obj.stack_size())
