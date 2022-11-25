"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!

Решите через рекурсию. В задании нельзя применять циклы.
"""


def compare(n):
    if n == 1:
        return n
    return n + compare(n - 1)




def main():
    n = int(input("Введите n: "))
    left_side_print = " + ".join([str(x) for x in range(1, n + 1)])
    right_side_print = f"{n} * ({n} + 1) / 2"

    right_side = n * (n + 1) / 2
    left_side = compare(n)

    if right_side == left_side:
        print(f"{left_side_print} = {right_side_print}")
    else:
        print(f"{left_side_print} != {right_side_print}")


if __name__ == '__main__':
    main()
