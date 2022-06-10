"""Генерация целых чисел"""

from timeit import default_timer, timeit


def time_it(func):
    def wrapper(numb):
        start_time = default_timer()
        func(numb)
        # правая отсечка времени и результат
        print(default_timer() - start_time)
        # логгирование
        # и любые другие действия
    return wrapper


@time_it
def gen_prime(x):
    multiples = []
    results = []
    for i in range(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in range(i*i, x+1, i):
                multiples.append(j)

    return results


gen_prime(3000)

print(timeit("gen_prime(3000)", "from __main__ import gen_prime", number=1))

"""
# левая отсечка времени
start_time = default_timer()
# запуск функции
gen_prime(3000)
# правая отсечка времени и результат
print(default_timer() - start_time)

# сравним с привычным вариантом замеров
print(timeit("gen_prime(3000)", "from __main__ import gen_prime", number=1))


0.0578244
0.05766979999999999

Существенных расхождений не выявлено
"""
