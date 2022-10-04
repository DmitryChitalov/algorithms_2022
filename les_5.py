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


class StackPlatesClass:

    def __init__(self):
        self.stacks_plates = []
        # устанавливаем ограничение на 4 тарелки в одной стопке
        self.size = 4
        self.plates = []

    # добавление объекта в стек
    def add(self, obj):
        if self.size == len(self.plates):
            self.stacks_plates.append(self.plates.copy())
            self.plates.clear()
            self.plates.append(obj)
        else:
            self.plates.append(obj)

    # удаление объекта из стека
    def take(self):
        if self.plates:
            self.plates.pop()
        elif self.stacks_plates:
            number_stacks = len(self.stacks_plates)
            self.stacks_plates[number_stacks-1].pop()
        else:
            print('Нет тарелок')

    # просмотр объектов в стеке
    def show(self):
        if self.plates:
            self.stacks_plates.append(self.plates)
        print(self.stacks_plates)


if __name__ == '__main__':
    stack = StackPlatesClass()

    stack.add('object_1')
    stack.add('object_2')
    stack.add('object_3')
    stack.add('object_4')
    stack.add('object_5')
    stack.add('object_6')
    stack.add('object_7')
    stack.add('object_8')
    stack.add('object_9')
    stack.add('object_10')
    stack.show() # добавили 10 тарелок

    stack.take()
    stack.take()
    stack.show() # удалили две тарелки

# [['object_1', 'object_2', 'object_3', 'object_4'],
# ['object_5', 'object_6', 'object_7', 'object_8'],
# ['object_9', 'object_10']]
#
#
# [['object_1', 'object_2', 'object_3', 'object_4'],
# ['object_5', 'object_6', 'object_7', 'object_8'], []]

