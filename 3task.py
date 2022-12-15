import timeit

#append
code_to_test = """
my_list = ['Apple',"Banana","Orange"]
my_list.append("Pineapple")
print(my_list)"""
elapsed_time_1 = timeit.timeit(code_to_test, number=10)
print(elapsed_time_1)


code_to_test_2 = """
from collections import deque
deq = deque(["Apple","Banana","Orange"])
deq.append('Pineapple')
print(deq)"""
elapsed_time_2 = timeit.timeit(code_to_test_2, number=10)
print(elapsed_time_2)

#pop
code_to_test_3 = """
my_list = ['Apple',"Banana","Orange"]
my_list.pop()
print(my_list)"""
elapsed_time_3 = timeit.timeit(code_to_test_3, number=10)
print(elapsed_time_3)


code_to_test_4 ="""
from collections import deque
deq = deque(["Apple","Banana","Orange"])
deq.pop()
print(deq)"""
elapsed_time_4= timeit.timeit(code_to_test_4, number=10)
print(elapsed_time_4)


#extend
code_to_test_5 = """
my_list = ['Apple',"Banana","Orange"]
my_list_2 = ['Mango','Pear']
my_list.extend(my_list_2)
print(my_list)"""
elapsed_time_5 = timeit.timeit(code_to_test_5, number=10)
print(elapsed_time_5)


code_to_test_6 ="""
from collections import deque
deq = deque(["Apple","Banana","Orange"])
my_list_2 = ['Mango','Pear']
deq.extend(my_list_2)
print(deq)"""
elapsed_time_6= timeit.timeit(code_to_test_6, number=10)
print(elapsed_time_6)

print('---------------------------------------------------------------------------------------------------------------------------------------------------------')



#2)appendleft
code_to_test = """
my_list = ['Apple',"Banana","Orange"]
my_list.append("Pineapple")
print(my_list)"""
elapsed_time_1 = timeit.timeit(code_to_test, number=10)
print(elapsed_time_1)


code_to_test_2 = """
from collections import deque
deq = deque(["Apple","Banana","Orange"])
deq.appendleft('Pineapple')
print(deq)"""
elapsed_time_2 = timeit.timeit(code_to_test_2, number=10)
print(elapsed_time_2)

#pop
code_to_test_3 = """
my_list = ['Apple',"Banana","Orange"]
my_list.pop()
print(my_list)"""
elapsed_time_3 = timeit.timeit(code_to_test_3, number=10)
print(elapsed_time_3)


code_to_test_4 = """
from collections import deque
deq = deque(["Apple","Banana","Orange"])
deq.popleft()
print(deq)"""
elapsed_time_4= timeit.timeit(code_to_test_4, number=10)
print(elapsed_time_4)


#extend
code_to_test_5 = """
my_list = ['Apple',"Banana","Orange"]
my_list_2 = ['Mango','Pear']
my_list.extend(my_list_2)
print(my_list)"""
elapsed_time_5 = timeit.timeit(code_to_test_5, number=10)
print(elapsed_time_5)


code_to_test_6 = """
from collections import deque
deq = deque(["Apple","Banana","Orange"])
my_list_2 = ['Mango','Pear']
deq.extendleft(my_list_2)
print(deq)"""
elapsed_time_6= timeit.timeit(code_to_test_6, number=10)
print(elapsed_time_6)


print('---------------------------------------------------------------------------------------------------------------------------------------------------------')




#получение элемента списка
code_to_test_5 = """
my_list = ['Apple',"Banana","Orange"]
print(my_list[0])"""
elapsed_time_5 = timeit.timeit(code_to_test_5, number=10)
print(elapsed_time_5)


code_to_test_6 = """
from collections import deque
deq = deque(["Apple","Banana","Orange"])
print(deq[0])"""
elapsed_time_6= timeit.timeit(code_to_test_6, number=10)
print(elapsed_time_6)


#Вывод по первому пункту:дека затрачивает больше времени,лист меньше.
#по второну пункту:дека оказалась чуть бытрее списка. Как и предполагалось.
#по третьему: лист оказался быстрее в доступе по индексу.