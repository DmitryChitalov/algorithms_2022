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
    def __init__(self, max_plate=5):
        self.elems = []
        self.max_plate = max_plate

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems) == 0:
            new_plate_stack = [el]
            self.elems.append(new_plate_stack)

        elif len(self.elems[len(self.elems)-1]) == self.max_plate:
            new_plate_stack = [el]
            self.elems.append(new_plate_stack)
        else:
            self.elems[len(self.elems)-1].append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


plate_ob1 = PlateStackClass(5)
plate_ob1.push_in(1)
plate_ob1.push_in(2)
plate_ob1.push_in(3)
plate_ob1.push_in(4)
plate_ob1.push_in(5)
plate_ob1.push_in(6)
plate_ob1.push_in(7)
plate_ob1.push_in(8)
plate_ob1.push_in(9)
plate_ob1.push_in(10)
plate_ob1.push_in(11)

print(plate_ob1.elems)
