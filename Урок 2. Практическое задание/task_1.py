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

Решите через рекурсию. Решение через цикл не принимается.

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

class Calculator:
    STOP_CALC = '0'
    
    @classmethod
    def get_number(cls, mess):
        try:
            num = int(input(mess))
            return num
        except ValueError:
            print('You enter wrong number')
            return cls.get_number(mess)
  
    @classmethod
    def get_operation(cls, mess):
        allowed_operations = set()
        allowed_operations.add('+')
        allowed_operations.add('-')
        allowed_operations.add('*')
        allowed_operations.add('/')
        allowed_operations.add(cls.STOP_CALC)

        def recursion_get_operation():
            operation = input(mess)
            if operation in allowed_operations:
                return operation
            else:
                print('You enter wrong operation')
                return recursion_get_operation()
        return recursion_get_operation()

    @classmethod
    def run(cls):
        operation = cls.get_operation('Enter operation (+, -, *, / or 0 for exit): ')

        if operation == cls.STOP_CALC:
            return
        num1 = cls.get_number('Enter first number: ')
        num2 = cls.get_number('Enter second number: ')

        expression = f'{num1} {operation} {num2}'
        result = eval(expression)
        print(f'{expression} = {result}')
        cls.run()

Calculator.run()




