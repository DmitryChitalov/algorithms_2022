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
p.minus_plate()  # пробуем убрать тарелку, получаем сообщение 'Операция невозможна, стопки пустые!'
p.plus_plate(1)
p.plus_plate(2)
p.plus_plate(3)
p.plus_plate(4)
p.plus_plate(5)
p.plus_plate(6)
p.plus_plate(7)
p.plus_plate(8)
p.plus_plate(9)
p.plus_plate(10)
print(p.get_val())  # добавляем 10 тарелок и проверяем, что получилось
p.minus_plate()
print(p.get_val())  # удаляем одну тарелку и проверяем
p.minus_plate()
p.minus_plate()
p.minus_plate()
p.minus_plate()
p.minus_plate()
p.minus_plate()
p.minus_plate()
p.minus_plate()
p.minus_plate()
print(p.get_val())  # удаляем остальные тарелки и проверяем
p.minus_plate()  # снова проверка на удаление пустой стопки
p.plus_plate(1)
p.plus_plate(2)
p.plus_plate(3)
p.plus_plate(4)
p.plus_plate(5)
p.plus_plate(6)
p.plus_plate(7)
p.plus_plate(8)
p.plus_plate(9)
print(p.get_val())
