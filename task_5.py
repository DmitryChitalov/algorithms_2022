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

class PilesPlatesClass:
    def __init__(self, max_plates):
        self.max_plates = max_plates  # максимальное число тарелок в стопке
        self.cur_pile = []  # текущая стопка
        self.piles = []  # список полных стопок

    def is_empty(self):
        return self.cur_pile == [] and self.piles == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.cur_pile) + 1 == self.max_plates:
            self.cur_pile.append(el)
            self.piles.append(self.cur_pile)
            self.cur_pile = []
        else:
            self.cur_pile.append(el)

    def pop_out(self):
        if len(self.cur_pile) == 0:
            if len(self.piles) > 0:
                self.cur_pile = self.piles[len(self.piles) - 1]
                self.piles.pop()
                return self.cur_pile.pop()
            else:
                return
        else:
            return self.cur_pile.pop()

    def get_val(self):
        if len(self.cur_pile) > 0:
            return self.cur_pile[len(self.cur_pile) - 1]
        else:
            if len(self.piles) > 0:
                return self.piles[len(self.piles) - 1][len(self.max_plates) - 1]
            else:
                return

    @property
    def count_full_piles(self):
        return len(self.piles)

    @property
    def count_cur_plates(self):
        return len(self.cur_pile)

    @property
    def count_all_plates(self):
        return len(self.cur_pile) + len(self.piles) * self.max_plates



if __name__ == '__main__':

    PP_OBJ = PilesPlatesClass(5)

    print(PP_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    PP_OBJ.push_in(1)
    PP_OBJ.push_in(2)
    PP_OBJ.push_in(3)
    PP_OBJ.push_in(4)
    PP_OBJ.push_in(5)
    PP_OBJ.push_in(6)
    PP_OBJ.push_in(7)

    # число полных стопок
    print(PP_OBJ.count_full_piles)  # -> 1

    # число тарелок в текущей неполной стопке
    print(PP_OBJ.count_cur_plates)  # -> 2

    # общее число тарелок во всех стопках
    print(PP_OBJ.count_all_plates)  # -> 7

    # получаем значение первого элемента с вершины стека,
    # но не удаляем сам элемент из стека
    print(PP_OBJ.get_val())  # -> 7

    print(PP_OBJ.is_empty())  # -> стек уже непустой

    # убираем элемент с вершины стека и возвращаем его значение
    print(PP_OBJ.pop_out())  # -> 7

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(PP_OBJ.pop_out())  # -> 6

    # число тарелок в текущей неполной стопке
    print(PP_OBJ.count_cur_plates)  # -> 0

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(PP_OBJ.pop_out())  # -> 5

    # число полных стопок
    print(PP_OBJ.count_full_piles)  # -> 0

    # число тарелок в текущей неполной стопке
    print(PP_OBJ.count_cur_plates)  # -> 4


