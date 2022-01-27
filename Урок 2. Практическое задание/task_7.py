"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать функцибю-рекурсию только для левой части выражения!
Результат нужно сверить с правой частью.
Решите через рекурсию. Решение через цикл не принимается.
"""

def get_sum(number):
    if number == 0:
        return 0
    else:
        return number + get_sum(number-1)

num = int(input('Введите число для проверки: '))
formula = num*(num+1)/2
print(f'{1}.....{num} = {get_sum(num)} \n'
      f'n(n+1)/2 = {formula} \n'
      f'#доказано ')
