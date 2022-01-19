n = int(input())


def rec(f):
    if f == 1:
        return 1
    return f + rec(f - 1)

print(int(n * (n+1)/2))
print(rec(n))
