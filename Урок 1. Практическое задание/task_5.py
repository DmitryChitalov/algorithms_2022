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


class Stack_of_stacks:
    def __init__(self):
        self.elem = [[]]

    def is_empty(self):
        return self.elem == [[]]

    def push_in(self, el):
        if len(self.elem[-1]) + 1 > 10:  # добавление новой стопки в 10 элементов
            self.elem.append([])
        self.elem[-1].append(el)

    def pop_out(self):  # удаление последнего элемента
        last = self.elem[-1].pop()
        if len(self.elem[-1]) == 0:  # если элементы был последним в стопке, то удаляем ее
            self.elem.pop()
        return last

    def get_val(self):  # Значение последнего элемента в последней стопке
        return self.elem[-1][-1]

    def stack_size(self):  # количество всех элементов
        return len(self.elem[-1]) + (len(self.elem) - 1) * 10

    def num_stacks(self):  # количество стопок
        return (len(self.elem))

    def num_in_last(self):  # Количество элементов в последней стопке
        return len(self.elem[-1])


plates = Stack_of_stacks()
print(plates.is_empty())

for i in range(11):
    plates.push_in(i)

print(plates.stack_size())
print(plates.num_stacks())
print(plates.num_in_last())

print(plates.pop_out())

print(plates.stack_size())
print(plates.num_stacks())
print(plates.num_in_last())
