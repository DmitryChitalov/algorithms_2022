"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
import timeit

array = [1, 3, 1, 3, 4, 5, 1]

mycode = """
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
"""

mycode2 = """
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'
"""

mycode3 = """
def func_3():
    dic = {}
    for i in set(array):
        c = 0
        for j in array:
            if i == j:
                c += 1
        dic[i] = c
    key = (max(dic.items(), key=lambda x: x[1]))
    return f'Чаще всего встречается число {key[0]}, ' \
           f'оно появилось в массиве {key[1]} раз(а)'
"""

print(timeit.timeit(setup='', stmt=mycode, number=1000000))
print(timeit.timeit(setup='', stmt=mycode2, number=1000000))
print(timeit.timeit(setup='', stmt=mycode3, number=1000000))

"""
Решения ускорить не получилось. Решения выполняются с небольшой разницей по скорости
0.03972979800164467
0.03905398699862417
0.03974388899951009
"""
