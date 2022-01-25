def user_input(text: str):
    global num  # пришлось делать глобал т к ретерн не видел переменную
    # за исключениями. Просто, если ввести число в первый раз неправильно (строку
    # вместо числа), то сразу вылезают баги, которые с наскока я лишь таким путем обошел.
    try:
        num = int(input(text))
    except ValueError:
        print('Введено не число, повторите ввод. ')
        user_input(text)
    return num


def check_operation(operation: str):
    if operation not in ('+', '-', '*', '/', '0'):
        operation = input('Введите правильную операцию т. е. +,-, *, /, 0 ')
        check_operation(operation)
    return operation


def calculations(operation):
    operation = check_operation(operation)  # либо вернется самим собой либо заново ввод
    if operation != '0':
        num_1 = user_input('Введите первое число ')
        num_2 = user_input('Введите второе число ')
        if num_2 == 0 and operation == '/':
            num_2 = user_input('Неправильный ввод. Деление на 0. '
                               f'Повторите ввод второго числа. Первое число - {num_1} ')
        if operation == '+':
            print("Итог: %.2f" % (num_1 + num_2))
        elif operation == '-':
            print("Итог: %.2f" % (num_1 - num_2))
        elif operation == '*':
            print("Итог: %.2f" % (num_1 * num_2))
        elif operation == '/':
            print("Итог: %.2f" % (num_1 / num_2))
        return calculations(input('Введите операцию '))


operation_in = input('Введите операцию. Введите 0 для прекращения работы програмы.')
calculations(operation_in)


"""
Ниже закоментировано второе решение, но возможно я не все случаи там протестировал
+ рекурсия реализована без входных параметров, что непрпавильно.
"""

# def user_input():
#     first_num, second_num, operation = 0, 0, 0
#     try:
#         first_num = float(input('Введите первое число'))
#         second_num = float(input('Введите второе число. Учтите, что делить на 0 нельзя.'))
#         operation = input('Введите  операцию. Введите 0 для прекращения работы програмы.')
#     except ValueError:
#         print('Введено не число, повторите ввод.')
#         user_input()
#     if second_num == 0 and operation == '/':
#         print('Неправильный ввод. Деление на 0. Повторите ввод.')
#         user_input()
#     elif operation not in ('+', '-', '*', '/', '0'):
#         print('Неправильный ввод.Введена некорректная операция. Повторите ввод.')
#         user_input()
#     else:
#         return first_num, second_num, operation
#
#
# def calculations():
#     num_1, num_2, operation = user_input()
#     if operation != '0':
#         if operation == '+':
#             print("%.2f" % (num_1 + num_2))
#         elif operation == '-':
#             print("%.2f" % (num_1 - num_2))
#         elif operation == '*':
#             print("%.2f" % (num_1 * num_2))
#         elif operation == '/':
#             print("%.2f" % (num_1 / num_2))
#         return calculations()
#
