from collections import Counter
from timeit import timeit

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
    cnt = {k: v for k, v in Counter(array).most_common(1)}
    max_num = int(*cnt.keys())
    count = int(*cnt.values())

    return f'Чаще всего встречается число {max_num}, ' \
           f'оно появилось в массиве {count} раз(а)'


def func_4():
    max_num = max(num for num in array if array.count(num) == max(map(array.count, array)))
    count = max(map(array.count, array))
    return f'Чаще всего встречается число {max_num}, ' \
           f'оно появилось в массиве {count} раз(а)'


print(f'Функция №1 c циклом')
print(timeit("func_1", "from __main__ import func_1", number=100000))

print(f'Функция №2 с циклом и append')
print(timeit("func_2", "from __main__ import func_2", number=100000))

print(f'Функция №3 c dict comprehension и counter')
print(timeit("func_3", "from __main__ import func_3", number=100000))

print(f'Функция №4 c map и max')
print(timeit("func_4", "from __main__ import func_4", number=100000))

#
# print(func_4())
# print(func_3())
# print(func_1())
# print(func_2())

# Аналитика показала, что функция с использованием max и map выполняется быстрее остальных
