def calc():
    res = input("Введите операцию (+, -, *, / или 0 для выхода): ")
    if res not in ('+', '-', '*', '/', '0'):
        return print("Неизвестная операция"), calc()
    elif res == '0':
        return print("Вы вышли из калькулятора")
    else:
        num_1 = input('Введите первое число: ')
        num_2 = input('Введите второе число: ')
        if num_1.isdigit() and num_2.isdigit():
            num_1 = int(num_1)
            num_2 = int(num_2)
            if res == '+':
                return print(f'Ваш результат {num_1 + num_2}'), calc()
            elif res == '-':
                return print(f'Ваш результат {num_1 - num_2}'), calc()
            elif res == '*':
                return print(f'Ваш результат {num_1 * num_2}'), calc()
            elif res == '/' and num_2 != 0:
                return print(f'Ваш результат {num_1 / num_2}'), calc()
            else:
                return print("На 0 делить нельзя"), calc()
        else:
            return print("Ошибка: Введите число!"), calc()


print(calc())
