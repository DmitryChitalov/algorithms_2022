def math_op2():
    try:
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))

        u_input = input('Введите математический знак: ')

    except ValueError:
        print('Вы ввели строку. Введите пожалуйста число: ')
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        u_input = input('Введите математический знак: ')

    if u_input == 0:
        return
    elif u_input == '+':
        result = num1 + num2
        print(result)
        return math_op2()
    elif u_input == '-':
        result = num1 - num2
        print(result)
        return math_op2()
    elif u_input == '*':
        result = num1 * num2
        print(result)
        return math_op2()
    elif u_input == '/':
        try:
            result = num1 // num2
            print(result)
            return math_op2()
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
            return math_op2()


print(math_op2())
