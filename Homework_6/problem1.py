from memory_profiler import profile

# Рекурсия из задания #2 урока №4

@profile
def wrap(n):
    def was(number):
        if number == 0:
            return ''
        return f'{str(number % 10)}{was(number // 10)}'
    return was(n)

# Заменили решением без рекурсии

@profile
def now(number):
    return print(*''.join([str(number)[(len(str(number)) - 1 - str(number).index(x))] for x in str(number)]).split())

@profile
def func(n):
    r = 0
    while n > 0:
        a = n % 10
        r = (r * 10) + a
        n //= 10
    return r

print(wrap(5432))
now(5432)
print(func(5432))