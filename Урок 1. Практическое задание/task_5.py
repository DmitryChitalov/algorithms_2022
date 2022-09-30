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


class PlateClass:
    def __init__(self):
        self.lst = [[]]
        self._max = 3  # максимум в стопке
        self._current = 0  # Текущая стопка

    def is_empty(self):
        return self.lst == [[]]

    def push_in(self, el):
        if len(self.lst[self._current]) >= self._max:
            self._current += 1
            self.lst.append([])
        self.lst[self._current].append(el)

    def pop_out(self):
        par = self.lst[self._current].pop()
        if len(self.lst[self._current]) == 0:
            if self._current == 0:
                raise NameError('Ошибка ввода данных!')
            self._current -= 1
            self.lst.pop()

    def __str__(self):

        return (f'{self.lst}')

    def stack_size(self):
        return (self._current + 1)


if __name__ == '__main__':
    Pl = PlateClass()
    for j in range(7):
        Pl.push_in(j)

    print(Pl)
    print(f'количество стопок {Pl.stack_size()}')

    for j in range(3):
        Pl.pop_out()

    print(Pl)
    print(f'количество стопок {Pl.stack_size()}')
