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
    enter_num = str(enter_num)
    return reversed(enter_num)
enter_num = 1000

print('revers', timeit('revers(enter_num)', number=1000, globals=globals()))
print('revers_2', timeit('revers_2(enter_num)', number=1000, globals=globals()))
print('revers_3', timeit('revers_3(enter_num)', number=1000, globals=globals()))
print('revers_4', timeit('revers_4(enter_num)', number=1000, globals=globals()))


'''
Вывод: самая эффективная 3я функция со срезом, сравнима с ней и 4я(reversed)
1.Рекурсия самая медленная, потомучто сохраняет данные в стеке
2.Цикл намного быстрей рекурстии потомучто имеент сложность О(n)
3.Срез и (reversed) самыe быстрыe не понимаю почему,сложность тоже 
O(n), может быть потомучто меньше строк кода
'''
