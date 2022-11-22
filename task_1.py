from random import randint
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_new(lst_obj):
    n = 1
    Flag = True
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                Flag = False
        if Flag is True:
            break
        n += 1
    return lst_obj


list_1 = [randint(-100, 100) for _ in range(100)]
sorted_list = [randint(-100, 100) for _ in range(100)]
sorted_list.sort(reverse=True)


print(bubble_sort(list_1[:]))
print('неотсортированный список')
print(timeit("bubble_sort(list_1[:])", globals=globals(), number=1000))

print(bubble_sort(sorted_list[:]))
print('отсортированный список')
print(timeit("bubble_sort(sorted_list[:])", globals=globals(), number=1000))

print(bubble_sort(list_1[:]))
print('неотсортированный список')
print(timeit("bubble_sort_new(list_1[:])", globals=globals(), number=1000))

print(bubble_sort(sorted_list[:]))
print('отсортированный список')
print(timeit("bubble_sort_new(sorted_list[:])", globals=globals(), number=1000))



"""
Результаты
неотсортированный список: 0.762711
                          0.7816587000000002
отсортированный список:   1.0826186
                          0.006487999999999605
Вывод: при сортировке массива очень небольшое преимущество будет у обычного пузырька, но если
массив уже отсортирован, то доработанный вариант будет намного быстрее, ведь после одного прохода он сразу
прекращает работу. В итоге, доработанный вариант будет эффективен только тогда, когда заранее неизвестно, что массив
отсортирован
"""