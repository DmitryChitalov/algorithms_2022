from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    res = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return res

num_1 = [i for i in range(100)]
num_2 = [i for i in range(10000)]


print(timeit("func_1(num_1)", globals=globals(), number=10000))
print(timeit("func_2(num_1)", globals=globals(), number=10000))

print(timeit("func_1(num_2)", globals=globals(), number=10000))
print(timeit("func_2(num_2)", globals=globals(), number=10000))

'''
f_1: 0.09185979999999999
f_2: 0.06928999999999999

f_1: 9.1573613
f_2: 6.796389400000001
Через List Comprehension выполнение функции получается немного быстрее! 
Особенно если мы увеличим число исследуемого массива, то результат будет наглядно замечен! 

'''