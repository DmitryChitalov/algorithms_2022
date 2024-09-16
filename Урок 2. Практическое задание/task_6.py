"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


class MyApp:

    def __init__(self):
        self.random = random.randint(0, 100)
        self.wrong = 0

    def start(self):
        print('Вы должны отгадать число (от 0-100) не более чем за 10 попыток. Удачи!')
        self.try_catch()

    def try_catch(self):
        if self.wrong >= 10:
            self.exit()
            return

        try:
            self.check_number(int(input('Введите число: ')))
        except BaseException:
            self.try_catch()

    def exit(self):
        print('Игра окончена. Попытки исчерпаны. Это число %i' % self.random)

    def wrong_try(self, number):
        high = self.random > number
        if high:
            print("Неудачная попытка. (%i/10). Число больше." % self.wrong)
        else:
            print("Неудачная попытка. (%i/10). Число меньше." % self.wrong)
        self.try_catch()

    def check_number(self, number):
        if self.random != number:
            self.wrong += 1
            self.wrong_try(number)
        else:
            print('Да! Вы правильно угадали число. Это %i.' % self.random)


app = MyApp()
app.start()


"""
    Вы должны отгадать число (от 0-100) не более чем за 10 попыток. Удачи!
    Введите число: 50
    Неудачная попытка. (1/10). Число больше.
    Введите число: 70
    Неудачная попытка. (2/10). Число меньше.
    Введите число: 60
    Да! Вы правильно угадали число. Это 60.
"""