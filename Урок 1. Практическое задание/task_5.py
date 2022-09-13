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
    def __init__(self, max_count_in_stack):
        self.stack = [[]]
        self.max_count = max_count_in_stack
        self._current_stack = 0

    def __str__(self):
        return f'{self.stack}'

    def push_in(self, count=1):
        for i in range(count):
            if len(self.stack[self._current_stack]) == self.max_count:
                self._current_stack += 1
                self.stack.append([])
            self.stack[self._current_stack].append(1)

    def pop_out(self, count=1):
        return_stack = StackOfPlates(self.max_count)
        for i in range(count):
            return_stack.push_in(self.stack[self._current_stack].pop())
            if len(self.stack[self._current_stack]) == 0:
                self.stack.pop()
                self._current_stack -= 1
        return return_stack


if __name__ == '__main__':
    stack = StackOfPlates(10)
    stack.push_in(13)
    stack.pop_out(2)
    stack.push_in()
    stack.pop_out()
    print(stack)