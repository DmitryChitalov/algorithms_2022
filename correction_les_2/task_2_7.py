"""
Комментарий после проверки:

Валерия, уже урок 4
почему столько ошибок стиля?

    summa
    sum

"""


def sum_row(n):
    if n == 1:
        return 1
    return n + sum_row(n - 1)


def checking(n):
    sum_formula = n * (n + 1) / 2
    return sum_formula == sum_row(n)


number = int(input('Для скольких членов ряда проверить? '))
print(checking(number))
