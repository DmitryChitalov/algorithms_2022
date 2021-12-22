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
import time


# задание а)


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        print(time.time() - start_time, "seconds")

    return wrapper()


@time_decorator
def list_fill():  # O(n) --- список заполняется в два раза быстрее
    list_1 = [a for a in range(1, 1000)]
    print(list_1)


@time_decorator
def dict_fill():  # O(n) --- Запись у словаря будет медленнее потому что надо посчитать хэш и
    # положить по индексам, а в list() (чтобы добавить элемент в конец) достаточно  несколько байт записать в заранее
    # выделенную память
    dict_1 = {a: a for a in range(1, 1000)}
    print(dict_1)


# задание b)

dict_1 = {a: a for a in range(1, 1000)}
list_1 = [a for a in range(1, 1000)]

start_time_1 = time.time()
list_1[1] = 1
print(time.time() - start_time_1, "seconds (list modificate)")

start_time_2 = time.time()
dict_1['1'] = 100
print(time.time() - start_time_2, "seconds (dict modificate)")

start_time_3 = time.time()
list_1.remove(1)
print(time.time() - start_time_3, "seconds (list remove)")

start_time_4 = time.time()
del dict_1[1]
print(time.time() - start_time_4, "seconds (dict remove)")

# честно говоря не понял в чем загвоздка, но постоянно выдаются разные результаты для list и dict
# 7.152557373046875e-07 seconds (list modificate)
# 9.5367431640625e-07 seconds (dict modificate)
#
# 9.5367431640625e-07 seconds (list modificate)
# 1.1920928955078125e-06 seconds (dict modificate)
