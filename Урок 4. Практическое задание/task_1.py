"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit

nums = [num for num in range(10)]

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(f'func_1 результат замера: '
      f'{timeit("func_1(nums)", "from __main__ import func_1", globals=globals(), number=1000000)} '
      f'сек')
print('*'*60)

nums = [num for num in range(10)]
new_arr = [i for i, num in enumerate(nums) if num % 2 == 0]

# new_arr = [i if j % 2 == 0 else None for i, j in enumerate(nums)] вариант плохо работает
print(f'generator результат замера: '
      f'{timeit("new_arr = [i for i, num in enumerate(nums) if num % 2 == 0]", globals=globals(), number=1000000)}')
print('*'*60)


nums = [num for num in range(100)]


def func_2(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr




print(f'func_2 результат замера: '
      f'{timeit("func_2(nums)", "from __main__ import func_1", globals=globals(), number=1000000)} сек')
print('*'*60)


new_arr = [i for i, num in enumerate(nums) if num % 2 == 0]

print(f'generator результат замера: '
      f'{timeit("new_arr = [i for i, num in enumerate(nums) if num % 2 == 0]", globals=globals(), number=1000000)}')
'''
Результаты замеров

func_1 результат замера: 0.8944282 сек
************************************************************
generator результат замера: 0.8811345
************************************************************
func_2 результат замера: 6.9086071 сек
************************************************************
generator результат замера: 5.583961799999999

здесь видно, что list comprehension работает быстрее,
 чем встроенная функция "enumerate"

освежил в памяти вопрос о генераторах
https://pythonist.ru/generatory-python-ih-sozdanie-i-ispolzovanie/



'''