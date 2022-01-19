n = int(input())
param1 = 0
param2 = 0
param3 = 0

def rec(f, k, a, b):
    if 10 ** k > f:
        return a, b
    m = int((f % (10 ** (k + 1)) - f % (10 ** k)) / (10 ** k))
    if m % 2 == 0:
        return rec(f, k + 1, a + 1, b)
    if m % 2 != 0:
        return rec(f, k + 1, a, b + 1)

print(rec(n, param1, param2, param3))