def rec(a1, a2, string):
    a1 = int(input('Введите первое число: '))
    a2 = int(input('Введите второе число: '))
    string = input('Введите операцию: ')
    try:
        if string == '0':
            return print('Calculator exited')
        if string == '+':
            print(a1 + a2)
            return rec(a1, a2, string)
        elif string == '-':
            print(a1 - a2)
            return rec(a1, a2, string)
        elif string == '/':
            print(a1 / a2)
            if a2 == 0:
                raise ZeroDivisionError
            return rec(a1, a2, string)
        elif string == '*':
            print(a1 * a2)
            return rec(a1, a2, string)
        elif string == '-':
            print(a1 - a2)
            return rec(a1, a2, string)
        else:
            raise ValueError
    except ZeroDivisionError:
        print("На ноль делить нельзя")
        return rec(a1, a2, string)
    except ValueError:
        print("Неверная операция")
        return rec(a1, a2, string)
rec(0, 0, '')