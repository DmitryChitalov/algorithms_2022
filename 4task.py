import timeit


dictionary = {'персона': 'человек',
              'марафон': 'гонка бегунов длиной около 26 миль',
              'противостоять': 'оставаться сильным, несмотря на давление',
              'бежать': 'двигаться со скоростью'}


code_to_test_1 = """
dictionary = {'персона': 'человек',
              'марафон': 'гонка бегунов длиной около 26 миль',
              'противостоять': 'оставаться сильным, несмотря на давление',
              'бежать': 'двигаться со скоростью'}
dictionary['гонка'] = 12"""
elapsed_time_1 = timeit.timeit(code_to_test_1, number=1)*100
print(elapsed_time_1)


code_to_test_2 = """
dictionary = {'персона': 'человек',
              'марафон': 'гонка бегунов длиной около 26 миль',
              'противостоять': 'оставаться сильным, несмотря на давление',
              'бежать': 'двигаться со скоростью'}
dictionary['персона'] = ['человек прямоходящий']"""
elapsed_time_2 = timeit.timeit(code_to_test_2, number=1)*100
print(elapsed_time_2)



code_to_test_3 = """
dictionary = {'персона': 'человек',
              'марафон': 'гонка бегунов длиной около 26 миль',
              'противостоять': 'оставаться сильным, несмотря на давление',
              'бежать': 'двигаться со скоростью'}
del dictionary['марафон']"""
elapsed_time_3 = timeit.timeit(code_to_test_3, number=1)*100
print(elapsed_time_3)


print('----------------------------------------------------------------------------------------------------------------')


code_to_test_4 = """
from collections import OrderedDict
my_dict = {'kiwi': 4, 'apple': 5, 'cat': 3}
ordered_dict = OrderedDict(my_dict) 
ordered_dict['dog'] = 3"""
elapsed_time_4 = timeit.timeit(code_to_test_4, number=1)*100
print(elapsed_time_4)

code_to_test_5 = """
from collections import OrderedDict
my_dict = {'kiwi': 4, 'apple': 5, 'cat': 3}
ordered_dict = OrderedDict(my_dict) 
ordered_dict['kiwi'] = 10 
print(ordered_dict)"""
elapsed_time_5 = timeit.timeit(code_to_test_5, number=1)*100
print(elapsed_time_5)


code_to_test_6 = """
from collections import OrderedDict
my_dict = {'kiwi': 4, 'apple': 5, 'cat': 3}
ordered_dict = OrderedDict(my_dict) 
ordered_dict.pop('kiwi') 
print(ordered_dict) """
elapsed_time_6 = timeit.timeit(code_to_test_6, number=1)*100
print(elapsed_time_6)


#вывод:исходя из результатов замеров словарь работает значительно быстрее
#использовать Ordereddict не вижу смысла.










