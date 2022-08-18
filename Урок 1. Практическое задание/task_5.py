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


class Stackstorage:
    Stack = 10

    def __init__(self):
        self.item_list = [[0]]

    def check_stack(self):
        n = self.item_list[-1][0] #количество тарелок в последней стопке
        return n

    def app_item(self, quanty):
        """добавляет тарелки в стопки"""
        checkspace = self.check_stack() + quanty  #сумма стака
        while checkspace != 0:
            if checkspace > 10:                      # добавление новой полной стопки
                checkspace -= 10
                self.item_list[-1][0] = 10
                self.item_list.append([0])           # добавление новой пустой стопки
            else:  #добавление в пустую стопку, если меньше 10 тарелок
                self.item_list[-1][0] = checkspace
                checkspace = 0

    def remove_item(self, quanty):
        """убрать тарелки"""
        total = ((len(self.item_list) - 1) * self.Stack) + self.item_list[-1][0]
        if quanty > total:
            self.item_list = [[0]]
        else:
            remain = total - quanty
            self.item_list = [[0]]
            while remain != 0:
                if remain > 10:
                    remain -= 10
                    self.item_list[-1][0] = 10
                    self.item_list.append([0])
                else:
                    self.item_list[-1][0] = remain
                    remain = 0

    @property
    def show_stacks(self):
        print(self.item_list)


if __name__ == '__main__':
    platestorage = Stackstorage()
    platestorage.show_stacks
    platestorage.app_item(1)
    platestorage.app_item(32)
    platestorage.show_stacks
    platestorage.app_item(78)
    platestorage.show_stacks
    platestorage.remove_item(11111)
    platestorage.show_stacks
    platestorage.app_item(43)
    platestorage.show_stacks
    platestorage.remove_item(18)
    platestorage.show_stacks


