"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return int(revers_num)
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def appending(enter_num):
    reversed_num = []
    enter_num = str(enter_num)
    enter_num = list(enter_num)
    for i in range(len(enter_num)):
        last_letter = enter_num.pop()
        reversed_num.append(last_letter)
    reversed_num = "".join(reversed_num)
    return int(reversed_num)


numbers = 3221754

test_revers = timeit.timeit('revers(numbers)', 'from __main__ import revers, numbers', number=100_000)
test_revers_2 = timeit.timeit('revers_2(numbers)', 'from __main__ import revers_2, numbers', number=100_000)
test_revers_3 = timeit.timeit('revers_3(numbers)', 'from __main__ import revers_3, numbers', number=100_000)
test_appending = timeit.timeit('appending(numbers)', 'from __main__ import appending, numbers', number=100_000)

print(f"Результат revers: {revers(numbers)}")
print(f"Результат revers_2: {revers_2(numbers)}")
print(f"Результат revers_3: {revers_3(numbers)}")
print(f"Результат appending: {appending(numbers)}\n")

print(f"Время test_revers: {test_revers}")  # 0.4915539000030549
print(f"Время test_revers_2: {test_revers_2}")  # 0.31191259999832255
print(f"Время test_revers_3: {test_revers_3}")  # 0.06923569999707979
print(f"Время test_appending: {test_appending}")  # 0.39294969999900786

# Наиболее эффективная функция через разворот строки, т.к. она выполняется за О(n) и есть "под капотом" у питона.
# Циклы второй и четвертой функции действуют дольше, но тоже со сложностью O(n)
# Рекурсия наиболее долго выполняется, и имеет время n!
