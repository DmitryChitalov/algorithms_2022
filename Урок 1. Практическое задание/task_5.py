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


class DishStackClass():
    def __init__(self):
        self.i = 0
        self.elems = []


    def is_empty(self):
        if self.elems == []:
            return True
        else:
            return False

    def push_in(self,el):
        if self.elems == []:
            self.elems.append([el])
        elif self.elems != [] and len(self.elems[self.i]) < 10:
            self.elems[self.i].append(el)
        else:
            self.i +=1
            self.elems.append([el])



    def pop_out(self):
        if self.elems == []:
            raise ValueError (" Stack is empty")
            return
        if len(self.elems[self.i]) == 1:
            el = self.elems[self.i].pop()
            self.elems.pop()
            if self.elems == []:
                self.i = 0
            else :
                self.i -= 1
            return el
        return self.elems[self.i].pop()



    def get_value(self):
        return self.elems[self.i][len(self.elems[self.i]) - 1]

    def stack_size(self):
        if self.elems == []:
            return 0
        return len(self.elems[self.i]) + self.i * 10


if __name__ == '__main__':

    DISHES = DishStackClass()
    print (f'DISHES.i : {DISHES.i}')
    print (f'DISHES.elems : {DISHES.elems}')
    print (f'DISHES.is_empty : {DISHES.is_empty()}')

    for n in range (0,25):
        el_name = 'el'+str(n)
        DISHES.push_in(el_name)
        print(DISHES.i)
        print(DISHES.elems)
        if n in (3,6,12):
            print(f'stack_size = {DISHES.stack_size()} ')

    print(f'DISHES.is_empty: {DISHES.is_empty()}')
    print(f'DISHES.get_value: {DISHES.get_value()}')

    for n in range(0, 26):
        try :
            print(DISHES.pop_out())
        except  ValueError:
            print('stack is empty')
            break
        print(DISHES.i)
        print(DISHES.elems)





