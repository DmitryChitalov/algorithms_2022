"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return                          # не понял что возвращает? может надо return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)   


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_my_4(enter_num, revers_num=''):
    if enter_num > 0:
        revers_num, enter_num = f'{revers_num}{enter_num % 10}', enter_num // 10
        return revers_my_4(enter_num, revers_num)
    return revers_num


def revers_my_5(enter_num):
    return ''.join(reversed(f'{enter_num}'))


enter_num = 77779999
print(revers(enter_num))
print('Revers № 1: ', timeit("revers(enter_num)", globals=globals(), number=100000))
print('===================================')
print(revers_2(enter_num))
print('Revers № 2: ', timeit("revers_2(enter_num)", globals=globals(), number=100000))
print('===================================')
print(revers_3(enter_num))
print('Revers № 3: ', timeit("revers_3(enter_num)", globals=globals(), number=100000))
print('===================================')
print(revers_my_4(enter_num))
print('My revers № 4: ', timeit("revers_my_4(enter_num)", globals=globals(), number=100000))
print('===================================')
print(revers_my_5(enter_num))
print('My revers № 5: ', timeit("revers_my_5(enter_num)", globals=globals(), number=100000))

"""
- Функция revers явно проигрывает остальным за счёт рекурсии и арифметических операций.
- Цикл и арифметических операций в функции revers_2 немного быстрее, но всё равно не самый лучший вариант по времени исполнения.
- Функция revers_3 (O(N)), в которой используется встроенная функция получения среза ЛУЧШАЯ.
- Моя функция revers_my_4, среднее между revers и revers_2 последнее место.
- Функция revers_my_5 лучше, но проигрывает Revers № 3.
"""