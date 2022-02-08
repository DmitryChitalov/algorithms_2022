"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для четвертого скрипта
"""


from pympler import asizeof


class CalcNumbers:
    def __init__(self):
        self.inp = CalcNumbers.check_inp()  # проверка до инициализации в переменной экземпляра
        self.x = CalcNumbers.check_val_x()  # проверка до инициализации в переменной экземпляра
        self.y = CalcNumbers.check_val_y()  # проверка до инициализации в переменной экземпляра
        self.result = CalcNumbers.calc(self)  # результат выводится через __str__()

    @staticmethod
    def check_inp():
        inp = input('Введите операцию (+, -, *, / или 0 для выхода): ')
        if inp not in ['+', '-', '*', '/', '0']:
            print('Введено что-то не то...')
            return CalcNumbers.check_inp()  # рекурсивный вызов, если проверка не пройдена
        elif inp == '0':
            return exit(0)
        else:
            return inp

    @staticmethod
    def check_val_x():
        try:
            x = int(input('Введите первое число: '))
        except ValueError:
            print('Вы вместо трехзначного числа ввели строку -(. Исправьтесь')
            return CalcNumbers.check_val_x()  # рекурсивный вызов, если проверка не пройдена
        if x not in range(100, 1000) and x != 0:
            print('Вы ввели не трехзначное число')
            return CalcNumbers.check_val_x()  # рекурсивный вызов, если проверка не пройдена
        else:
            return x

    @staticmethod
    def check_val_y():
        try:
            y = int(input('Введите второе число: '))
        except ValueError:
            print('Вы вместо трехзначного числа ввели строку -(. Исправьтесь')
            return CalcNumbers.check_val_y()  # рекурсивный вызов, если проверка не пройдена
        else:
            return y

    def calc(self):
        if self.inp == '+':
            return self.x + self.y
        elif self.inp == '-':
            return self.x - self.y
        elif self.inp == '*':
            return self.x * self.y
        elif self.inp == '/':
            try:
                return self.x / self.y
            except ZeroDivisionError:
                print('На ноль делить нельзя')
                return CalcNumbers.check_inp()  # рекурсивный вызов, если проверка не пройдена

    def __str__(self):
        return f'Ваш результат: {self.result}'


if __name__ == '__main__':
    calc_1 = CalcNumbers()
    print(asizeof.asizeof(calc_1))


class CalcNumbers2:
    __slots__ = ['inp', 'x', 'y', 'result']

    def __init__(self):
        self.inp = CalcNumbers2.check_inp()  # проверка до инициализации в переменной экземпляра
        self.x = CalcNumbers2.check_val_x()  # проверка до инициализации в переменной экземпляра
        self.y = CalcNumbers2.check_val_y()  # проверка до инициализации в переменной экземпляра
        self.result = CalcNumbers2.calc(self)  # результат выводится через __str__()

    @staticmethod
    def check_inp():
        inp = input('Введите операцию (+, -, *, / или 0 для выхода): ')
        if inp not in ['+', '-', '*', '/', '0']:
            print('Введено что-то не то...')
            return CalcNumbers2.check_inp()  # рекурсивный вызов, если проверка не пройдена
        elif inp == '0':
            return exit(0)
        else:
            return inp

    @staticmethod
    def check_val_x():
        try:
            x = int(input('Введите первое число: '))
        except ValueError:
            print('Вы вместо трехзначного числа ввели строку -(. Исправьтесь')
            return CalcNumbers2.check_val_x()  # рекурсивный вызов, если проверка не пройдена
        if x not in range(100, 1000) and x != 0:
            print('Вы ввели не трехзначное число')
            return CalcNumbers2.check_val_x()  # рекурсивный вызов, если проверка не пройдена
        else:
            return x

    @staticmethod
    def check_val_y():
        try:
            y = int(input('Введите второе число: '))
        except ValueError:
            print('Вы вместо трехзначного числа ввели строку -(. Исправьтесь')
            return CalcNumbers2.check_val_y()  # рекурсивный вызов, если проверка не пройдена
        else:
            return y

    def calc(self):
        if self.inp == '+':
            return self.x + self.y
        elif self.inp == '-':
            return self.x - self.y
        elif self.inp == '*':
            return self.x * self.y
        elif self.inp == '/':
            try:
                return self.x / self.y
            except ZeroDivisionError:
                print('На ноль делить нельзя')
                return CalcNumbers2.check_inp()  # рекурсивный вызов, если проверка не пройдена

    def __str__(self):
        return f'Ваш результат: {self.result}'


if __name__ == '__main__':
    calc_2 = CalcNumbers2()
    print(asizeof.asizeof(calc_2))

#  Урок 2, задание 1.
#  Использован объект объект __slots__ для аргументов класса.
#  Результат: 528 против 216 в пользу слота.
