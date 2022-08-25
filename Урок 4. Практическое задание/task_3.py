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
    """Решил доработать функцию, т.к. она возвращала None, в условии указано 'вывести на экран'
    сначала добавил параметр rev в функцию, выглядело это так def revers(enter_num, revers_num=0, rev=0):
    при этом параметр rev подсвечен серым, если его убрать, функция работает. Помогите разобраться что происходит и
    почему это работает и можно ли так вообще делать?)
    """
    if enter_num == 0:
        revers.rev = revers_num
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
    return revers.rev


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


def revers_4(enter_num):
    rever = list(str(enter_num))
    rever.reverse()
    return ''.join(rever)


n = 111222333

print(revers(n))
print(revers_2(n))
print(revers_3(n))
print(revers_4(n))

print(f'Время работы функции {revers.__name__} - {timeit("revers(n)", globals=globals())}')
print(f'Время работы функции {revers_2.__name__} - {timeit("revers_2(n)", globals=globals())}')
print(f'Время работы функции {revers_3.__name__} - {timeit("revers_3(n)", globals=globals())}')
print(f'Время работы функции {revers_4.__name__} - {timeit("revers_4(n)", globals=globals())}')

"""
Время работы функции revers - 5.56696969999939
Время работы функции revers_2 - 3.5340578999985155
Время работы функции revers_3 - 0.750298599999951
Время работы функции revers_4 - 1.2945488999994268

В четвёртом варианте сделал через реверс списка с последующей сборкой в строку. Как видим, это быстрей первых двух 
функций, но дольше среза. В этом варианте проиграли срезу по времени  т.к. добавились операции создания списка из 
строки и сборки строки из списка, что привело к увеличению времени исполнения.
"""
