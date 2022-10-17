"""
Курс Основы Python, урок 5. Задание 5:
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном
списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
"""
from memory_profiler import memory_usage


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


@memory
def uniq_numb(src):
    uni_numb = set()
    tmp = set()
    for el in src:
        if el not in tmp:
            uni_numb.add(el)
        else:
            uni_numb.discard(el)
        tmp.add(el)
    unique_numbers_ord = [el for el in src if el in uni_numb]
    return unique_numbers_ord


print(uniq_numb(src))
# Выполнение заняло 0.00390625 Mib


@memory
def opti_uniq_numb(src):
    uni_numb = set()
    tmp = set()
    for el in src:
        if el not in tmp:
            uni_numb.add(el)
        else:
            uni_numb.discard(el)
        tmp.add(el)
    unique_numbers_ord = [el for el in src if el in uni_numb]
    del uni_numb
    del tmp
    return unique_numbers_ord


print(opti_uniq_numb(src))
# Выполнение заняло 0.0 Mib

"""Оптимизация затрат памяти выполнена за счёт удаления ставших ненужными объектов. После их удаления
высвобождается небольшой объем памяти"""
