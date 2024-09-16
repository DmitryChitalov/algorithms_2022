"""Изменение значений переменных"""


def recursion(a, b):
    """Рекурсия"""
    # базовый случай
    # последний шаг рекурсии
    if a == b:
        return str(a)
    # шаг рекурсии
    # рекурсивное условие
    elif a > b:
        return f'{a} {recursion(a - 1, b)}'
    # шаг рекурсии
    # рекурсивное условие
    elif a < b:
        return f'{str(a)} {recursion(a + 1, b)}'


print(recursion(20, 15))
print(recursion(10, 15))
