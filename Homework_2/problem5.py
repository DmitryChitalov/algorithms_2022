def rec(n):
    if n == 127:
        return f'{n} - {chr(n)}'
    elif n % 10 == 1:
        print(f'{n} - {chr(n)}')
        return rec(n + 1)
    else:
        print(f'{n} - {chr(n)}', end=' ')
        return rec(n + 1)

print(rec(32))