def sum_members(n):
    if n <= 0:
        return 0
    el = ((-1) ** (n+1)) * 1 / (2 ** (n-1))
    print('элемент', el)
    return el + sum_members(n-1)


print('Сумма', sum_members(3))
