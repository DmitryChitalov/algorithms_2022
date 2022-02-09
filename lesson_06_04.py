from memory_profiler import memory_usage
# Алгоритмы, 2 урок
"""
Заменила рекурсию на цикл, что снизило потребление памяти с 0.23828125 Mib до  0.01953125 Mib
"""


def profile_function(func):
    def wrapper(*args, **kwargs):
        start_memory = memory_usage()
        result_function = func(*args, **kwargs)
        end_memory = memory_usage()
        result_memory = end_memory[0] - start_memory[0]
        return result_function, result_memory
    return wrapper


@profile_function
def nums_count(number, even_count=0, odd_count=0):
    if number == 0:
        return print(f'Количество четных чисел равно: {even_count}, нечетных: {odd_count}')
    else:
        if (number % 10) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        nums_count(number // 10, even_count, odd_count)


result_function, result_memory = nums_count(12345678901234575734762476234561356235624562457426713789713801309491094794161471457134)
print(f'Memory: {result_memory}') # --> 0.23828125


@profile_function
def nums_count_2(number, even_count=0, odd_count=0):
    while number != 0:
        if (number % 10) % 2 == 0:
            even_count += 1
            number //= 10
        else:
            odd_count += 1
            number //= 10

    return print(f'Количество четных чисел равно: {even_count}, нечетных: {odd_count}')


result_function, result_memory = nums_count_2(12345678901234575734762476234561356235624562457426713789713801309491094794161471457134)
print(f'Memory: {result_memory} Mib') # --> 0.01953125

