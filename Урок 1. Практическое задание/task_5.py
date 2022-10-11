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
    def __init__(self, size):
        self.elems = []
        self.one_stack_size = size

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems) == 0 or len(self.elems[-1]) == 10:
            self.elems.append([])
        self.elems[-1].append(el)

    def pop_out(self):
        """Если берём последний элемент из списка, то удалаяем список"""
        next_elem = self.elems[-1].pop()
        if len(self.elems[-1]) == 0:
            self.elems.pop()
        return next_elem

    def get_val(self):
        return 'no elements' if len(self.elems) == 0 else self.elems[-1][-1]

    def last_stack_size(self):
        return 0 if len(self.elems) == 0 else len(self.elems[-1])

    def number_of_stacks(self):
        return len(self.elems)

    def show_all(self):
        """
        Выводим список всех элементов,
        Каждый вложенный список выводим на отдельную строку"""
        show_all_str = ''
        for el in self.elems:
            show_all_str += ', '.join(el) + '\n'
        return show_all_str

    def describe(self):
        return f'On shelves {self.number_of_stacks()} stacks, in last {self.last_stack_size()} elements'


if __name__ == '__main__':
    shelves_for_plates = StackClass(10)

    print('we put 22 plates on shelves')
    number_of_plates = 22
    for i in range(1, number_of_plates + 1):
        shelves_for_plates.push_in(f'plate {i}')
    print(shelves_for_plates.describe())

    print('we took 5 plates')
    plates_to_take = 5
    for i in range(plates_to_take):
        shelves_for_plates.pop_out()
    print(shelves_for_plates.describe())
