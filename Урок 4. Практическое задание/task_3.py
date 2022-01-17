"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""

from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


enter_num = 1234
print(f'Времени понадобилось', timeit("revers(enter_num)", globals=globals()))
"Времени понадобилось 1.5990194. Та же рекурсия, которая выполняется очень долго и плохо выглядит"


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


enter_num = 12345
print(f'Времени понадобилось', timeit("revers_2(enter_num)", globals=globals()))
"Времени понадобилось 1.1367178000000002. Срезы выполняются O(n), но чуть быстрее рекурсии "


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


enter_num = '1234567'
print(f'Времени понадобилось', timeit("revers_3(enter_num)", globals=globals()))
"Времени понадобилось 0.42920440000000015. " \
"Обращение по индексу имеет сложность О(1) и решает проблему, если ввод = строка"


def revers_4(enter_num):
    list1.append([*enter_num])
    return ''.join(map(str, list1[0][::-1]))


list1 = []
enter_num = '12345'
revers_4(enter_num)
print(f'Времени понадобилось', timeit("revers_4(enter_num)", globals=globals()))
"Времени понадобилось 1.8895922. Распаковка *args выполняется, как итератор О(n). Здесь  Очень долгий код, худущий вариант"


enter_num = '1234567'
print(f'Времени понадобилось', timeit("revers_3(enter_num)", globals=globals()))
"Времени понадобилось 0.42920440000000015. " \
"Обращение по индексу имеет сложность О(1) и решает проблему, если ввод = строка"


def revers_4(enter_num):
    list1.append([*enter_num])
    return ''.join(map(str, list1[0][::-1]))


list1 = []
enter_num = '12345'
revers_4(enter_num)
print(f'Времени понадобилось', timeit("revers_4(enter_num)", globals=globals()))
"Времени понадобилось 1.8895922. Распаковка *args выполняется, как итератор О(n). Здесь  Очень долгий код, худущий вариант"


enter_num = '1234567'
print(f'Времени понадобилось', timeit("revers_3(enter_num)", globals=globals()))
"Времени понадобилось 0.42920440000000015. " \
"Обращение по индексу имеет сложность О(1) и решает проблему, если ввод = строка"


def revers_4(enter_num):
    list1.append([*enter_num])
    return ''.join(map(str, list1[0][::-1]))


list1 = []
enter_num = '12345'
revers_4(enter_num)
print(f'Времени понадобилось', timeit("revers_4(enter_num)", globals=globals()))
"Времени понадобилось 1.8895922. Распаковка *args выполняется, как итератор О(n). Здесь  Очень долгий код, худущий вариант"
