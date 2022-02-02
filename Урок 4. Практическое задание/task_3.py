"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""


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


#  вариант решения
def revers_5(enter_num):
    return int(''.join(reversed(str(enter_num))))


enter_num = int(input('Введите число: '))

print(timeit(stmt='revers(enter_num)', globals=globals(), number=1000))
print(timeit(stmt='revers_2(enter_num)', globals=globals(), number=1000))
print(timeit(stmt='revers_3(enter_num)', globals=globals(), number=1000))
print(timeit(stmt='revers_4(enter_num)', globals=globals(), number=1000))
print(timeit(stmt='revers_5(enter_num)', globals=globals(), number=1000))

"""
Результаты
Введите число: 675
0.0012074499999998878
0.0008446580000001092
0.00045928800000005765
0.0006436230000002041
0.0009096079999997286
Эффективнее оказадась реализация последняя через join
самая меделенная первая
возможно спицифика работы join и заключается в обработке информации и и формировании и выделении необходимого буфера памяти
для каждой оперции отдельный и только один раз и используется для многопоточной обработки
"""
