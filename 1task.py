import timeit

code_to_test = """

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)




code_to_test_2 = """

def func_2(nums):
    new_arr = []
    odd_squares = [new_arr.append(n) for n in range(len(nums)) if nums[n] % 2 == 0]
    print(odd_squares)"""

elapsed_time = timeit.timeit(code_to_test_2, number=100)/100
print(elapsed_time)



# В данном задании я преобразовал цикл и оператор if в list comprehension,благодаря этому удалось снизить время выполнения кода.