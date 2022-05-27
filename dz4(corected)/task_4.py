"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
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
    num = max(array, key=lambda x: array.count(x))
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'


print(func_1())
print(fr"Замер func_1: {timeit('func_1', globals=globals(), number=1000)}")

print(func_2())
print(fr"Замер func_2: {timeit('func_2', globals=globals(), number=100)}")

print(func_3())
print(fr"Замер func_3: {timeit('func_3', globals=globals(), number=1000)}")


"""
В функции fun_1 замер времени показал средний результат, это линейная сложность.
В функции func_2 замер времени показал самый медленный результат, так как у нее квадратичная сложность,
она потребляет больше ресурсов.
Самая быстрая функция func_3, так как в этой функции используется встроенная функци max(), 
с параметром поиска максимального значения count(). Встроеные функции работают быстрее циклов.
"""