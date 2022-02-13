import os
def calculator():
    user_sign = input("Введите знак: ")

    try:
        user_1 = float(input("Первое число: "))
        user_2 = float(input("Второе число: "))
    except:
        print("Вместо числа вы ввели что то другое... :( \n Попробуйте еще раз.")
        return calculator()

    if user_sign in "+-*/0":
        if user_sign == "0": # ВЫХОД
            return "Выход"
        elif user_sign == "+": # +
            print(user_1 + user_2)
            os.system("cls")
            return calculator()

        elif user_sign == "-": # -
            print(user_1 - user_2)
            os.system("cls")
            return calculator()

        elif user_sign == "*": # *
            print(user_1 * user_2)
            os.system("cls")
            return calculator()

        elif user_sign == "/": # /
            print(user_1 / user_2)
            os.system("cls")
            return calculator()
    else:
        print("Вы ввели некоректный знак!")
        return calculator()

print(calculator())