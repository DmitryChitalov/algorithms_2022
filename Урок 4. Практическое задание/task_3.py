"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
# увидел что в следующем коммите вы поменяли задание и убрали вариант профилировки через cProfile,
# поэтому не добавляю его
from timeit import timeit


def reverse_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        reverse_1(enter_num, revers_num)


def reverse_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def reverse_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def reverse_4(number, reverse_list):
    if number == 0:
        return ''.join(map(str, reverse_list))
    a = number % 10
    reverse_list.append(a)
    return reverse_4(number//10, reverse_list)


print(f"reverse_1: {timeit('reverse_1', globals=globals(), number=100000000)}")
print(f"reverse_2: {timeit('reverse_2', globals=globals(), number=100000000)}")
print(f"reverse_3: {timeit('reverse_3', globals=globals(), number=100000000)}")
print(f"reverse_4: {timeit('reverse_4', globals=globals(), number=100000000)}\n")

print('Вывод: не могу дать однозначный ответ что быстрее, все варианты выдают одинаково разные цифры, '
      'снизу собраны несколько выводов функции:\n')

print('reverse_1: 1.3919562, \
reverse_2: 1.5939799, \
reverse_3: 1.4876570999999998, \
reverse_4: 1.8515984999999997\n\
reverse_1: 1.6174716, \
reverse_2: 1.5049049, \
reverse_3: 1.3808365999999999, \
reverse_4: 1.3998065999999998\n\
reverse_1: 1.4732835, \
reverse_2: 1.4120622, \
reverse_3: 1.4919806000000002, \
reverse_4: 1.3767164999999997 \n\
reverse_1: 1.4033079, \
reverse_2: 1.4907501, \
reverse_3: 1.6939628999999998, \
reverse_4: 1.3871418999999996')
