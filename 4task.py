from collections import Counter
import timeit
array = [1, 3, 1, 3, 4, 5, 1]




code_to_test = """

def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)

code_to_test = """

def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'"""
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)


code_to_test = """
def func_3():
    l = ['1', '3', '1', '3', '4', '5','1']
    return f'Чаще всего встречается число{Counter(l).most_common(1)}раза оно появилось в массиве'"""
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)







#7.099999999999468e-08
#7.100000000002937e-08
#3.689999999999943e-07  судя по результатам ускорить задачу удалось.

#print(func_1())
#print(func_2())
#print(func_3())