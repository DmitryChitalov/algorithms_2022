"""
Вычисление суммы первых n целых чисел
"""


def get_sum_1(n):
    """
    В основе идеи алгоритма - переменная-счетчик, инициализируемая нулем
    и к которой в процессе решения задачи прибавляются числа,
    перебираемые в цикле
    :param n:
    :return:
    """
    res = 0
    for i in range(1, n + 1):
        res = res + i

    return res


print(get_sum_1(10))


def get_sum_2(obj):
    """
    Текущее решение является неудачным из-за избыточного присваивания,
    а также неудачного выбора имен переменных
    :param obj:
    :return:
    """
    var = 0
    for part in range(1, obj + 1):
        dec = part
        var = var + dec
    return var


print(get_sum_2(10))
