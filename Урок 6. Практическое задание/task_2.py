"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import memory_usage


def memory_info(func):
    def wrapper():
        m1 = memory_usage()
        result = func()
        m2 = memory_usage()
        memory_diff = m2[0] - m1[0]
        return result, memory_diff
    return wrapper


@memory_info
def recur_mem():
    def recur_method(numb=int(''.join([str(el) for el in range(350)])), even=0, odd=0):
        if numb == 0:
            return even, odd
        else:
            cur_n = numb % 10
            numb = numb // 10
            if cur_n % 2 == 0:
                even += 1
            else:
                odd += 1
            return recur_method(numb, even, odd)
    return recur_method()


res, mem_diff = recur_mem()
print(mem_diff)


"""
Проблема заключается в том, что декоратор срабатывает каждый раз при рекурсивном шаге,
чтобы этого избежать можно обернуть рекурсивную функцию другой функцией, 
таким образом декортаор отработает верно.

Результат: 1.464 Mib
"""
