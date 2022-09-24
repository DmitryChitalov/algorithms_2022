def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return f'{orig_list} - отсортированный список'


orig_list = [randint(-100, 100) for i in range(10)]
print(f'{orig_list} - исходный список')
print(bubble_sort(orig_list))
time_func = timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000)
print(f'{time_func} - время выполнения функции')