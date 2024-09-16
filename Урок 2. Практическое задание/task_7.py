"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!

Решите через рекурсию. В задании нельзя применять циклы.
"""


class MyApp:

    def __init__(self):
        self.n = 0
        self.c = 1
        self.left = 0

    def count_left(self):
        self.left += self.c
        if self.c < self.n:
            self.c += 1
            self.count_left()

    def count_right(self):
        return self.n * (self.n + 1)/2

    def start(self):
        try:
            self.n = int(input('Введите натуральное число N: '))
            self.count_left()
            if self.left == self.count_right():
                print('Равенство выполняется (%i == %i)' % (self.left, self.count_right()))
        except BaseException as e:
            # maximum recursion depth exceeded in comparison
            # print(str(e))
            self.start()


app = MyApp()
app.start()
