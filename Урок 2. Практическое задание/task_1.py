"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


class MyApp:

    def __init__(self):
        self.operand = None
        self.numbers = [0, 0]
        self.stage = 0
        self.continuous = True

    def next(self):
        self.stage += 1

    def reset(self):
        self.stage = 0

    def result(self):
        print('Ваш результат %s' % (self.detect_operand(self.operand)))

    def set_operand(self, operand):
        """ Установить операнд """
        self.operand = operand.strip()

        if self.operand == '0':
            self.continuous = False
            return True

        if self.detect_operand(self.operand) is not None:
            return True

        return False

    def detect_operand(self, operand: str):
        """ Валидация операнда и произвести вычисления """

        # Antipattern 👍
        if operand == '+':
            return self.numbers[0] + self.numbers[1]
        if operand == '-':
            return self.numbers[0] - self.numbers[1]
        if operand == "*":
            return self.numbers[0] * self.numbers[1]
        if operand == '/':
            return self.numbers[0] / self.numbers[1]
        self.operand = None

    def __set_number(self, index, number):
        """ Общий метод установки числа """
        try:
            number = int(number)
            self.numbers[index] = number
            return True
        except BaseException as e:
            return False

    def set_number1(self, number: str):
        return self.__set_number(0, number)

    def set_number2(self, number: str):
        return self.__set_number(1, number)

    @staticmethod
    def wrong_number():
        print('Вы вместо числа ввели строку (((. Исправьтесь')

    @staticmethod
    def wrong_operand():
        print('Вы ввели неверную операцию, попробуйте еще раз...')

    def process(self):
        if self.stage == 0:
            while self.set_operand(input('Введите операцию (+, -, *, / или 0 для выхода):')) is False:
                self.wrong_operand()
            self.next()
        # Запрос первого числа
        elif self.stage == 1:
            while self.set_number1(input('Введите первое число:')) is False:
                self.wrong_number()
            self.next()
        # Запрос второго числа
        elif self.stage == 2:
            while self.set_number2(input('Введите второе число:')) is False:
                self.wrong_number()
            self.result()
            self.reset()

        if self.continuous:
            self.process()


if __name__ == '__main__':
    # while app.continuous:
    MyApp().process()

"""
    Введите операцию (+, -, *, / или 0 для выхода):+
    Введите первое число:2
    Введите второе число:64
    Ваш результат 66
    Введите операцию (+, -, *, / или 0 для выхода):*
    Введите первое число:2
    Введите второе число:2
    Ваш результат 4
    Введите операцию (+, -, *, / или 0 для выхода):0
    
    Process finished with exit code 0
"""