def calc(x):
    if x == 0:
        return " "

    else:
        return f'{x % 10}{calc(x // 10)}'


print(calc(784520))
