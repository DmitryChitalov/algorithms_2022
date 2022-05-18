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
    def init(self):
        self.plats = []
        self.stack = []

    def is_empty(self):
        return self.plats == []

    def push_in(self, plat):
        if len(self.stack) == 3:
            self.plats.append(self.stack)
            self.stack = []
            self.stack.append(plat)

    def pop_out(self):
        return self.stack.pop()

    def stack_size(self):
        return 'Большая стопка - {}, маленькая стопка - {}'.format(self.plats, self.stack)
        
if __name__ == '__main__':

    plats = StackOfPlates()
    
    plats.push_in(plat=1)
    plats.push_in(plat=1)
    plats.push_in(plat=1)
    plats.push_in(plat=1)
    plats.push_in(plat=1)
    plats.push_in(plat=1)
    plats.push_in(plat=1)
    plats.push_in(plat=1)
    
    print plats.stack_size()
