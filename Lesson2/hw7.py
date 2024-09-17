def my_func(n):
    if n == 0:

        return n
    else:
        return n + my_func(n - 1)


def my_func2(n):
    return int(n * (n + 1) / 2)


def check(n):
    if my_func(n) == my_func2(n):
        return f'{my_func(n)}={my_func2(n)}'
    else:
        return False


print(check(10))
