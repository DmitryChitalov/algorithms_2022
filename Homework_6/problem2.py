from memory_profiler import profile

# Рекурсия из задания #2 урока №2

@profile
def rec(f, k=0, a=0, b=0):
    if 10 ** k > f:
        return a, b
    m = int((f % (10 ** (k + 1)) - f % (10 ** k)) / (10 ** k))
    if m % 2 == 0:
        return rec(f, k + 1, a + 1, b)
    if m % 2 != 0:
        return rec(f, k + 1, a, b + 1)

# Заменили решением без рекурсии

@profile
def quantity(f):
    a = ''.join(['1' if int(x) % 2 == 0 else '0' for x in str(f)]).split()
    print(a[0].count('1'), a[0].count('0'), sep=', ')

quantity(2345)
print(*rec(2345), sep=', ')
