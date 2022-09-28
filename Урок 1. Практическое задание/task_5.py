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

class Stack:
    def __init__(self, max_one_stack : int = 7):
        self.stack = []
        self.max_stack = max_one_stack
        self.index_list = 0

    def stack_put(self, item):
        if len(self.stack) == 0:
            self.stack.append(list())
        if len(self.stack[self.index_list]) == self.max_stack:
            self.stack.append(list())
            self.index_list += 1
        self.stack[self.index_list].append(item)

    def stack_get(self):
        if len(self.stack) == 0:
            print('Стэк пустой')
            return None
        else:
            item = self.stack[self.index_list].pop()

        if len(self.stack[self.index_list]) == 0:
            self.stack.pop()
            self.index_list -= 1
            if self.index_list == -1: self.index_list = 0

        return item

    def stack_print(self):
        print(self.stack)


# ПРОВЕРКА:
if __name__ == '__main__':
    stack = Stack(3)
    item = input("Укажите что положить в stack: ")
    while item != 'stop':
        stack.stack_put(item)
        item = input("Укажите что положить в stack: ")
    stack.stack_print()

    item = None
    while item != 'stop':
        elem = stack.stack_get()
        print('Достал из стека элемент:', elem, 'Остаток стека:')
        stack.stack_print()
        item = input("Еще один элемент достаем? ")

    item = None
    item = input("Укажите что положить в stack: ")
    while item != 'stop':
        stack.stack_put(item)
        item = input("Укажите что положить в stack: ")
    stack.stack_print()

    item = None
    while item != 'stop':
        elem = stack.stack_get()
        print('Достал из стека элемент:', elem, 'Остаток стека:')
        stack.stack_print()
        item = input("Еще один элемент достаем? ")