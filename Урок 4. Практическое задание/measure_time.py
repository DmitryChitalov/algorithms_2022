from timeit import Timer
from timeit import timeit

# Реализуем модуль измерения времени выполнения функций.
print('Измерения для списка из 100 элементов на 100 прогонов.')
t1 = Timer(stmt="func_1(nums_100)", setup="from task_1 import func_1, nums_100")
print("list append for nums_100 ", t1.timeit(number=100), "seconds")

t2 = Timer(stmt="func_concat(nums_100)", setup="from task_1 import func_concat, nums_100")
print("list concat for nums_100 ", t2.timeit(number=100), "seconds")

t3 = Timer(stmt="func_list_comp(nums_100)", setup="from task_1 import func_list_comp, nums_100")
print("list comprehension for nums_100 ", t3.timeit(number=100), "seconds")

print('\nИзмерения для списка из 1000 элементов на 100 прогонов.')
t1 = Timer(stmt="func_1(nums_1000)", setup="from task_1 import func_1, nums_1000")
print("list append for nums_1000 ", t1.timeit(number=100), "seconds")

t2 = Timer(stmt="func_concat(nums_1000)", setup="from task_1 import func_concat, nums_1000")
print("list concat for nums_1000 ", t2.timeit(number=100), "seconds")

t3 = Timer(stmt="func_list_comp(nums_1000)", setup="from task_1 import func_list_comp, nums_1000")
print("list comprehension for nums_1000 ", t3.timeit(number=100), "seconds")

print('\nИзмерения для списка из 10000 элементов на 100 прогонов.')
t1 = Timer(stmt="func_1(nums_10000)", setup="from task_1 import func_1, nums_10000")
print("list append for nums_10000 ", t1.timeit(number=100), "seconds")

t2 = Timer(stmt="func_concat(nums_10000)", setup="from task_1 import func_concat, nums_10000")
print("list concat for nums_100000 ", t2.timeit(number=100), "seconds")

t3 = Timer(stmt="func_list_comp(nums_10000)", setup="from task_1 import func_list_comp, nums_10000")
print("list comprehension for nums_10000 ", t3.timeit(number=100), "seconds")

# Оптимизируем локальные замеры времени.
print("\nlist append for nums_100 ", timeit("func_1(nums_100)", setup="from task_1 import func_1, nums_100",
                                            number=100))

print("\nlist concat for nums_100 ", timeit("func_concat(nums_100)", setup="from task_1 import func_concat, nums_100",
                                            number=100))

print("\nlist comprehension for nums_100 ", timeit("func_list_comp(nums_100)",
                                                   setup="from task_1 import func_list_comp, nums_100", number=100))

# Определим время выполнения выражения с конкотенацией 1000 элементов на 1000 прогонов.
print("\nlist concat for nums_1000 ", timeit("""
new_arr = []
for i in range(1000):
    if i % 2 == 0:
        new_arr = new_arr + [i]""", number=1000))

# Оптимально использовать модуль измерения времени, чтобы не загромождать код программы.
