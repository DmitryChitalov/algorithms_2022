import timeit

code_to_test = """

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)"""


elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)



code_to_test_2 = """
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num"""

elapsed_time_2 = timeit.timeit(code_to_test_2, number=100)/100
print(elapsed_time_2)



code_to_test_3 = """
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num"""

elapsed_time_3 = timeit.timeit(code_to_test_3, number=100)/100
print(elapsed_time_3)




code_to_test_4 = """
def revers_4(enter_num):
    string = ''.join(reversed(enter_num))
    return string"""

elapsed_time_4 = timeit.timeit(code_to_test_4, number=100)/100
print(elapsed_time_4)





#Вывод:По результатом замеров видно что самый долгая функция первая так как это рекурсия. 7.400000000001155e-08
#На втором месте цикл while с сложностью O(N), цикл оказался быстрее рекурсии 5.1999999999968735e-08 
#Третие место разделяет встроенная функция reversed O(N) и срезO(N) встроенные функции всегда быстро работают, так же как и срезы.
# 4.8999999999986555e-08 
# 4.900000000002125e-08