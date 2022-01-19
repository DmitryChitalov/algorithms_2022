from random import randint


def rec(k, a):
    if a == 0:
        return print(f'Не угадали\nЧисло было равно {k}')
    n = int(input())
    if n > k:
        print(f'Число меньше\nосталось{a}попыток')
        return rec(k, a - 1)
    if n < k:
        print(f'Число больше\nосталось{a}попыток')
        return rec(k, a - 1)
    if n == k:
        return print('Вы выиграли')

rec(randint(0, 10000), 10)