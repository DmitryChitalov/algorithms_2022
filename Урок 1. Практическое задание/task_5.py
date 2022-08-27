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

class PlateStClass:
    def __init__(self, n, s):  # n-кол-во тарелок в стеке, s- общее кол-во тарелок
        self.stack_m = []
        self.st_size = n
        self.all = s

    def __str__(self):
        return str(self.stack_m)

    def is_empty(self):
        return self.stack_m == [[]]

    def plate_in(self):
        j = 0
        while j < self.all:
            if (self.all - j) < self.st_size:
                self.st_size = (self.all - j)
            stack_n = []
            for i in range(self.st_size):
                stack_n.append(f'plate {j}')
                j += 1
            self.stack_m.append(stack_n)
        return self.stack_m

    def plate_out(self):
        result = self.stack_m[len(self.stack_m) - 1].pop()
        if len(self.stack_m[len(self.stack_m) - 1]) == 0:
            self.stack_m.pop()
        return result




if __name__ == '__main__':
    plates = PlateStClass(10, 28)
    print(type(plates))
    plates.plate_in()
    print(plates)
    print(plates.plate_out())
    print(plates.plate_out())
    print(plates.plate_out())

