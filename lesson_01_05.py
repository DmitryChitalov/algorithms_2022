"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""


class PlateStackClass:
    def __init__(self, max_count):
        self.elements = []
        self.max_count = max_count
        self.shelf_list = []

    def is_empty(self):
        return print(self.elements == [])

    def push_in(self, item):
        if len(self.elements) == self.max_count:
            self.shelf_list.insert(0, self.elements)
            self.elements = [item]
        else:
            self.elements.insert(0, item)
        return self.elements

    def pop_out(self):
        self.elements.pop(0)
        return print('One item was deleted')

    def get_val(self):
        return print(f'Now in a stack: {len(self.elements)} plate(s) --> {self.elements}')

    def shelf_count(self):
        return print(f'On the shelf {len(self.shelf_list)} stack(s) of plates')


a = PlateStackClass(2)
a.push_in(1)
a.push_in(2)
a.push_in(3)
a.push_in(4)
a.push_in(5)
a.push_in(6)

a.get_val()
a.shelf_count()
a.pop_out()
a.get_val()


