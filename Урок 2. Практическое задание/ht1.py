def calc():
    operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if operation == '0':
        return print('Выход из программы')
    elif operation in '+-*/':
        try:
            number_1 = int(input('Введите первое число: '))
            number_2 = int(input('Введите второе число: '))

            if operation == '+':
                result = number_1 + number_2
                print(f'Ваш результат: {result}')
            elif operation == '-':
                result = number_1 - number_2
                print(f'Ваш результат: {result}')
            elif operation == '*':
                result = number_1 * number_2
                print(f'Ваш результат: {result}')
            elif operation == '/':
                try:
                    result = number_1 / number_2
                except ZeroDivisionError:
                    print('Нельзя делить на ноль!')
                else:
                   print(f'Ваш результат: {result}')
                finally:
                    return calc()

        except ValueError:
            print('Неверный ввод числа!')
            return calc()
    else:
        print('Введен неверный знак операции!')
        return calc()

calc()
