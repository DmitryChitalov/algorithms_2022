"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

"""
ВЫВОДЫ:
Оба предлагаемых решения имеют сложность О(n^2). Даже при увеличении количества элементов с 7 до 14,
и переписав на линейную сложность мы получаем выигрыш в производительности.

Вариант 3, это вариант 2, с проверкой уже постчитанных результатов, будет хорошо работать если в массиве много 
повторяющихся значений

Предлагаемый вариант решения 4, самый быстрый, по причинам описанным выше, плюс оно стабильно, не зависит от содержания 
массива

Вариант 5 одной строкой, правда на мой взгляд как-то громоздко получилось   
 
"""

from timeit import timeit


array = [1, 3, 1, 3, 4, 5, 1]
array = [1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1]
array = [1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    new_array = []
    dct = {}
    for el in array:
        if el in dct:
            continue
        count2 = array.count(el)
        new_array.append(count2)
        dct[el] = el

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

def func_4():
    m, num = 0, 0
    dct = {}
    for i in array:
        dct.setdefault(i, 0)
        cur_dict_i = dct[i] + 1
        dct[i] = cur_dict_i
        if cur_dict_i > m:
            m, num = cur_dict_i, i

    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_5():
    tmp = next(iter(sorted({array.count(i): i for i in array}.items(), reverse=True)))
    return f'Чаще всего встречается число {tmp[1]}, ' \
           f'оно появилось в массиве {tmp[0]} раз(а)'


if __name__ == '__main__':
    print(f'Вариант 1: {timeit("func_1()", number=100000, globals=globals())}')
    print(f'Вариант 2: {timeit("func_2()", number=100000, globals=globals())}')
    print(f'Вариант 3: {timeit("func_3()", number=100000, globals=globals())}')
    print(f'Вариант 4: {timeit("func_4()", number=100000, globals=globals())}')
    print(f'Вариант 5: {timeit("func_5()", number=100000, globals=globals())}')

    print(f'Результат {" " if func_1() == func_2() == func_3() == func_4()  == func_5() else "не "}корректен')
