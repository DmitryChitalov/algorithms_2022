def calc():
    sign = input('Введите знак операции: ')

    if sign == '0':
        print('Пока-пока')
    else:
        try:
            num_1 = int(input('Введите первое число: '))
            num_2 = int(input('Введите второе число: '))
            if sign == '+':
                print(num_1 + num_2)
                return calc()
            elif sign == '-':
                print(num_1 - num_2)
                return calc()
            elif sign == '*':
                print(num_1 * num_2)
                return calc()
            elif sign == '/':
                try:
                    print(num_1 / num_2)
                except ZeroDivisionError:
                    print('Деление на ноль')
                finally:
                    return calc()
            else:
                print('Вы ввели неверный знак')
                return calc()
        except ValueError:
            print('Вы ввели строку вместо числа')
            return calc()


calc()
