"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import random
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1(array: list) -> str:
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2(array: list) -> str:
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(arr: list) -> str:
    """ 3 Вариант функции """
    number = max(arr, key=lambda x: arr.count(x))
    return "число %s встречается в массиве %s раз(а)" % (number, arr.count(number))


for func in (func_1, func_2, func_3):
    print(f'{func.__name__}: {timeit("func(array)", globals=globals())}')
    #print(f"Result: {func(array)}")


""" 
результаты на малом массиве: [1, 3, 1, 3, 4, 5, 1] 

func_1: 1.3579489
func_2: 1.9960303
func_3: 2.1639953000000003

Судя по замерам, func_1 выполнает задачу быстрее, однако func_3 более лаконична и решается в одну строку,
Так же стоит заметить что с ростом колличества елементов в массиве скорость func_3 более оптимизирована для этой задачи

протестирована на timeit("func(array)", globals=globals(), number=1000)
array = random.sample(range(1000, 10000), 1000)

результаты замеров:
func_1: 14.370042600000001
func_2: 14.2398977
func_3: 14.223591699999997

"""


