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

# при создании класса мы принимаем два аргумента - список, в котором находится название для каждой тарелки
# (в примерах я использовал для этого обычные числа), и размер стопки как число тарелок. Размеры стопок двух наборов
# могут не совпадать (что продемонстрировано в примерах) и поэтому приоритет отдается размеру первого набора стопок.
# При убавлении тарелок из набора просто удаляется заданное количество элементов из стопок (удаленные тарелки с этой командой отправляются в небытие)
class PlateStack:
    def __init__(self, plates, stack_size):
        self.stack_list = []
        self.plates = plates
        self.stack_size = stack_size
        for i in range(len(plates) // self.stack_size):
            self.stack_list.append(plates[i*self.stack_size:i*self.stack_size + self.stack_size])
        if len(plates) % self.stack_size == 0:
            self.stack_list.append([])
        else:
            self.stack_list.append(plates[-(len(plates) % self.stack_size):])

    def __add__(self, plates):
        extender = []
        extender_2 = []
        for i in self.stack_list:
            extender.extend(i)
        for j in plates.stack_list:
            extender_2.extend(j)
        extender_2.reverse()
        extender.extend(extender_2)
        self.stack_list.clear()
        for k in range(len(extender) // self.stack_size):
            self.stack_list.append(extender[k * self.stack_size:(k + 1) * self.stack_size])
        if len(extender) % self.stack_size == 0:
            self.stack_list.append([])
        else:
            self.stack_list.append(extender[-(len(extender) % self.stack_size):])
        return str(self.stack_list)

    def remove(self, num):
        while len(self.stack_list[-1]) <= num:
            num = num - len(self.stack_list[-1])
            self.stack_list.pop()
        if num != 0:
            for i in range(num):
                self.stack_list[-1].pop()
        elif num == 0:
            self.stack_list.append([])
        return str(self.stack_list)

    def __str__(self):
        return str(self.stack_list)

    def stacks_num(self):
        return print(str(len(self.stack_list)) + ' stacks')

    def plates_num(self):
        res = 0
        for i in self.stack_list:
            res += len(i)
        return print(str(res) + ' plates')

stacks_1 = PlateStack([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 9)
stacks_2 = PlateStack([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 6)
print(stacks_1)
print(stacks_2)
print(stacks_1 + stacks_2)
print(stacks_2 + stacks_1)
print(stacks_1.remove(7))
stacks_1.stacks_num()
stacks_2.stacks_num()
stacks_2.plates_num()