"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для второго скрипта
"""

'''
Курс Основы языка Python
Задание:
Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
'''
from memory_profiler import profile
from collections import Counter


# старое решение
@profile
def get_non_repeat_nums(nums):
    repeat_nums = []
    non_repeat_nums = []
    for i in range(len(nums)):
        if nums[i] in non_repeat_nums:
            non_repeat_nums.remove(nums[i])
            repeat_nums.append(nums[i])
        elif nums[i] not in non_repeat_nums:
            non_repeat_nums.append(nums[i])
    return non_repeat_nums


@profile
def get_non_repeat_nums_2(nums):
    counter = {}
    for elem in nums:
        counter[elem] = counter.get(elem, 0) + 1
    rep_nums = {element: count for element, count in counter.items() if count > 1}.keys()
    non_repeat_nums = [num for num in nums if num not in rep_nums]
    return non_repeat_nums


# новое решение
@profile
def get_non_repeat_nums_new(nums):
    repeat_nums = []
    non_repeat_nums = []
    for i in range(len(nums)):
        if nums[i] in non_repeat_nums:
            non_repeat_nums.remove(nums[i])
            repeat_nums.append(nums[i])
        elif nums[i] not in non_repeat_nums:
            non_repeat_nums.append(nums[i])
    del repeat_nums
    return non_repeat_nums


@profile
def get_non_repeat_nums_2_new_1(nums):
    counter = {}
    for elem in nums:
        counter[elem] = counter.get(elem, 0) + 1
    rep_nums = {element: count for element, count in counter.items() if count > 1}.keys()
    del counter
    non_repeat_nums = [num for num in nums if num not in rep_nums]
    del rep_nums
    return non_repeat_nums


@profile
def get_non_repeat_nums_2_new_2(nums):
    rep_nums = (dict((x, nums.count(x)) for x in set(nums) if nums.count(x) > 1)).keys()
    non_repeat_nums = [num for num in nums if num not in rep_nums]
    del rep_nums
    return non_repeat_nums


@profile
def get_non_repeat_nums_2_new_3(nums):
    counter = Counter(nums)
    non_repeat_nums = [num for num in nums if
                       num not in {element: count for element, count in counter.items() if count > 1}.keys()]
    del counter
    return non_repeat_nums


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(get_non_repeat_nums(src))
print(get_non_repeat_nums_2(src))
print(get_non_repeat_nums_new(src))
print(get_non_repeat_nums_2_new_1(src))
print(get_non_repeat_nums_2_new_2(src))
print(get_non_repeat_nums_2_new_3(src))

# пытался оптимизировать код с помощью del, использования Counter, но цифры остались те же,
# вероятно, польза от del и Counter если и есть, то незначительная
