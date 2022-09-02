from memory_profiler import memory_usage
# посчитать четные и нечетные числа


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff
    return wrapper


@decor
def count_numb(n, even=0, odd=0):
    if n == 0:
        return (f"Количество четных цифр в числе: {even}, нечетных цифр: {odd}")
    else:
        number = n % 10
        n = n // 10
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        return count_numb(n, even, odd)


@decor
def count_numb_opt(n, even=0, odd=0):
    while n > 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
        n = n // 10
    return (f"Количество четных цифр в числе: {even}, нечетных цифр: {odd}")


n = 123456789123456789986589955694698450000000000000000000000000000777776459875

print(count_numb(n))
print(count_numb_opt(n))

# цикл занимат меньше места, чем рекурсия
