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


class StackClass:
    def __init__(self):
        self.elems = []

    def __str__(self):
        return f'{self.elems}'

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems) == 0:
            self.elems.append([])
        if len(self.elems[-1]) < 5:
            self.elems[-1].append(el)
        elif len(self.elems[-1]) == 5:
            self.elems.append([])
            self.elems[-1].append(el)

    def pop_out_stack(self):
        return self.elems.pop()

    def pop_out_elem(self):
        return self.elems[-1].pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def count_of_steck(self):
        return len(self.elems)

    def count_of_plates(self):
        count = 0
        for x in range(len(self.elems)):
            count += len(self.elems[x])
        return count


if __name__ == '__main__':
    plates = StackClass()

    print(plates.is_empty())  # -> стек пустой

    # наполняем стек
    plates.push_in('plate')
    plates.push_in('plate')
    plates.push_in('plate')
    plates.push_in('plate')
    plates.push_in('plate')
    plates.push_in('plate')
    plates.push_in('plate')
    plates.push_in('plate')
    plates.push_in('plate')

    # получаем весь стек
    print(plates)  # -> [['plate', 'plate', 'plate', 'plate', 'plate'], ['plate', 'plate', 'plate', 'plate']]

    # получаем первой стопки с вершины стека,
    # но не удаляем саму стопку из стека
    print(plates.get_val())  # -> ['plate', 'plate', 'plate', 'plate']

    # узнаем количество стопок
    print(plates.count_of_steck())  # -> 2

    # узнаем количество тарелок
    print(plates.count_of_plates())  # -> 4

    print(plates.is_empty())  # -> стек уже непустой

    # убираем стопку с вершины стека и возвращаем его значение
    print(plates.pop_out_stack())  # -> ['plate', 'plate', 'plate', 'plate']

    # убираем элемент из стопки с вершины стека и возвращаем его значение
    print(plates.pop_out_elem())  # -> plate

    # вновь узнаем количество стопок
    print(plates.count_of_steck())  # 1
