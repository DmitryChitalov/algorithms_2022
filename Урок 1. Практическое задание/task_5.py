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

class StackClass:
    
    st = 0
    st_top = 2
    
    def __init__(self):
        self.elems = [[]]

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems[self.st]) == self.st_top:
            self.st += 1
            self.elems.append([])
        self.elems[self.st].append(el)
        
    def pop_out(self):
        if len(self.elems[self.st]) == 1:
            self.st -= 1
            a = self.elems[self.st + 1][0]
            self.elems.pop()
            return a
        else:
            return self.elems[self.st].pop()

    def get_val(self):
        return self.elems[self.st][len(self.elems[self.st]) - 1]

    def stack_size(self):
        for i in range(self.st + 1):
            print('Размер стопки',  i + 1 , ':', len(self.elems[i]))
        return len(self.elems)