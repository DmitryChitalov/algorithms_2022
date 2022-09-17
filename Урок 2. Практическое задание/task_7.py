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
class MyException(Exception):
    pass
def rec(num, summ=0, right_part=0):
    try:
        if int(num) < 1 and right_part == 0:
            raise MyException("wrong symbol")
        elif right_part == 0:
            right_part = int(num * (num + 1) / 2)
            # print(right_part)
            rec(num, summ=0, right_part=right_part)
        elif num >= 1:
            summ += num
            # print(num)
            rec(num-1, summ=summ, right_part=right_part)
        else:
            # print(sum)
            print(summ == right_part)
            return summ == right_part
    except MyException as e:
        print("Ошибка ввода! Требуется ввести число! Число должно быть натуральным!")
    except ValueError:
        print("Ошибка ввода! Требуется ввести число! Вы ввели не число!")
rec(5)


