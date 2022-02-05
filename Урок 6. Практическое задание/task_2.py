"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение.
"""

from random import randint
from memory_profiler import profile


@profile
def make_list():
    # Cписком
    result = [elem for idx, elem in enumerate(src) if elem > src[idx-1] and idx > 0]
    print(result)


@profile
def make_generator():
    # Оптимизация по памяти, генератором
    result = (elem for idx, elem in enumerate(src) if elem > src[idx-1] and idx > 0)
    print(result)


if __name__ == "__main__":
    src = [randint(0, 100000) for i in range(1000000)]

    make_list()
    make_generator()

"""
Оптимизация используя генератор. 
попытаемся получить результат по памяти...
В первом варианте lc, во втором генератор
До:    62.2 MiB      0.0 MiB           1       print(result)
После: 58.4 MiB      0.0 MiB           1       print(result)
    
"""
