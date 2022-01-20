n = int(input())


def rec(f):
    k = -0.5
    if f == 1:
        return 1
    return k ** (f - 1) + rec(f - 1)

print(rec(n))
for i in range(n):
    print((-0.5) ** i, end=' ')