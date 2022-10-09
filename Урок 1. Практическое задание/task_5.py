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


class StackOfPlates:
    def __init__(self, max_plate_count):
        self.max_size = max_plate_count
        self.piles = []
        self.piles_count = 0
        self.plates_count = 0

    def __str__(self):
        return str(self.piles)

    def is_empty(self):
        return self.piles_count == 0

    def push(self, plate):
        if self.piles_count == 0 or (self.plates_count % self.max_size) == 0:
            self.piles.append([plate])
            self.piles_count += 1
            self.plates_count += 1
        else:
            self.piles[self.piles_count - 1].append(plate)
            self.plates_count += 1

    def pop(self):
        result = None
        if self.piles_count > 0:
            result = self.piles[self.piles_count - 1].pop()
            self.plates_count -= 1
            if (self.plates_count % self.max_size) == 0:
                self.piles.pop()
                self.piles_count -= 1
        return result

    def get_piles_count(self):
        return self.piles_count

    def get_plates_count(self):
        return self.plates_count


if __name__ == '__main__':
    my_plate_stack = StackOfPlates(3)
    for i in range(1, 11):
        my_plate_stack.push('Т' + str(i))

    print(my_plate_stack)
    for i in range(9):
        print(f'Убрали {my_plate_stack.pop()}: '
              f'{my_plate_stack.get_piles_count()}, {my_plate_stack.get_plates_count()}')
        if i % 2 == 0:
            new_plate = "Тd" + str(i)
            my_plate_stack.push(new_plate)
            print(
                f'Добавили {new_plate}: '
                f'{my_plate_stack.get_piles_count()}, {my_plate_stack.get_plates_count()}')
    print(my_plate_stack)
