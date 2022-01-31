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
class StackOfPlates():
    def __init__(self):
        self.plates = []
        self.plates.append([])

    def put_down_the_plate(self, plate):
        if len(self.plates[-1]) == 5:
            self.plates.append([])
            self.plates[-1].append(plate)
        else:
            self.plates[-1].append(plate)

    def show_stacks(self):
        return self.plates

    def clear_the_plate(self):
        if self.plates[-1] == []:
            self.plates.pop()
        return self.plates[-1].pop()


test = StackOfPlates()
test.put_down_the_plate('plate1')
test.put_down_the_plate('plate2')
test.put_down_the_plate('plate3')
test.put_down_the_plate('plate4')
test.put_down_the_plate('plate5')
test.put_down_the_plate('plate6')
test.put_down_the_plate('plate7')
test.put_down_the_plate('plate8')
test.put_down_the_plate('plate9')
test.put_down_the_plate('plate10')
test.put_down_the_plate('plate11')
print(test.clear_the_plate())
print(test.clear_the_plate())
print(test.clear_the_plate())
print(test.show_stacks())
