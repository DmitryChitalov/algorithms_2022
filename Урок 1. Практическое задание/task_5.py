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

class PlatesClass:
    def __init__(self):
        self.stacks = 1
        self.elems = []
        print('новый камод с тарелками')

    def is_empty(self):
        return self.elems == []

    def new_stack(self):
        self.stacks += 1
        self.elems.append('_')

    def push_in(self, el):
        """Предполагаем, что в камоде можно уложить стопки по три тарелки"""
        if len(self.elems) == 0 or len(self.elems) % 3 != 0:
            self.elems.append(el)
            return f'добавил тарелку {el} в камод {self.__dict__}'
        else:
            self.new_stack()
            self.elems.append(el)
            return f'больше 3-х в стопке, добавил тарелку {el} в новую стопку {(self.__dict__)}'

    def pop_out(self):
        if self.elems[-1:] == ['_']:
            self.elems.pop()
            self.stacks -= 1
        return f'убрал тарелку {self.elems.pop()}'

    def get_val(self):
        return f'взял тарелку {self.elems[len(self.elems) - 1]}'

    def stack_size(self):
        return f'стопок: {self.stacks}, тарелок: {len(self.elems) - self.elems.count("_")}'


if __name__ == '__main__':

    PC_KAMOD = PlatesClass()
    print(PC_KAMOD.push_in(1))
    print(PC_KAMOD.push_in(2))
    print(PC_KAMOD.push_in(3))
    print(PC_KAMOD.push_in(4))
    print(PC_KAMOD.push_in(5))
    print(PC_KAMOD.stack_size())
    print(PC_KAMOD.pop_out())
    print(PC_KAMOD.pop_out())
    print(PC_KAMOD.pop_out())
    print(PC_KAMOD.__dict__)
    print(PC_KAMOD.stack_size())
    print(PC_KAMOD.get_val())