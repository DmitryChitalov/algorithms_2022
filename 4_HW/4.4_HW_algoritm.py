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
my_array = [1, 3, 1, 3, 4, 5, 1]


# функция проходит весь массив и у каждого элемента узнает кол-во
# если элемент имеет большее кол-во то он перезаписывает num
# 0.17327330000000002
# достаточно быстро
def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


# функция проходится по массиву и добавляет в новый массив колличество вхождений элемента.
# так как индексы в двух массивах относятся к одному элементу, то ф-я max находит большее число из нового массива
# и по его индексу достает элемент из исходного массива
# 0.2421066
# Работает дольше
def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


# ф-ция при помощи Counter.most_common() превращает массив в отсортированный по кол-ву вхождений элементов массив
# с кортежами, где первый кортеж будет с самым частым елементом и его колличеством
# решение выглядит лаконичнее, но работает дольше всех.
# 0.39139070000000004
def func_3(array):
    return (Counter(array).most_common())[0][0]


# Самый быстрый способ использовать встроенную ф-цию max с ключом по колличеству
# 0.12096170000000006
def func_4(array):
    return max(array, key=array.count)


print(timeit('func_1(my_array)', globals=globals(), number=100000))
print(timeit('func_2(my_array)', globals=globals(), number=100000))
print(timeit('func_3(my_array)', globals=globals(), number=100000))
print(timeit('func_4(my_array)', globals=globals(), number=100000))
