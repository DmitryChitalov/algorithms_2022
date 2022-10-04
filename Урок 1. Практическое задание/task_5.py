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
class PlatesStack:
    def __init__(self):
        self.plates = [[]]

    def is_empty(self):
        return self.plates == [[]]

    def push_in(self, plates):
        if len(self.plates[-1]) == 5:
            self.plates.append([plates])
        else:
            self.plates[-1].append(plates)

    def pop_out(self):
        result = self.plates[-1].pop()
        if len(self.plates[-1]) == 0:
            self.plates.pop()
        return result

    def get_val(self):
        return self.plates[-1][-1]

    def stack_size(self):
        j = len(self.plates)
        if j > 1:
            j = (j-1)*5 + len(self.plates[-1])
        return j


if __name__ == '__main__':

    pl1 = PlatesStack()
    print(pl1.is_empty())  # пустая ли стопка тарелок?
    pl1.push_in('red1')
    pl1.push_in('green1')
    pl1.push_in('green2')
    print(pl1.is_empty())
    pl1.push_in('blue1')
    pl1.push_in('yellow1')
    pl1.push_in('red2')
    pl1.push_in('orange1')
    pl1.push_in('blue2')
    pl1.push_in('yellow2')
    pl1.push_in('orange2')
    pl1.push_in('orange3')
    pl1.push_in('orange4')
    #print(pl1.get_val())  # первая тарелка с вершины последней стопки
    #print(pl1.stack_size())  # количество тарелок
    #print(pl1.pop_out())  # убираем последнюю тарелку
    #print(pl1.stack_size())  # количество тарелок