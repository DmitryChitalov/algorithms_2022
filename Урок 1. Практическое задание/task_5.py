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


class StackOfPlates:
    def __init__(self):
        self.elems = [[], [], [], [], [], [], [], [], []]

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        # предпологаем что верхний элемент стека находится в конце списка
        for a in range(0, len(self.elems) - 1, 1):
            if len(self.elems[a]) < 5:
                self.elems[a].append(el)
                break

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        elem_sum = 0
        for stack in self.elems:
            elem_sum += len(stack)
        return elem_sum

    def stack_plate(self):
        return len(self.elems)


if __name__ == "__main__":
    plates = StackOfPlates()
    i = 0
    # укажите количество тарелок
    j = 23
    while i < j:
        plates.push_in(1 + i)
        i += 1

    print(plates.elems)
