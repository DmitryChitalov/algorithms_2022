def calc():
    operation = input("Введите операцию: +, -, *, / или 0 для выхода: ")

    if operation == '0':
        return "Выход"

    else:
        if operation in "+-*/":
            try:
                n_1 = int(input("введите первое число: "))
                n_2 = int(input("введите второе число: "))

                if operation == '+':
                    res = n_1 + n_2
                    print(f"ваш результат {res}")
                    return calc()

                elif operation == '-':
                    res = n_1 - n_2
                    print(f"ваш результат {res}")
                    return calc()

                elif operation == '*':
                    res = n_1 * n_2
                    print(f"ваш результат {res}")
                    return calc()

                elif operation == '/':
                    try:
                        res = n_1 / n_2
                    except ZeroDivisionError:
                        print("Деление на 0 невозможно")
                    else:
                        print(f"ваш результат {res}")
                    finally:
                        return calc()

            except ValueError:
                print("Вместо числа вы ввели строку. Исправьте")
                return calc()

        else:
            print("Вы ввели неправильный оператор")
            return calc()


calc()
