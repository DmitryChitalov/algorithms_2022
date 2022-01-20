n = int(input())


def rec(f, k):
    if 10 ** k > f:
        return ''
    return f'{int((f % (10 ** (k + 1)) - f % (10 ** k)) / (10 ** k))}' + rec(f, k + 1)

print(rec(n, 0))
