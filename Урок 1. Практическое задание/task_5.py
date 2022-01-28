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


class MyStack:
    def __init__(self, max_size):
        self.elements = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.elements)

    def is_empty(self):
        return self.elements == []

    def push_to_stack(self, el):
        # Добавляем пустую стопку, если достигнут максимальный размер стопки
        if len(self.elements[len(self.elements)-1]) == self.max_size:
            self.elements.append([])
        self.elements[len(self.elements)-1].append(el)

    def pop_from_stack(self):
        if self.is_empty():
            return None
        result = self.elements[len(self.elements)-1].pop()
        if len(self.elements[len(self.elements)-1]) == 0:     # Убираем пустую стопку
            self.elements.pop()
        return result

    def stack_size(self):  # Общее количество элементов в стеке
        result = 0
        for stack in self.elements:
            result += len(stack)
        return result

    def stack_count(self):  # Количество стоек
        return len(self.elements)

    def get_val(self):  # Возвращает последнее значение
        return self.elements[len(self.elements) - 1]


if __name__ == '__main__':
    plates = MyStack(3)
    plates.push_to_stack('1')
    plates.push_to_stack('2')
    plates.push_to_stack('3')
    plates.push_to_stack('4')
    plates.push_to_stack('5')
    plates.push_to_stack('6')
    plates.push_to_stack('7')
    print(plates)
    print(f'Количество элементов: {plates.stack_size()}, количество стопок: {plates.stack_count()}')
    plates.pop_from_stack()
    plates.pop_from_stack()
    print(plates)
    print(f'Количество элементов: {plates.stack_size()}, количество стопок: {plates.stack_count()}')
    plates.pop_from_stack()
    plates.pop_from_stack()
    plates.pop_from_stack()
    plates.pop_from_stack()
    plates.pop_from_stack()
    plates.pop_from_stack()
    print(plates)
    print(f'Количество элементов: {plates.stack_size()}, количество стопок: {plates.stack_count()}')