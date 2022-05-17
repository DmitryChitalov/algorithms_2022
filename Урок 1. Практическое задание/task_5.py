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


class PlateStacks:
    class PlateStack:
        def __init__(self, max_size=5):
            self.__max_size = max_size  # Максимальный размер стопки
            self.plates = []  # Пустое хранилище элементов

        def __bool__(self):
            return bool(self.plates)

        def push(self, element):
            if len(self.plates) < self.__max_size:
                self.plates.append(element)
                return True
            else:
                return False

        def pop(self):
            return self.plates.pop()

        def __str__(self):
            return self.plates.__str__()

    def __init__(self, max_size=5):
        self.stacks = []
        self.max_size = max_size
        self.len = 0

    def push(self, el):
        if self.stacks:
            if self.stacks[-1].push(el):
                return
        self.stacks.append(self.PlateStack(self.max_size))
        self.stacks[-1].push(el)

    def pop(self):
        if self.stacks:
            result = self.stacks[-1].pop()
            if not self.stacks[-1]:
                self.stacks.pop(-1)
            return result

    def __str__(self):
        result = []
        for stack in self.stacks:
            result.append(stack.plates)
        return result.__str__()


test = PlateStacks(5)  # Создадим стопку стопок тарелок, максимальным размером 5
for plate in range(5):  # Положим 5 тарелок от 0 до 4
    test.push(plate)
print(test)  # -> Должно быть [[0,1,2,3,4]]
for plate in range(3):  # Положим 3 тарелки с названиями '0','1','2'
    test.push(plate.__str__())
print(test)  # -> Должно быть [[0,1,2,3,4],['0','1','2']]
test.push(0.54)  # Добавим 1 тарелку 0.54
print(test)  # -> Должно быть [[0,1,2,3,4],['0','1','2', 0.54]]
test.pop()  # Удалим одну тарелку
print(test)  # -> Должно быть [[0,1,2,3,4],['0','1','2']]
for i in range(4):  # Удалим четыре тарелки
    test.pop()
print(test)  # -> Должно быть [[0,1,2,3]]
