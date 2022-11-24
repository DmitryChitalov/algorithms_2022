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

class Stack_of_plates:
    '''Складывание в стопки по 10 тарелок'''
    def __init__(self):
        self.stacks = [[]]

    def folding(self):
        if len(self.stacks[-1]) < 10:
            self.stacks[-1].append(1)
        else:
            self.stacks.append([])
            self.stacks[-1].append(1)
        return self.stacks

add_plates = Stack_of_plates()
for _ in range(34):
    print(add_plates.folding())