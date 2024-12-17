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


def revers(enter_num: int, revers_num=0) -> int | str:
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num: int, revers_num=0) -> int | str:
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num: int) -> str:
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


revers_4 = lambda x, y='': revers_4(x[:-1], y + x[-1]) if x else y

revers_5 = lambda x: str(x)[::-1]

number = 56214462344432653564423

print(f"Рекурсивный метод без преобразования в тип str: "
      f"{timeit('revers(number)', globals=globals(), number=1000000)} секунд")
print(
    f"Перебор через цикл без преобразования в тип str: "
    f"{timeit('revers_2(number)', globals=globals(), number=1000000)} секунд")
print(
    f"Преобразования в тип str и через срезы разворот в обратном порядке: "
    f"{timeit('revers_3(number)', globals=globals(), number=1000000)} секунд")
print(
    f"Рекурсивный метод с преобразованием в тип str и разворот с использованием 'lambda' функции:"
    f"{timeit('revers(number)', globals=globals(), number=1000000)} секунд")
print(
    f"Лямбда-функция с преобразованием в тип str и через срезы разворот в обратном порядке: "
    f"{timeit('revers_5(number)', globals=globals(), number=1000000)} секунд")

"""
Методы, использующие строковые срезы, такие как revers_3 и revers_5,
являются наиболее эффективными, поскольку они используют оптимизированные встроенные операции.
Рекурсивные методы (например, revers и reversed_4) менее эффективны из-за накладных расходов на рекурсивные вызовы.
"""
