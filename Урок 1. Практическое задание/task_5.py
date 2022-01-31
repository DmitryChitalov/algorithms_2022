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


class Stack:

    def __init__(self, capacity):
        self._capacity = capacity
        self._elems = []
        self._add_stack()

    def push(self, element):
        if self.is_empty():
            self._add_stack()
        if len(self._current_stack) >= self._capacity:
            self._add_stack()
        self._current_stack.append(element)

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
            return None

        elem = self._current_stack.pop()
        if len(self._current_stack) <= 0:
            self._del_stack()
        return elem

    def is_empty(self):
        return self._elems == []

    def _set_current_stack(self):
        if not self.is_empty():
            self._current_stack = self._elems[len(self._elems) - 1]
        else:
            self._current_stack = None

    def _add_stack(self):
        self._elems.append([])
        self._set_current_stack()

    def _del_stack(self):
        if not self.is_empty():
            del self._elems[len(self._elems) - 1]
        self._set_current_stack()

    def __str__(self):
        return 'In stack:\n' + '\n'.join(map(str, self._elems))


if __name__ == "__main__":

    stack = Stack(6)

    for i in (1, 2):
        print(f'Round: {i} \n')

        for j in range(16):
            stack.push(j)

        print(stack)

        for j in range(10):
            print(stack.pop())

        print(stack)

        for j in range(10):
            print(stack.pop())

        print(stack)


