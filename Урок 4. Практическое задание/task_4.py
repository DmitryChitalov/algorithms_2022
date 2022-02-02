"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from collections import Counter
import timeit

array = [1, 3, 1, 3, 4, 5, 1]


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
    cnt = Counter(array).most_common(1)
    return f'Чаще всего встречается число {cnt[0][0]}, ' \
           f'оно появилось в массиве {cnt[0][1]} раз(а)'


def func_4():
    max_elem = max(array, key=lambda x: array.count(x))
    return f'Чаще всего встречается число {max_elem}, ' \
           f'оно появилось в массиве {array.count(max_elem)} раз(а)'


if __name__ == '__main__':
    # print(func_1())
    # print(func_2())
    # print(func_3())
    # print(func_4())

    t = timeit.Timer(lambda: func_1())
    print(t.repeat(3))
    t = timeit.Timer(lambda: func_2())
    print(t.repeat(3))
    t = timeit.Timer(lambda: func_3())
    print(t.repeat(3))
    t = timeit.Timer(lambda: func_4())
    print(t.repeat(3))

# импорты модулей переместил вверх кода (были после инструкции if __name__ == '__main__')

# после варианта с Counter из Collections добавил четвертый вариант с использованием функции max
# Мои результаты:
# [1.0169228000000001, 1.0075225999999997, 1.006519] с простым перебором в цикле
# [1.3748741999999998, 1.3746597999999999, 1.3733064000000006] с создание нового массива
# [2.4472626, 2.4335015999999996, 2.4390339] c Counter и функцией most_common (если использовать max вместо most_common
# то выполнение происходит быстрее, чуть больше по времени уровня варианта 5
# [1.5479435000000006, 1.5473247000000008, 1.5452632000000008] с функцией max
