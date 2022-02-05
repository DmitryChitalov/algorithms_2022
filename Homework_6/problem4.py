from memory_profiler import profile

# Рекурсия из задания #7 урока №2

@profile
def omg(a):
    def rec(f):
        if f == 1:
            return 1
        return f + rec(f - 1)
    return rec(a)

# Заменили решением без рекурсии

@profile
def summa(n):
    t = 0
    while n > 0:
        t += n
        n -= 1
    return t

print(omg(99))
print(summa(99))