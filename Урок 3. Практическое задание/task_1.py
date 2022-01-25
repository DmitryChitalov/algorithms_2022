"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import random
from functools import wraps
from time import time



def timing(f):
    @wraps(f)
    def wrap(*args):
        ts = time()
        result = f(*args)
        te = time()
        print(f.__name__, te-ts)
        return result
    return wrap

test_list = []
test_dict = {}
#Сложность O(n)
@timing
def go_list():
    for i in range(10000):
        test_list.append(i+1)


go_list()
#Врем заполнения списска через append = 0.0010061264038085938

#Сложность O(n)
@timing
def go_dict():
    for i in range(10000):
        test_dict.setdefault(i+1, chr(97+i))


go_dict()
#Врем заполнения словаря через setdefault = 0.003990650177001953

"""
Заполнения списска через append в несколько раз быстрее
чам заполнения словаря через setdefault. Это связано с тем, 
что не нужно хэшировать данны, на что тратится время.
"""
n = random.randint(0, 9)

@timing
def plus_list():
    test_list[n] = n + n

@timing
def plus_dict():
    test_dict[n] = n + n

plus_list()
plus_dict()



@timing
def pop_list():
    test_list.pop(n)

@timing
def pop_dict():
    test_dict.pop(n)

pop_list()
pop_dict()

