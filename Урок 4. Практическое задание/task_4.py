"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1, 8, 9, 4, 7, 8, 9, 2, 6]


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


def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(array):
    arr_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for i in array:
        arr_count[i] = arr_count[i] + 1
    n = max(arr_count, key=arr_count.get)
    m = arr_count.get(n)
    return f'Чаще всего встречается число {n}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_4(array):
    n = max(array, key=array.count)
    return f'Чаще всего встречается число {n}, ' \
           f'оно появилось в массиве {array.count(n)} раз(а)'


print(func_1(array))
print(timeit("func_1(array)", number=1000000, globals=globals()))
print('--------------------')
print(func_2(array))
print(timeit("func_2(array)", number=1000000, globals=globals()))
print('--------------------')
print(func_3(array))
print(timeit("func_3(array)", number=1000000, globals=globals()))
print('--------------------')
print(func_4(array))
print(timeit("func_4(array)", number=1000000, globals=globals()))

"""
    Все замеры и логика работы на стороне func_1, проводящей все подсчёты
внутри цикла.
    Первоначальная моя попытка "позаигрывать" со словарём (func_3), надеясь
на его упорядоченность и "порядочность", результатов в сторону оптимизации
кода не дала. Проверка показала, что виной этому затраты на работу по
поиску максимального значения среди значений (max(arr_count, key=arr_count.get)).
(ВНЕ РЕШЕНИЯ ДЗ: при некоторых изменениях условия (увеличении заданного списка
и количестве замеров) словарь работает с явным преимуществом... Ответа для 
себя не нашёл.)
    В максимально приближенном к чемпионскому результату работает func_4,
осуществляющая проверку в массиве, используя встроенные возможности Python.
"""
