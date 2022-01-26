"""Сравним цикл и рекурсию"""


def get_sum_1(lst_obj):
    """Простой цикл"""

    res = 0
    for el in lst_obj:
        res = res + el
    return res


def get_sum_2(lst_obj):
    """Простая рекурсия"""
    # базовый случай
    if len(lst_obj) == 1:
        return lst_obj[0]
    else:
        # шаг рекурсии
        return lst_obj[0] + get_sum_2(lst_obj[1:])


print(get_sum_1([1, 3, 5, 7, 9]))
print(get_sum_2([1, 3, 5, 7, 9]))


# get_sum([1, 3, 5, 7, 9])
# 1 + get_sum([3, 5, 7, 9])
# 3 + get_sum([5, 7, 9])
# 5 + get_sum([7, 9])
# 7 + get_sum([9])
# get_sum(9) = 9 - длина равна 1 -> завершаем рекурсивные вызовы
# и начинаем возвраты
# 9
# 7 + 9
# 5 + 16
# 3 + 21
# 1 + 24
# и получаем 25 и выполняем возврат в главную ветку программы
