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
class stack_of_plates:
    def __init__(self):
        self.stack = []
        self.max_plate_in_stack = 5
        self.count_stack = 0
        self.count_plate = 0

    def put_in_stack(self, plate):
        if plate >= self.max_plate_in_stack:
            while plate >= self.max_plate_in_stack:
                plate -= self.max_plate_in_stack
                self.stack.append(self.max_plate_in_stack)
                self.count_stack += 1

        elif plate < self.max_plate_in_stack:
            self.count_plate = plate + self.count_plate
            print(self.count_plate)

            if self.count_plate == self.max_plate_in_stack:
                self.stack.append(self.max_plate_in_stack)
                self.count_stack += 1





if __name__ == '__main__':
    test = stack_of_plates()
    test.put_in_stack(10)  # кладем тарелки n
    test.put_in_stack(10)
    test.put_in_stack(1)
    print(" кол-во стопок ", test.count_stack)
    print(" кол-во тарелок всего ", test.stack)

class Plates:
    def __init__(self):
        self.plates = [[]]  # тарелки) начинаем с пустых стопок
        self.max = 3  # максимальное количество тарелок в стопке
        self.count = 0  # количество стопок, 0 - одна, 1 - две стопки и т.д.

    def plus_plate(self, plate):  # добавляем тарелку в стопку
        if len(self.plates[self.count]) == self.max:  # если количество тарелок в стопке предельно
            self.plates.append([])  # добавляем новую стопку (новый список)
            self.count += 1  # увеличиваем на 1 количество стопок
        self.plates[self.count].append(plate)  # добавляем тарелку в нужную стопку

    def minus_plate(self):  # удаляем тарелку
        if self.plates == [[]]:  # если нет тарелки, то ее нельзя удалить
            print('Операция невозможна, стопки пустые, у Вас ни одной тарелки!')
            return
        result = self.plates[self.count].pop()
        if not self.plates[self.count]:  # соответственно уменьшаем количество стопок, если нужно
            del self.plates[self.count]
            self.count -= 1
            if not self.plates:  # а если у нас снова одна пустая стопка, то возвращаем исходные данные
                self.plates = [[]]
                self.count = 0
        return result

    def get_val(self):
        return self.plates


p = Plates()  # создаем переменную класса Plates
print(p.get_val())  # проверяем, что тарелок нет
# p.minus_plate()  # пробуем убрать тарелку, получаем сообщение 'Операция невозможна, стопки пустые!'
p.plus_plate(1)
p.plus_plate(2)
p.plus_plate(3)
p.plus_plate(4)
p.plus_plate(5)
