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


class StackOfPlatesClass:
    def __init__(self):
        self.elements = []
        self.max_size = 3

    def empty(self):
        return self.elements == []

    def pop(self):
        if len(self.elements) == 0:
            return None
        removed = self.elements.pop()
        return removed

    def push(self, el):
        if len(self.elements) == 0:
            new_stack_plate = [el]
            self.elements.append(new_stack_plate)

        elif len(self.elements[len(self.elements) - 1]) == self.max_size:
            new_stack_plate = [el]
            self.elements.append(new_stack_plate)
        else:
            self.elements[len(self.elements) - 1].append(el)

    def get_val(self):
        return self.elements[len(self.elements) - 1]

    def stack_size(self):
        cnt_elements = 0
        for el in self.elements:
            cnt_elements += len(el)
        return cnt_elements


# Проверка
plate_obj = StackOfPlatesClass()
plate_obj.push(1)
plate_obj.push(2)
plate_obj.push(3)
plate_obj.push(4)

print(plate_obj.elements)
