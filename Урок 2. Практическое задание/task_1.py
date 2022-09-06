def calc():
    operation = input("Введите операцию (+, -, *, / или 0 для выхода): ")

    if operation == '0':
        return "Выход"

    else:
        if operation in "+-*/":
            try:
                num_1 = int(input("Введите первое число: "))
                num_2 = int(input("Введите второе число: "))

                if operation == "+":
                    sum1 = num_1 + num_2
                    print(f'Результат суммы: {sum1}')
                    return calc()

                if operation == "-":
                    difference = num_1 - num_2
                    print(f'Резуальтат разности: {difference}')
                    return calc()

                if operation == "*":
                    multiply = num_1 * num_2
                    print(f'Результат произведения: {multiply}')
                    return calc()

                if operation == "/":
                    try:
                        division = num_1 / num_2
                    except ZeroDivisionError:
                        print("Деление на 0 невозможно")
                    else:
                        print(f'Результат деления: {division}')
                    finally:
                        return calc()
            except ValueError:
                print("Вы вместо трехзначного числа ввели строку. Исправьтесь")
                return calc()

        else:
            print("Введен неверный символ, попробуйте еще раз")
            return calc()

calc()
