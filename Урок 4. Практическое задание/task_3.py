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

nums = 123456789


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
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



# Вариант 4 мемоизация
def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def revers_4(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{revers_4(number // 10)}'


# Вариант 5 Встроиная функция join
def revers_5(enter_num):
    return reversed(str(enter_num))


# Вариант 6. Сокращенная версия от варианта 3
def revers_6(enter_num):
    return str(enter_num)[::-1]


print('Время выполнения. Вариант 1: ', end='')
print(timeit('revers(nums)', setup='from __main__ import revers, nums', number=1000))
print('Время выполнения. Вариант 2: ', end='')
print(timeit('revers_2(nums)', setup='from __main__ import revers_2, nums', number=1000))
print('Время выполнения. Вариант 3: ', end='')
print(timeit('revers_3(nums)', setup='from __main__ import revers_3, nums', number=1000))
print('Время выполнения. Вариант 4: ', end='')
print(timeit('revers_4(nums)', setup='from __main__ import revers_4, nums', number=1000))
print('Время выполнения. Вариант 5: ', end='')
print(timeit('revers_5(nums)', setup='from __main__ import revers_5, nums', number=1000))
print('Время выполнения. Вариант 6: ', end='')
print(timeit('revers_6(nums)', setup='from __main__ import revers_6, nums', number=1000))
print('---------------------------Однократное выполнение --------------------')

'''
Вариант 1. Рекурсивный метод, долгий метод, из-за задействованого стека вызовов и сохранения результатов вызова 
        в оперативной памяти.
Вариант 2. Такой же как и первый, но без рекурсии. Использован цикл с переназначением уже созданной переменной.
        Выполняется быстрее первого из-за отсутсвия необходимости сохранения результата каждого вызова.
Вариант 3. Быстрый способ. Скорость за счет использованя встроенного в Python среза, оптемизированного.
Вариант 4. Мемоизация. При однократном запуске скрипта самы долгий. Будет самым быстрым, только при многократном
        прогоне скрипта, при обработке большого массива данных.
Вариант 5. Самый быстрый способ, за счет испоьзования встроенной функции reversed. В отличае от варианта 4, 
        результат вычисления сразу передается в return, без создания промежуточных переменных.
Вариант 6. Тоже самый быстрый способ, за счет использования среза, т.е. встроенной функции. Упращенный вариант 4. 

Вывод: Самые быстрые варианты 5 и 6, за счет использования оптемизированных встроенных функций, без создания 
        промежуточных переменных, и передачей результата вычислений сразу в return.  
'''

