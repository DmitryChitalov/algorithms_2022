"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

!!! Решите через рекурсию.
!!! В задании нельзя применять циклы.
!!! Нужно обойтисть без создания массива
"""

class MyApp:

    def __init__(self):
        self.number = 1
        self.step = 1
        self.total = 0
        self.sum = 0

    def process(self):
        # Can be better with try/except, too lazy
        self.step = int(input('Введите количество элементов:'))

        self.total = self.step
        self.count_num(self.number)
        self.create_step()

    def count_num(self, number):
        print(number)
        self.sum += number

    def create_step(self):
        less = self.number / 2
        self.number -= less
        self.number *= -1
        self.step -= 1
        self.count_num(self.number)
        if self.step > 1:
            self.create_step()
        else:
            self.result()

    def result(self):
        print('Количество элементов - %i, их сумма - %.2f' % (self.total, self.sum))


app = MyApp()
app.process()

"""
    Введите количество элементов:3
    1
    -0.5
    0.25
    Количество элементов - 3, их сумма - 0.75
"""