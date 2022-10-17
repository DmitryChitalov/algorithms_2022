def st(n):
    if n == 0:
        return n
    return n + st(n - 1)

n = int(input('Введите число:'))
print(f'n = {n}, {st(n)} = {n * (n + 1) // 2}')
