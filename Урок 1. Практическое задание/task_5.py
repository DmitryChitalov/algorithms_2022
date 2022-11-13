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


class Stacks:
    def __init__(self):
        self.len_one_stack = 3
        self.stacks = []

    def push_stack(self):
        self.stacks.append([])

    def pop_stack(self):
        if len(self.stacks) == 0:
            return None
        self.stacks.pop()

    def push(self, item):
        if len(self.stacks) == 0:
            self.push_stack()
            self.stacks[-1].append(item)
        elif len(self.stacks[-1]) < self.len_one_stack:
            self.stacks[-1].append(item)
        else:
            self.push_stack()
            self.stacks[-1].append(item)

    def pop(self):
        if len(self.stacks) == 0:
            return True
        elif len(self.stacks[-1]) < 2:
            self.stacks[-1].pop()
            self.pop_stack()
        else:
            self.stacks[-1].pop()


s = Stacks()
print(s.stacks)

# Высота стопок
# s.len_one_stack = 4
print(f'Высота стопок {s.len_one_stack}')

# Заполнение стопок
n = 14 # сколько тарелок добавить

while n != 0:
    s.push("Т")
    n -= 1
print(s.stacks)

# Убираем тарелки
n = 13  # сколько тарелок убрать

while n != 0:
    x = s.pop()
    if x:
        print(f'Тарелки закончились. Не хватает {n} тарелок')
        break
    n -= 1
print(s.stacks)