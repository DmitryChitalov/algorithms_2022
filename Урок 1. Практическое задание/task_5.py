"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""


class StackClass:
    def __init__(self):
        self.elems_list = []  # массив стопок
        self.elems = []
        self.MAX_SIZE_STACK = 5  # максимальное значение элементов в стопке

    def __str__(self):  # строковое представлени объекта (построчно каждую стопку)
        list_ = self.elems_list[:]
        list_.append(self.elems)
        return 'Stack:\n' + '\n'.join([' '.join([str(y) for y in x]) for x in list_])

    def is_empty(self):
        return not (self.elems or self.elems_list)  # True - пустой

    def push_in(self, el):
        if len(self.elems) >= self.MAX_SIZE_STACK:
            self.elems_list.append(self.elems)  # полную стопку в массив стопок
            self.elems = []  # инициализируем массив эл-тов
        self.elems.append(el)

    def pop_out(self):
        if self.is_empty():  # массив стопок и массив эл-тов пусты
            return None
        if not self.elems and self.elems_list:
            self.elems = self.elems_list.pop()  # массив стопок из массива эл-тов
        return self.elems.pop()

    def get_val(self):
        if self.is_empty():
            return None
        if self.elems:
            return self.elems[len(self.elems) - 1]  # из массива эл-тов
        return self.elems_list[len(self.elems_list) - 1][self.MAX_SIZE_STACK - 1]   # эл-т из массив стопок

    def stack_size(self):
        return len(self.elems) + len(self.elems_list) * self.MAX_SIZE_STACK


if __name__ == '__main__':
    stack = StackClass()

    # проверяем работу стека
    print(f'{stack.is_empty()=} {stack.stack_size()=}')  # True -> стек пустой, эл-тов 0
    print('наполняем стек')
    for i in range(15):
        stack.push_in(i)
    for i in ['text1', {'aaa': 221}, ('bbb', 222), False, True, 5.5, 7.7]:
        stack.push_in(i)
    print(stack)
    print(f'{stack.is_empty()=} {stack.stack_size()=}')

    print('stack.pop_out():', end=' ')
    for i in range(21):
        print(f'{stack.pop_out()}', end=' ')
    print(f'\n{stack.stack_size()=}')
    print(f'{stack.pop_out()=}')  # 0: последнее значение
    print(f'{stack.pop_out()=}')  # None: попытка получить значение из пустого стека
    print('снова наполняем стек')
    for i in range(6):
        stack.push_in(i)
    print(stack)
    print(f'{stack.get_val()=}')  # эл-т из массива эл-тов
    print(f'{stack.pop_out()=}')  # массив эл-тов пустой
    print(stack)
    print(f'{stack.get_val()=}')  # эл-т из массив стопок

