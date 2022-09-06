"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

from timeit import timeit
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 3, 9, 6, 1]


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


# С помощью класса Counter() модуля collections
def func_3():
    return f'Самое часто встречающееся число и количество раз его появления: {Counter(array).most_common(1)[0]}'


# Через функцию max.
def func_4():
    number = max(array, key=array.count)
    quantity = array.count(number)
    return f'Чаще всего встречается число {number}, оно появилось в массиве {quantity} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(timeit("func_1()", "from __main__ import func_1", number=1000))
print(timeit("func_2()", "from __main__ import func_2", number=1000))
print(timeit("func_3()", "from __main__ import func_3", number=1000))
print(timeit("func_4()", "from __main__ import func_4", number=1000))

"""
Время исполнения функции func_1 - 0.0027018000109819695
Время исполнения функции func_2 - 0.0037096000014571473
Время исполнения функции func_3 - 0.007532899995567277
Время исполнения функции func_4 - 0.002664800005732104

Лучшие результаты показывает первая и четвертая функции. Вторая функция на втором месте. Все они использую функцию 
.count, но во второй функции также используется метод .append, который дополнительно формирует список. 
Самая медленная третья, она реализованна c помощью класса Counter модуля collections. Скорее всего из-за того 
что Counter использует протокол итерации Python и каждый символ должен быть приобразован в обьект Python.
"""
